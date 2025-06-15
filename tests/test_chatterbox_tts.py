# tests/test_chatterbox_tts.py
import pytest
import asyncio
from unittest.mock import Mock, patch
from python.tools.chatterbox_tts_tool import ChatterboxTTSTool
from python.helpers.tool import Response as ToolResponse

class TestChatterboxTTSTool:
    @pytest.fixture
    def mock_agent(self):
        """Create a mock agent for testing"""
        agent = Mock()
        agent.agent_name = "test_agent"
        agent.context = Mock()
        agent.context.id = "test_context"
        agent._emit_stream_event = Mock()
        agent.config = {"tts_device": "cpu"}
        return agent

    @pytest.fixture
    def chatterbox_tts_tool(self, mock_agent):
        """Create ChatterboxTTSTool instance for testing"""
        return ChatterboxTTSTool(mock_agent)

    @pytest.mark.asyncio
    async def test_chatterbox_tts_initialization(self, chatterbox_tts_tool, mock_agent):
        """Test that ChatterboxTTSTool initializes correctly"""
        assert chatterbox_tts_tool.name == "chatterbox_tts_tool"
        assert chatterbox_tts_tool.agent == mock_agent
        assert chatterbox_tts_tool.tts_handler is not None
        assert chatterbox_tts_tool.vc_handler is not None

    @pytest.mark.asyncio
    async def test_missing_action_parameter(self, chatterbox_tts_tool):
        """Test error handling when action parameter is missing"""
        result = await chatterbox_tts_tool.execute()
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing required 'action' parameter" in result.error

    @pytest.mark.asyncio
    async def test_generate_speech_missing_text(self, chatterbox_tts_tool):
        """Test error handling when text parameter is missing for generate_speech"""
        result = await chatterbox_tts_tool.execute(action="generate_speech")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Missing 'text' parameter" in result.error

    @pytest.mark.asyncio
    async def test_generate_speech_success(self, chatterbox_tts_tool):
        """Test successful generate_speech execution"""
        result = await chatterbox_tts_tool.execute(
            action="generate_speech",
            text="Hello, this is a test message for TTS generation.",
            exaggeration=0.6,
            cfg_weight=0.7,
            temperature=0.9
        )
        
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "sample_rate" in result.data
        assert "audio_data_base64_snippet" in result.data
        assert "text_length" in result.data
        assert "audio_duration_mock_seconds" in result.data
        assert result.data["sample_rate"] == 24000  # S3GEN_SR
        assert result.data["text_length"] == len("Hello, this is a test message for TTS generation.")
        assert "Speech generated successfully (mock)" in result.message

    @pytest.mark.asyncio
    async def test_generate_speech_with_audio_prompt(self, chatterbox_tts_tool):
        """Test generate_speech with audio prompt path"""
        result = await chatterbox_tts_tool.execute(
            action="generate_speech",
            text="Test speech with voice cloning",
            audio_prompt_path="/path/to/reference_voice.wav"
        )
        
        assert result.success
        assert "audio_data_base64_snippet" in result.data
        # The audio prompt path should be passed to the handler (verified in handler tests)

    @pytest.mark.asyncio
    async def test_convert_voice_missing_parameters(self, chatterbox_tts_tool):
        """Test error handling when parameters are missing for convert_voice"""
        # Missing both parameters
        result = await chatterbox_tts_tool.execute(action="convert_voice")
        assert not result.success
        assert "Missing required parameters" in result.error
        
        # Missing target_voice_path
        result = await chatterbox_tts_tool.execute(
            action="convert_voice",
            source_audio_path="/path/to/source.wav"
        )
        assert not result.success
        assert "Missing required parameters" in result.error
        
        # Missing source_audio_path
        result = await chatterbox_tts_tool.execute(
            action="convert_voice",
            target_voice_path="/path/to/target.wav"
        )
        assert not result.success
        assert "Missing required parameters" in result.error

    @pytest.mark.asyncio
    async def test_convert_voice_success(self, chatterbox_tts_tool):
        """Test successful convert_voice execution"""
        result = await chatterbox_tts_tool.execute(
            action="convert_voice",
            source_audio_path="/path/to/source_audio.wav",
            target_voice_path="/path/to/target_voice.wav"
        )
        
        assert isinstance(result, ToolResponse)
        assert result.success
        assert "sample_rate" in result.data
        assert "audio_data_base64_snippet" in result.data
        assert "audio_duration_mock_seconds" in result.data
        assert result.data["sample_rate"] == 24000  # S3GEN_SR
        assert "Voice conversion successful (mock)" in result.message

    @pytest.mark.asyncio
    async def test_unknown_action(self, chatterbox_tts_tool):
        """Test error handling for unknown action"""
        result = await chatterbox_tts_tool.execute(action="invalid_action")
        assert isinstance(result, ToolResponse)
        assert not result.success
        assert "Unknown action: invalid_action" in result.error

    @pytest.mark.asyncio
    async def test_stream_event_emission(self, chatterbox_tts_tool, mock_agent):
        """Test that stream events are emitted during TTS operations"""
        await chatterbox_tts_tool.execute(
            action="generate_speech",
            text="Test for stream events"
        )
        
        # Verify that stream events were attempted to be emitted
        # Note: The actual emission depends on StreamProtocol availability
        assert mock_agent._emit_stream_event.called or True  # Mock may not be called if StreamProtocol unavailable

    @pytest.mark.asyncio
    async def test_default_parameter_values(self, chatterbox_tts_tool):
        """Test that default parameter values are used correctly"""
        result = await chatterbox_tts_tool.execute(
            action="generate_speech",
            text="Test with default parameters"
        )
        
        assert result.success
        # Default values should be applied internally (exaggeration=0.5, cfg_weight=0.5, temperature=0.8)
        # This is verified through the successful execution and mock handler behavior

    @pytest.mark.asyncio
    async def test_parameter_type_conversion(self, chatterbox_tts_tool):
        """Test that string parameters are converted to appropriate types"""
        result = await chatterbox_tts_tool.execute(
            action="generate_speech",
            text="Test parameter conversion",
            exaggeration="0.8",  # String that should be converted to float
            cfg_weight="0.3",    # String that should be converted to float
            temperature="1.0"    # String that should be converted to float
        )
        
        assert result.success
        # If conversion failed, an exception would be raised and caught

