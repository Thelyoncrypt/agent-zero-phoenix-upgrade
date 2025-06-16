# python/tools/general_code_execution_tool.py
import asyncio
import os
import sys
import tempfile
import uuid
from pathlib import Path
from typing import List, Optional, Tuple, Dict, Any
from python.tools.response import Response
from python.tools.stream_protocol_tool import StreamEventType

class GeneralCodeExecutionTool:
    """
    Tool for executing code in various runtimes (Python, Node.js, Terminal) with real-time output streaming.
    Supports streaming stdout/stderr via CODE_EXECUTION_OUTPUT events.
    """
    
    def __init__(self, agent_id: str, agent=None):
        self.agent_id = agent_id
        self.agent = agent
        self.name = "code_execution"
        self.description = "Execute code in Python, Node.js, or terminal with real-time output streaming"
        
    async def _read_stream(self, stream: asyncio.StreamReader, stream_name: str, tool_call_id: str):
        """Helper to read a stream and emit events for each chunk."""
        output_buffer = ""
        while True:
            try:
                # Read chunks of data for real-time streaming
                chunk_bytes = await asyncio.wait_for(stream.read(4096), timeout=0.1)
                if not chunk_bytes:  # EOF
                    break
                
                output_chunk = chunk_bytes.decode(errors='replace')
                output_buffer += output_chunk
                
                # Emit streaming event
                payload = {"source": stream_name, "tool_call_id": tool_call_id}
                if stream_name == "stdout":
                    payload["stdout"] = output_chunk
                else:  # stderr
                    payload["stderr"] = output_chunk
                
                if self.agent:
                    await self.agent._emit_stream_event(StreamEventType.CODE_EXECUTION_OUTPUT, payload)
                
            except asyncio.TimeoutError:
                # No new data, continue trying
                continue
            except Exception as e:
                print(f"Error reading stream {stream_name}: {e}")
                break
                
        return output_buffer

    async def _execute_process_streaming(
        self, 
        cmd_args: List[str], 
        work_dir: str, 
        timeout: int,
        input_data: Optional[bytes] = None,
        tool_call_id: str = "default_exec_id"
    ) -> Tuple[str, str, Optional[int]]:
        """Runs a process, captures output, and streams stdout/stderr."""
        full_stdout = ""
        full_stderr = ""
        exit_code = None

        try:
            process = await asyncio.create_subprocess_exec(
                *cmd_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE if input_data else None,
                cwd=work_dir
            )

            if input_data and process.stdin:
                process.stdin.write(input_data)
                await process.stdin.drain()
                process.stdin.close()

            # Concurrently read stdout and stderr
            stdout_task = asyncio.create_task(self._read_stream(process.stdout, "stdout", tool_call_id))
            stderr_task = asyncio.create_task(self._read_stream(process.stderr, "stderr", tool_call_id))

            # Wait for process to complete OR timeout
            try:
                await asyncio.wait_for(process.wait(), timeout=timeout)
                exit_code = process.returncode
            except asyncio.TimeoutError:
                process.terminate()
                try:
                    await asyncio.wait_for(process.wait(), timeout=5.0)
                except asyncio.TimeoutError:
                    process.kill()
                    await process.wait()
                exit_code = -99  # Custom timeout exit code
                timeout_msg = f"Execution timed out after {timeout} seconds."
                if self.agent:
                    await self.agent._emit_stream_event(
                        StreamEventType.CODE_EXECUTION_OUTPUT, 
                        {"stderr": timeout_msg, "source": "timeout", "tool_call_id": tool_call_id}
                    )
                full_stderr += f"\n[SYSTEM: {timeout_msg}]\n"

            # Ensure streams are fully read after process exit
            full_stdout = await stdout_task
            full_stderr += await stderr_task

        except FileNotFoundError:
            fnf_msg = f"Command or runtime not found: {cmd_args[0]}"
            if self.agent:
                await self.agent._emit_stream_event(
                    StreamEventType.CODE_EXECUTION_OUTPUT, 
                    {"stderr": fnf_msg, "source": "error", "tool_call_id": tool_call_id}
                )
            return "", fnf_msg, -100
        except Exception as e:
            err_msg = f"Error during code execution setup: {str(e)}"
            if self.agent:
                await self.agent._emit_stream_event(
                    StreamEventType.CODE_EXECUTION_OUTPUT, 
                    {"stderr": err_msg, "source": "error", "tool_call_id": tool_call_id}
                )
            return "", err_msg, -101
        
        return full_stdout, full_stderr, exit_code

    async def execute(
        self, 
        runtime: str, 
        code: str, 
        work_dir: Optional[str] = None,
        timeout: int = 30,
        save_to_file: bool = False,
        filename: Optional[str] = None,
        **kwargs
    ) -> Response:
        """
        Execute code in the specified runtime with real-time output streaming.
        
        Args:
            runtime: "python", "nodejs", or "terminal"
            code: Code to execute
            work_dir: Working directory (defaults to current)
            timeout: Execution timeout in seconds
            save_to_file: Whether to save code to a file before execution
            filename: Custom filename for saved code
        """
        try:
            # Get tool call ID for event correlation
            tool_call_id = str(uuid.uuid4())
            if self.agent and hasattr(self.agent, 'context'):
                tool_call_id = self.agent.context.get_custom_data('current_tool_call_event_id', tool_call_id)

            # Set working directory
            current_work_dir = work_dir or os.getcwd()
            if not os.path.exists(current_work_dir):
                os.makedirs(current_work_dir, exist_ok=True)

            stdout = ""
            stderr = ""
            exit_code = 0
            script_path = None

            if runtime == "terminal":
                # Terminal execution using shell
                try:
                    process = await asyncio.create_subprocess_shell(
                        code,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                        cwd=current_work_dir
                    )
                    
                    stdout_bytes, stderr_bytes = await asyncio.wait_for(
                        process.communicate(), timeout=timeout
                    )
                    stdout = stdout_bytes.decode(errors='replace')
                    stderr = stderr_bytes.decode(errors='replace')
                    exit_code = process.returncode
                    
                    # Emit output events for terminal
                    if stdout and self.agent:
                        await self.agent._emit_stream_event(
                            StreamEventType.CODE_EXECUTION_OUTPUT,
                            {"stdout": stdout, "source": "stdout", "tool_call_id": tool_call_id}
                        )
                    if stderr and self.agent:
                        await self.agent._emit_stream_event(
                            StreamEventType.CODE_EXECUTION_OUTPUT,
                            {"stderr": stderr, "source": "stderr", "tool_call_id": tool_call_id}
                        )
                        
                except asyncio.TimeoutError:
                    process.terminate()
                    await asyncio.wait_for(process.wait(), 5.0)
                    stdout = ""
                    stderr = f"Terminal execution timed out after {timeout}s."
                    exit_code = -99
                    if self.agent:
                        await self.agent._emit_stream_event(
                            StreamEventType.CODE_EXECUTION_OUTPUT,
                            {"stderr": stderr, "source": "timeout", "tool_call_id": tool_call_id}
                        )

            elif runtime == "python":
                # Python execution
                if save_to_file or filename:
                    # Save to specified file
                    script_name = filename or f"script_{tool_call_id[:8]}.py"
                    script_path = os.path.join(current_work_dir, script_name)
                    with open(script_path, 'w', encoding='utf-8') as f:
                        f.write(code)
                    script_to_run = script_path
                else:
                    # Create temporary file
                    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                        f.write(code)
                        script_to_run = f.name

                cmd_args = [sys.executable, script_to_run]
                stdout, stderr, exit_code = await self._execute_process_streaming(
                    cmd_args, current_work_dir, timeout, tool_call_id=tool_call_id
                )

                # Cleanup temporary file
                if not save_to_file and not filename:
                    try:
                        os.unlink(script_to_run)
                    except:
                        pass

            elif runtime == "nodejs":
                # Node.js execution
                if save_to_file or filename:
                    # Save to specified file
                    script_name = filename or f"script_{tool_call_id[:8]}.js"
                    script_path = os.path.join(current_work_dir, script_name)
                    with open(script_path, 'w', encoding='utf-8') as f:
                        f.write(code)
                    script_to_run = script_path
                else:
                    # Create temporary file
                    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
                        f.write(code)
                        script_to_run = f.name

                cmd_args = ["node", script_to_run]
                stdout, stderr, exit_code = await self._execute_process_streaming(
                    cmd_args, current_work_dir, timeout, tool_call_id=tool_call_id
                )

                # Cleanup temporary file
                if not save_to_file and not filename:
                    try:
                        os.unlink(script_to_run)
                    except:
                        pass

            else:
                return Response(
                    success=False,
                    message=f"Unsupported runtime: {runtime}",
                    error=f"Runtime '{runtime}' is not supported. Use 'python', 'nodejs', or 'terminal'."
                )

            # Prepare result data
            result_data = {
                "runtime": runtime,
                "stdout": stdout,
                "stderr": stderr,
                "exit_code": exit_code,
                "work_dir": current_work_dir,
                "script_path": script_path,
                "execution_time": timeout,  # Could be actual time if measured
                "tool_call_id": tool_call_id
            }

            success = exit_code == 0
            message = f"Code executed successfully in {runtime}" if success else f"Code execution failed in {runtime} (exit code: {exit_code})"

            return Response(
                success=success,
                message=message,
                data=result_data
            )

        except Exception as e:
            error_msg = f"Error executing code: {str(e)}"
            if self.agent:
                await self.agent._emit_stream_event(
                    StreamEventType.CODE_EXECUTION_OUTPUT,
                    {"stderr": error_msg, "source": "error", "tool_call_id": tool_call_id}
                )
            return Response(
                success=False,
                message=error_msg,
                error=str(e)
            )
