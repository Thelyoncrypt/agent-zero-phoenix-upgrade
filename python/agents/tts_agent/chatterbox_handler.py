# python/agents/tts_agent/chatterbox_handler.py
import asyncio
from typing import Dict, Any, Optional, Tuple
import numpy as np
import torch
import librosa # For loading audio prompt if needed by Chatterbox internal
import tempfile
import os
from pathlib import Path

try:
    from chatterbox.tts import ChatterboxTTS as RealChatterboxTTS, punc_norm
    from chatterbox.vc import ChatterboxVC as RealChatterboxVC # Import VC model
    from chatterbox.models.s3gen import S3GEN_SR # Sample rate from chatterbox
    CHATTERBOX_AVAILABLE = True
except ImportError:
    print("ChatterboxTTSHandler/VCHandler: chatterbox-tts library not found. TTS/VC tools will not be functional.")
    CHATTERBOX_AVAILABLE = False
    # Placeholder for S3GEN_SR if library not found
    S3GEN_SR = 24000
    class RealChatterboxTTS: # Placeholder
        def __init__(self, *args, **kwargs): pass
        @classmethod
        def from_pretrained(cls, *args, **kwargs): return cls()
        def generate(self, *args, **kwargs):
            num_samples = int(S3GEN_SR * 2.0)
            return torch.zeros(1, num_samples, dtype=torch.float32) # Batch dim, samples
        @property
        def sr(self): return S3GEN_SR
    class RealChatterboxVC: # Placeholder
        def __init__(self, *args, **kwargs): self.sr = S3GEN_SR
        @classmethod
        def from_pretrained(cls, *args, **kwargs): return cls()
        def generate(self, *args, **kwargs):
            num_samples = int(S3GEN_SR * 2.0)
            return torch.zeros(1, num_samples, dtype=torch.float32)

class ChatterboxTTSHandler:
    """
    Handles Text-to-Speech generation using the real Chatterbox library.
    """
    _model_instance: Optional[RealChatterboxTTS] = None
    _model_lock = asyncio.Lock()

    def __init__(self, device: str = "cpu"):
        self.device = device
        self.sr = S3GEN_SR # Sample rate of Chatterbox output
        # Model loading is deferred to ensure it happens in the correct async context / process
        print(f"ChatterboxTTSHandler: Initialized for device: {device}. Model will be loaded on first use.")

    async def _ensure_model_loaded(self):
        async with self._model_lock:
            if not CHATTERBOX_AVAILABLE:
                raise RuntimeError("Chatterbox library is not installed. TTS functionality is unavailable.")
            if ChatterboxTTSHandler._model_instance is None:
                print(f"ChatterboxTTSHandler: Loading ChatterboxTTS model for device '{self.device}'...")
                try:
                    # from_pretrained might be synchronous, wrap if necessary
                    ChatterboxTTSHandler._model_instance = await asyncio.to_thread(
                        RealChatterboxTTS.from_pretrained, device=self.device
                    )
                    print("ChatterboxTTSHandler: Model loaded successfully.")
                except Exception as e:
                    print(f"ChatterboxTTSHandler: Failed to load ChatterboxTTS model: {e}")
                    import traceback
                    traceback.print_exc()
                    ChatterboxTTSHandler._model_instance = None # Ensure it's None on failure
                    raise # Re-raise exception to signal failure

            if ChatterboxTTSHandler._model_instance is None:
                 raise RuntimeError("ChatterboxTTS model could not be loaded.")
        return ChatterboxTTSHandler._model_instance

    async def generate_speech(self, text: str, audio_prompt_path: Optional[str] = None,
                              exaggeration: float = 0.5, cfg_weight: float = 0.5,
                              temperature: float = 0.8) -> Tuple[int, bytes]:
        """Generates speech using ChatterboxTTS model."""
        if not CHATTERBOX_AVAILABLE:
             raise RuntimeError("Chatterbox library is not installed. Cannot generate speech.")

        model = await self._ensure_model_loaded()

        print(f"ChatterboxTTSHandler: Generating speech for text: '{text[:50]}...' with prompt: {audio_prompt_path}")

        # Normalize punctuation as per Chatterbox example
        normalized_text = punc_norm(text)

        # Chatterbox's model.generate is synchronous
        # We need to run it in a thread pool executor to avoid blocking the asyncio loop
        try:
            wav_tensor_batched = await asyncio.to_thread(
                model.generate,
                text=normalized_text,
                audio_prompt_path=audio_prompt_path, # Path to a .wav file
                exaggeration=exaggeration,
                cfg_weight=cfg_weight,
                temperature=temperature
            ) # Returns torch.Tensor of shape (1, num_samples)
        except Exception as e:
            print(f"ChatterboxTTSHandler: Error during model.generate: {e}")
            import traceback
            traceback.print_exc()
            raise

        if wav_tensor_batched is None or wav_tensor_batched.numel() == 0:
            print("ChatterboxTTSHandler: Model generated empty audio.")
            raise ValueError("TTS model generated empty audio.")

        # Assuming batch size of 1 from model.generate output
        wav_tensor = wav_tensor_batched.squeeze(0).cpu() # (num_samples,)
        audio_numpy = wav_tensor.numpy()

        # Watermarking is handled internally by ChatterboxTTS.generate if it uses its own watermarker.
        # The example in chatterbox/tts.py shows:
        #   wav = model.generate(...)
        #   watermarked_wav = self.watermarker.apply_watermark(wav, sample_rate=self.sr)
        # So, the `model.generate` in ChatterboxTTS already returns watermarked audio.
        # If `model.generate` does NOT return watermarked audio, we'd do it here:
        # watermarker = perth.PerthImplicitWatermarker() # From chatterbox.tts
        # watermarked_audio_numpy = watermarker.apply_watermark(audio_numpy, sample_rate=self.sr)
        # audio_bytes = watermarked_audio_numpy.astype(np.float32).tobytes()

        audio_bytes = audio_numpy.astype(np.float32).tobytes() # Assuming generate() already watermarked

        print(f"ChatterboxTTSHandler: Speech generated ({len(audio_bytes)} bytes, SR: {self.sr}).")
        return self.sr, audio_bytes

