# python/tools/chatterbox_tts_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any, Optional
import base64

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
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent,
            name="chatterbox_tts_tool",
            description="Generates speech from text (TTS) or performs voice conversion (VC) using Chatterbox models.",
            args_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["generate_speech", "convert_voice"],
                        "description": "Type of TTS operation to perform"
                    },
                    "text": {
                        "type": "string",
                        "description": "Text to synthesize (for generate_speech action)"
                    },
                    "audio_prompt_path": {
                        "type": "string",
                        "description": "Path to .wav file for voice cloning (optional)"
                    },
                    "exaggeration": {
                        "type": "number",
                        "description": "Controls emotion/intensity (default: 0.5)"
                    },
                    "cfg_weight": {
                        "type": "number",
                        "description": "Controls pacing/adherence to prompt (default: 0.5)"
                    },
                    "temperature": {
                        "type": "number",
                        "description": "Sampling temperature (default: 0.8)"
                    },
                    "source_audio_path": {
                        "type": "string",
                        "description": "Path to source .wav file (for convert_voice action)"
                    },
                    "target_voice_path": {
                        "type": "string",
                        "description": "Path to target voice .wav file (for convert_voice action)"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        # In a real setup, device would come from agent config
        device = getattr(agent, 'config', {}).get("tts_device", "cpu")
        self.tts_handler = ChatterboxTTSHandler(device=device)
        self.vc_handler = ChatterboxVCHandler(device=device)
        print(f"ChatterboxTTSTool initialized for agent {agent.agent_name} on device {device}")

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
            return ToolResponse(
                success=False,
                error="Missing required 'action' parameter",
                message="Error: 'action' is required for ChatterboxTTS operations."
            )

        try:
            if action == "generate_speech":
                text = kwargs.get("text")
                if not text:
                    return ToolResponse(
                        success=False,
                        error="Missing 'text' parameter",
                        message="Error: 'text' is required for generate_speech action."
                    )
                
                audio_prompt_path = kwargs.get("audio_prompt_path") # Path to a .wav file
                exaggeration = float(kwargs.get("exaggeration", 0.5))
                cfg_weight = float(kwargs.get("cfg_weight", 0.5))
                temperature = float(kwargs.get("temperature", 0.8))
                
                return await self._generate_speech(text, audio_prompt_path, exaggeration, cfg_weight, temperature)
            
            elif action == "convert_voice":
                source_audio_path = kwargs.get("source_audio_path")
                target_voice_path = kwargs.get("target_voice_path")
                if not source_audio_path or not target_voice_path:
                    return ToolResponse(
                        success=False,
                        error="Missing required parameters",
                        message="Error: 'source_audio_path' and 'target_voice_path' are required for convert_voice action."
                    )
                return await self._convert_voice(source_audio_path, target_voice_path)
            
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown ChatterboxTTSTool action: {action}"
                )

        except Exception as e:
            import traceback
            error_message = f"ChatterboxTTSTool error during action '{action}': {str(e)}"
            print(f"{error_message}\\n{traceback.format_exc()}")
            await self._emit_tts_event(action, "error", {"error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _generate_speech(self, text: str, audio_prompt_path: Optional[str], 
                               exaggeration: float, cfg_weight: float, temperature: float) -> ToolResponse:
        await self._emit_tts_event("generate_speech", "starting", {"text_length": len(text), "prompt": bool(audio_prompt_path)})
        
        sr, audio_bytes = await self.tts_handler.generate_speech(
            text, audio_prompt_path, exaggeration, cfg_weight, temperature
        )
        
        # Encode audio data for JSON transport (e.g., base64) or store and return a reference.
        # For this placeholder, let's return a small snippet of base64.
        audio_base64 = base64.b64encode(audio_bytes[:1024]).decode('utf-8') # Snippet for response
        # In a real scenario, you might save the file and return a path/URL, 
        # or stream bytes via a different AG-UI event type if supported.

        result_details = {
            "sample_rate": sr, 
            "audio_data_base64_snippet": audio_base64, # Or "audio_url": "path/to/file.wav"
            "text_length": len(text),
            "audio_duration_mock_seconds": len(audio_bytes) / (sr * 2) # Assuming 16-bit mono for mock
        }
        await self._emit_tts_event("generate_speech", "completed", result_details)
        return ToolResponse(
            success=True,
            data=result_details,
            message="Speech generated successfully (mock)."
        )

    async def _convert_voice(self, source_audio_path: str, target_voice_path: str) -> ToolResponse:
        await self._emit_tts_event("convert_voice", "starting", {"source": source_audio_path, "target_prompt": target_voice_path})
        
        sr, audio_bytes = await self.vc_handler.convert_voice(source_audio_path, target_voice_path)
        
        audio_base64 = base64.b64encode(audio_bytes[:1024]).decode('utf-8')
        result_details = {
            "sample_rate": sr, 
            "audio_data_base64_snippet": audio_base64,
            "audio_duration_mock_seconds": len(audio_bytes) / (sr * 2)
        }
        await self._emit_tts_event("convert_voice", "completed", result_details)
        return ToolResponse(
            success=True,
            data=result_details,
            message="Voice conversion successful (mock)."
        )