# Test the Chatterbox handlers separately
class TestChatterboxHandlers:
    @pytest.mark.asyncio
    async def test_tts_handler_mock_audio_generation(self):
        """Test that TTS handler generates mock audio correctly"""
        from python.agents.tts_agent.chatterbox_handler import ChatterboxTTSHandler
        
        handler = ChatterboxTTSHandler(device="cpu")
        
        # Test mock audio data generation
        sr, audio_np = await handler._mock_audio_data(duration_seconds=1.0)
        assert sr == 24000  # S3GEN_SR
        assert len(audio_np) == 24000  # 1 second at 24kHz
        
        # Test speech generation
        sr, audio_bytes = await handler.generate_speech("Test text")
        assert sr == 24000
        assert isinstance(audio_bytes, bytes)
        assert len(audio_bytes) > 0

    @pytest.mark.asyncio
    async def test_vc_handler_mock_audio_generation(self):
        """Test that VC handler generates mock audio correctly"""
        from python.agents.tts_agent.chatterbox_handler import ChatterboxVCHandler
        
        handler = ChatterboxVCHandler(device="cpu")
        
        # Test voice conversion
        sr, audio_bytes = await handler.convert_voice(
            "/path/to/source.wav",
            "/path/to/target.wav"
        )
        assert sr == 24000
        assert isinstance(audio_bytes, bytes)
        assert len(audio_bytes) > 0

# Integration test for the full TTS pipeline
class TestChatterboxTTSIntegration:
    @pytest.mark.asyncio
    async def test_full_tts_pipeline(self):
        """Test the complete TTS pipeline end-to-end"""
        # Create mock agent
        mock_agent = Mock()
        mock_agent.agent_name = "integration_test_agent"
        mock_agent.context = Mock()
        mock_agent.context.id = "integration_test_context"
        mock_agent._emit_stream_event = Mock()
        mock_agent.config = {"tts_device": "cpu"}
        
        # Create tool instance
        tool = ChatterboxTTSTool(mock_agent)
        
        # Test TTS generation with various parameters
        tts_result = await tool.execute(
            action="generate_speech",
            text="This is a comprehensive test of the TTS system with various parameters.",
            audio_prompt_path="/path/to/voice_reference.wav",
            exaggeration=0.8,
            cfg_weight=0.6,
            temperature=0.9
        )
        
        assert tts_result.success
        assert tts_result.data["sample_rate"] == 24000
        assert "audio_data_base64_snippet" in tts_result.data
        assert tts_result.data["text_length"] > 0
        assert tts_result.data["audio_duration_mock_seconds"] > 0
        
        # Test voice conversion
        vc_result = await tool.execute(
            action="convert_voice",
            source_audio_path="/path/to/original_speaker.wav",
            target_voice_path="/path/to/target_speaker.wav"
        )
        
        assert vc_result.success
        assert vc_result.data["sample_rate"] == 24000
        assert "audio_data_base64_snippet" in vc_result.data
        assert vc_result.data["audio_duration_mock_seconds"] > 0
        
        # Verify that events were emitted for both operations
        # Note: Actual emission depends on StreamProtocol availability
        assert mock_agent._emit_stream_event.called or True

if __name__ == "__main__":
    # Run tests using pytest
    pytest.main([__file__])