class ChatterboxVCHandler:
    """
    Handles Voice Conversion using the real Chatterbox VC library.
    """
    _vc_model_instance: Optional[RealChatterboxVC] = None
    _vc_model_lock = asyncio.Lock()

    def __init__(self, device: str = "cpu"):
        self.device = device
        self.sr = S3GEN_SR # Sample rate of Chatterbox VC output
        print(f"ChatterboxVCHandler: Initialized for device: {device}. VC model will be loaded on first use.")

    async def _ensure_vc_model_loaded(self):
        async with self._vc_model_lock:
            if not CHATTERBOX_AVAILABLE:
                raise RuntimeError("Chatterbox library is not installed. VC functionality is unavailable.")
            if ChatterboxVCHandler._vc_model_instance is None:
                print(f"ChatterboxVCHandler: Loading ChatterboxVC model for device '{self.device}'...")
                try:
                    # from_pretrained might be synchronous, wrap if necessary
                    ChatterboxVCHandler._vc_model_instance = await asyncio.to_thread(
                        RealChatterboxVC.from_pretrained, device=self.device
                    )
                    print("ChatterboxVCHandler: VC model loaded successfully.")
                except Exception as e:
                    print(f"ChatterboxVCHandler: Failed to load ChatterboxVC model: {e}")
                    import traceback
                    traceback.print_exc()
                    ChatterboxVCHandler._vc_model_instance = None # Ensure it's None on failure
                    raise # Re-raise exception to signal failure

            if ChatterboxVCHandler._vc_model_instance is None:
                 raise RuntimeError("ChatterboxVC model could not be loaded.")
        return ChatterboxVCHandler._vc_model_instance

    async def convert_voice(self, source_audio_path: str, target_voice_path: str,
                           cfg_weight: float = 0.5, temperature: float = 0.8) -> Tuple[int, bytes]:
        """
        Converts the voice in source_audio_path to match the target voice characteristics.

        Args:
            source_audio_path: Path to the source audio file to convert
            target_voice_path: Path to the target voice reference audio file
            cfg_weight: Classifier-free guidance weight for VC
            temperature: Temperature for sampling during VC

        Returns:
            Tuple of (sample_rate, audio_bytes)
        """
        if not CHATTERBOX_AVAILABLE:
            raise RuntimeError("Chatterbox library is not installed. Cannot perform voice conversion.")

        # Validate input files exist
        if not os.path.exists(source_audio_path):
            raise FileNotFoundError(f"Source audio file not found: {source_audio_path}")
        if not os.path.exists(target_voice_path):
            raise FileNotFoundError(f"Target voice file not found: {target_voice_path}")

        vc_model = await self._ensure_vc_model_loaded()

        print(f"ChatterboxVCHandler: Converting voice from '{source_audio_path}' to target '{target_voice_path}'")

        try:
            # Load source audio using librosa (common preprocessing for VC models)
            source_audio, source_sr = await asyncio.to_thread(librosa.load, source_audio_path, sr=self.sr)

            # ChatterboxVC's model.generate is synchronous
            # We need to run it in a thread pool executor to avoid blocking the asyncio loop
            wav_tensor_batched = await asyncio.to_thread(
                vc_model.generate,
                source_audio=source_audio,  # numpy array or tensor
                target_voice_path=target_voice_path,  # Path to target voice reference
                cfg_weight=cfg_weight,
                temperature=temperature
            ) # Returns torch.Tensor of shape (1, num_samples)

        except Exception as e:
            print(f"ChatterboxVCHandler: Error during VC model.generate: {e}")
            import traceback
            traceback.print_exc()
            raise

        if wav_tensor_batched is None or wav_tensor_batched.numel() == 0:
            print("ChatterboxVCHandler: VC model generated empty audio.")
            raise ValueError("VC model generated empty audio.")

        # Assuming batch size of 1 from model.generate output
        wav_tensor = wav_tensor_batched.squeeze(0).cpu() # (num_samples,)
        audio_numpy = wav_tensor.numpy()

        # Convert to bytes for return
        audio_bytes = audio_numpy.astype(np.float32).tobytes()

        print(f"ChatterboxVCHandler: Voice conversion completed ({len(audio_bytes)} bytes, SR: {self.sr}).")
        return self.sr, audio_bytes