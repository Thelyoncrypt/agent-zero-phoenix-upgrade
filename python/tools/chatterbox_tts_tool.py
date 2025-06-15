# python/tools/chatterbox_tts_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any, Optional
import base64
import asyncio
import tempfile # For saving audio temporarily if needed
from pathlib import Path # For path manipulation
import uuid
import numpy as np
import torch

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

# Import TTS handler components
from python.agents.tts_agent.chatterbox_handler import ChatterboxTTSHandler, ChatterboxVCHandler

class ChatterboxTTSTool(Tool):
    """
    Chatterbox TTS and Voice Conversion tool for Agent Zero.
    """
    _tts_handler_instance: Optional[ChatterboxTTSHandler] = None
    _vc_handler_instance: Optional[ChatterboxVCHandler] = None
    _handler_lock = asyncio.Lock()

    @classmethod
    async def get_tts_handler(cls, device: str) -> ChatterboxTTSHandler:
        async with cls._handler_lock:
            if cls._tts_handler_instance is None:
                cls._tts_handler_instance = ChatterboxTTSHandler(device=device)
            # Ensure model is loaded within handler if not already
            await cls._tts_handler_instance._ensure_model_loaded()
        return cls._tts_handler_instance

    @classmethod
    async def get_vc_handler(cls, device: str) -> ChatterboxVCHandler:
        async with cls._handler_lock:
            if cls._vc_handler_instance is None:
                cls._vc_handler_instance = ChatterboxVCHandler(device=device)
            # Ensure VC model is loaded within handler if not already
            await cls._vc_handler_instance._ensure_vc_model_loaded()
        return cls._vc_handler_instance

    def __init__(self, agent, **kwargs):
        args_schema = {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["generate_speech", "generate_speech_stream", "voice_conversion"],
                    "description": "Action to perform: generate_speech (save to file), generate_speech_stream (stream audio chunks), or voice_conversion"
                },
                "text": {
                    "type": "string",
                    "description": "Text to convert to speech (for generate_speech and generate_speech_stream actions)"
                },
                "generate_speech_stream": {
                    "type": "string",
                    "description": "Text to convert to speech and stream as audio chunks (for generate_speech_stream action)"
                },
                "chunk_size_ms": {
                    "type": "integer",
                    "description": "Size of audio chunks in milliseconds for streaming (default: 1000ms, for generate_speech_stream action)",
                    "default": 1000
                },
                "stream_id": {
                    "type": "string",
                    "description": "Unique identifier for the audio stream (auto-generated if not provided, for generate_speech_stream action)"
                },
                "voice_id": {
                    "type": "string",
                    "description": "Voice identifier for TTS (optional, uses default if not specified)"
                },
                "source_audio_path": {
                    "type": "string",
                    "description": "Path to source audio file (for voice_conversion action)"
                },
                "target_voice_id": {
                    "type": "string",
                    "description": "Target voice identifier for voice conversion (for voice_conversion action)"
                }
            },
            "required": ["action"]
        }

        super().__init__(agent, name="chatterbox_tts_tool",
                         description="Generates speech from text (TTS) or performs voice conversion (VC) using Chatterbox models with streaming support.",
                         args_schema=args_schema,
                         **kwargs)
        self.device = agent.config.get("tts_device", agent.config.get("device", "cpu")) # Get device from agent config
        # Handlers will be fetched on demand to ensure model loading happens in async context
        print(f"ChatterboxTTSTool initialized for agent {agent.agent_name}. Handlers will use device: {self.device}")

    async def _emit_tts_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        """Helper to emit TTS related events (could be PROGRESS_UPDATE or a custom TTS event)."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"ChatterboxTTSTool: StreamProtocol not available, logging event: {action_name} - {status}")
            return
            
        payload = {"source_tool": "chatterbox_tts", "action": action_name, "status": status}
        if details:
            payload.update(details)
        
        if hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(StreamEventType.PROGRESS_UPDATE, payload)
        else:
            print(f"ChatterboxTTSTool: Agent does not have _emit_stream_event method. Cannot emit PROGRESS_UPDATE.")

    async def execute(self, **kwargs) -> ToolResponse:
        """
        Execute Chatterbox TTS/VC operations.
        
        Args:
            action (str): "generate_speech" or "convert_voice".
            **kwargs: Arguments for the action.
        """
        action = kwargs.get("action")
        if not action:
            return ToolResponse("Error: 'action' is required for ChatterboxTTS operations.", error=True)

        try:
            if action == "generate_speech":
                tts_handler = await self.get_tts_handler(self.device)
                text = kwargs.get("text")
                if not text: return ToolResponse("Error: 'text' is required for generate_speech.", error=True)

                audio_prompt_path = kwargs.get("audio_prompt_path")
                exaggeration = float(kwargs.get("exaggeration", 0.5))
                cfg_weight = float(kwargs.get("cfg_weight", 0.5))
                temperature = float(kwargs.get("temperature", 0.8))

                return await self._generate_speech(tts_handler, text, audio_prompt_path, exaggeration, cfg_weight, temperature)

            elif action == "generate_speech_stream":
                tts_handler = await self.get_tts_handler(self.device)
                text = kwargs.get("text") or kwargs.get("generate_speech_stream")
                if not text: return ToolResponse("Error: 'text' or 'generate_speech_stream' is required for generate_speech_stream.", error=True)

                chunk_size_ms = kwargs.get("chunk_size_ms", 1000)
                stream_id = kwargs.get("stream_id") or str(uuid.uuid4())
                audio_prompt_path = kwargs.get("audio_prompt_path")
                exaggeration = float(kwargs.get("exaggeration", 0.5))
                cfg_weight = float(kwargs.get("cfg_weight", 0.5))
                temperature = float(kwargs.get("temperature", 0.8))

                return await self._generate_speech_stream(tts_handler, text, stream_id, chunk_size_ms, audio_prompt_path, exaggeration, cfg_weight, temperature)

            elif action == "convert_voice":
                vc_handler = await self.get_vc_handler(self.device)
                source_audio_path = kwargs.get("source_audio_path")
                target_voice_path = kwargs.get("target_voice_path")
                if not source_audio_path or not target_voice_path:
                    return ToolResponse("Error: 'source_audio_path' and 'target_voice_path' required.", error=True)

                cfg_weight = float(kwargs.get("cfg_weight", 0.5))
                temperature = float(kwargs.get("temperature", 0.8))

                return await self._convert_voice(vc_handler, source_audio_path, target_voice_path, cfg_weight, temperature)
            else:
                return ToolResponse(f"Unknown ChatterboxTTSTool action: {action}", error=True)

        except RuntimeError as rne: # Catch model loading errors specifically
            error_message = f"ChatterboxTTSTool runtime error (likely model loading) during action '{action}': {str(rne)}"
            print(error_message)
            await self._emit_tts_event(action, "error", {"error": str(rne), "type": "RuntimeError"})
            return ToolResponse(message=error_message, error=True)
        except Exception as e: # General errors
            import traceback
            error_message = f"ChatterboxTTSTool error during action '{action}': {str(e)}\n{traceback.format_exc()}"
            print(error_message)
            await self._emit_tts_event(action, "error", {"error": str(e)})
            return ToolResponse(message=error_message, error=True)

    async def _generate_speech(self, tts_handler: ChatterboxTTSHandler, text: str, audio_prompt_path: Optional[str],
                               exaggeration: float, cfg_weight: float, temperature: float) -> ToolResponse:
        await self._emit_tts_event("generate_speech", "starting", {"text_length": len(text), "prompt": bool(audio_prompt_path)})

        sr, audio_bytes = await tts_handler.generate_speech(
            text, audio_prompt_path, exaggeration, cfg_weight, temperature
        )

        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')

        # Create a temporary file path for the audio.
        # The UI will need an endpoint to fetch this if it doesn't handle base64 directly.
        # Agent Zero's work_dir is /root in Docker, or ./work_dir locally.
        # Let's use a subdirectory in tmp for TTS outputs for now.

        # Ensure tmp/tts_output directory exists
        tts_output_dir = Path(self.agent.context.get_custom_data("work_dir_path", "work_dir")) / "tmp" / "tts_output"
        tts_output_dir.mkdir(parents=True, exist_ok=True) # Agent Zero might need a helper for this

        temp_audio_filename = f"tts_output_{uuid.uuid4()}.wav"
        temp_audio_filepath = tts_output_dir / temp_audio_filename

        try:
            # Save the raw bytes as a .wav file using torchaudio or soundfile
            # For raw bytes (assuming float32 PCM), need to construct a WAV header or use a library
            # Torchaudio is a dependency of chatterbox, so it should be available.
            import torchaudio
            # Convert raw bytes back to tensor
            audio_tensor = torch.from_numpy(np.frombuffer(audio_bytes, dtype=np.float32))
            if audio_tensor.ndim == 1: audio_tensor = audio_tensor.unsqueeze(0) # Add channel dim if mono

            await asyncio.to_thread(torchaudio.save, str(temp_audio_filepath), audio_tensor, sr)
            print(f"ChatterboxTTSTool: Saved generated speech to {temp_audio_filepath}")

            # The URL should be relative to how work_dir files are served by Agent Zero's API
            # e.g., if /api/download_work_dir_file takes path relative to work_dir
            # work_dir_path = self.agent.context.get_custom_data("work_dir_path", "work_dir") -> root
            # relative_path = temp_audio_filepath.relative_to(work_dir_path) -> tmp/tts_output/filename.wav
            # This assumes work_dir is accessible directly.
            # If Agent Zero uses /root as work_dir in Docker, path becomes /tmp/tts_output/filename.wav
            # For now, use an absolute-like path that the /api/download_work_dir_file can resolve from base_dir
            # This needs careful handling of Agent Zero's file serving.
            # The download_work_dir_file API takes paths relative to the *root of the work_dir*.
            # If work_dir is /root (docker) or ./work_dir (local), then path should be "tmp/tts_output/..."
            relative_audio_path = f"tmp/tts_output/{temp_audio_filename}"


        except Exception as e:
            print(f"ChatterboxTTSTool: Error saving TTS audio to file: {e}")
            relative_audio_path = None # Indicate save error

        result_details = {
            "sample_rate": sr,
            "audio_path": relative_audio_path if relative_audio_path else "Error saving audio", # Relative path for API download
            "audio_data_base64_preview": audio_base64[:256] + "..." if audio_base64 else None, # Small preview
            "text_length": len(text),
            "audio_duration_seconds": len(audio_bytes) / (sr * np.dtype(np.float32).itemsize) # Correct duration for float32
        }
        await self._emit_tts_event("generate_speech", "completed", result_details)
        return ToolResponse(message="Speech generated successfully." + (f" Saved to {relative_audio_path}" if relative_audio_path else ""), data=result_details, success=True)

    async def _generate_speech_stream(self, tts_handler: ChatterboxTTSHandler, text: str, stream_id: str,
                                    chunk_size_ms: int, audio_prompt_path: Optional[str],
                                    exaggeration: float, cfg_weight: float, temperature: float) -> ToolResponse:
        """Generate speech and stream it as audio chunks via AG-UI events."""
        await self._emit_tts_event("generate_speech_stream", "starting", {
            "text_length": len(text),
            "stream_id": stream_id,
            "chunk_size_ms": chunk_size_ms,
            "prompt": bool(audio_prompt_path)
        })

        # Emit TTS stream start event
        if STREAM_PROTOCOL_AVAILABLE and hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(StreamEventType.TTS_STREAM_START, {
                "stream_id": stream_id,
                "text": text,
                "chunk_size_ms": chunk_size_ms,
                "total_estimated_chunks": max(1, len(text) // 50)  # Rough estimate
            })

        try:
            # Generate the full audio first (Chatterbox doesn't support true streaming)
            sr, audio_bytes = await tts_handler.generate_speech(
                text, audio_prompt_path, exaggeration, cfg_weight, temperature
            )

            # Convert to audio tensor for chunking
            audio_tensor = torch.from_numpy(np.frombuffer(audio_bytes, dtype=np.float32))
            if audio_tensor.ndim == 1:
                audio_tensor = audio_tensor.unsqueeze(0)  # Add channel dim if mono

            # Calculate chunk size in samples
            chunk_size_samples = int((chunk_size_ms / 1000.0) * sr)
            total_samples = audio_tensor.shape[-1]
            total_chunks = (total_samples + chunk_size_samples - 1) // chunk_size_samples

            chunks_sent = 0
            for i in range(0, total_samples, chunk_size_samples):
                chunk_tensor = audio_tensor[:, i:i + chunk_size_samples]

                # Convert chunk back to bytes
                chunk_bytes = chunk_tensor.numpy().astype(np.float32).tobytes()
                chunk_base64 = base64.b64encode(chunk_bytes).decode('utf-8')

                # Emit audio chunk event
                if STREAM_PROTOCOL_AVAILABLE and hasattr(self.agent, '_emit_stream_event'):
                    await self.agent._emit_stream_event(StreamEventType.AUDIO_CHUNK, {
                        "stream_id": stream_id,
                        "chunk_index": chunks_sent,
                        "total_chunks": total_chunks,
                        "audio_data": chunk_base64,
                        "sample_rate": sr,
                        "chunk_duration_ms": (chunk_tensor.shape[-1] / sr) * 1000,
                        "is_final": chunks_sent == total_chunks - 1
                    })

                chunks_sent += 1

                # Small delay to simulate streaming (optional)
                await asyncio.sleep(0.01)

            # Emit TTS stream end event
            if STREAM_PROTOCOL_AVAILABLE and hasattr(self.agent, '_emit_stream_event'):
                await self.agent._emit_stream_event(StreamEventType.TTS_STREAM_END, {
                    "stream_id": stream_id,
                    "total_chunks_sent": chunks_sent,
                    "total_duration_ms": (total_samples / sr) * 1000,
                    "sample_rate": sr
                })

            result_details = {
                "stream_id": stream_id,
                "chunks_sent": chunks_sent,
                "total_duration_ms": (total_samples / sr) * 1000,
                "sample_rate": sr,
                "text_length": len(text),
                "chunk_size_ms": chunk_size_ms
            }

            await self._emit_tts_event("generate_speech_stream", "completed", result_details)
            return ToolResponse(
                message=f"Speech streaming completed. Sent {chunks_sent} audio chunks for stream {stream_id}.",
                data=result_details,
                success=True
            )

        except Exception as e:
            # Emit error event
            if STREAM_PROTOCOL_AVAILABLE and hasattr(self.agent, '_emit_stream_event'):
                await self.agent._emit_stream_event(StreamEventType.TTS_STREAM_END, {
                    "stream_id": stream_id,
                    "error": str(e),
                    "status": "error"
                })
            raise  # Re-raise to be handled by the main execute method

    async def _convert_voice(self, vc_handler: ChatterboxVCHandler, source_audio_path: str,
                            target_voice_path: str, cfg_weight: float, temperature: float) -> ToolResponse:
        await self._emit_tts_event("convert_voice", "starting", {
            "source": source_audio_path,
            "target_prompt": target_voice_path,
            "cfg_weight": cfg_weight,
            "temperature": temperature
        })

        sr, audio_bytes = await vc_handler.convert_voice(source_audio_path, target_voice_path, cfg_weight, temperature)

        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')

        # Save the converted audio to a file similar to TTS
        vc_output_dir = Path(self.agent.context.get_custom_data("work_dir_path", "work_dir")) / "tmp" / "vc_output"
        vc_output_dir.mkdir(parents=True, exist_ok=True)

        temp_audio_filename = f"vc_output_{uuid.uuid4()}.wav"
        temp_audio_filepath = vc_output_dir / temp_audio_filename

        try:
            # Save the raw bytes as a .wav file using torchaudio
            import torchaudio
            # Convert raw bytes back to tensor
            audio_tensor = torch.from_numpy(np.frombuffer(audio_bytes, dtype=np.float32))
            if audio_tensor.ndim == 1:
                audio_tensor = audio_tensor.unsqueeze(0) # Add channel dim if mono

            await asyncio.to_thread(torchaudio.save, str(temp_audio_filepath), audio_tensor, sr)
            print(f"ChatterboxTTSTool: Saved converted voice to {temp_audio_filepath}")

            relative_audio_path = f"tmp/vc_output/{temp_audio_filename}"

        except Exception as e:
            print(f"ChatterboxTTSTool: Error saving VC audio to file: {e}")
            relative_audio_path = None

        result_details = {
            "sample_rate": sr,
            "audio_path": relative_audio_path if relative_audio_path else "Error saving audio",
            "audio_data_base64_preview": audio_base64[:256] + "..." if audio_base64 else None,
            "source_audio_path": source_audio_path,
            "target_voice_path": target_voice_path,
            "audio_duration_seconds": len(audio_bytes) / (sr * np.dtype(np.float32).itemsize),
            "cfg_weight": cfg_weight,
            "temperature": temperature
        }

        await self._emit_tts_event("convert_voice", "completed", result_details)
        return ToolResponse(
            message="Voice conversion completed successfully." + (f" Saved to {relative_audio_path}" if relative_audio_path else ""),
            data=result_details,
            success=True
        )