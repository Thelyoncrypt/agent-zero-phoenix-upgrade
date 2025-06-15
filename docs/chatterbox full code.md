├── .gitignore
├── LICENSE
├── README.md
├── example_for_mac.py
├── example_tts.py
├── example_vc.py
├── gradio_tts_app.py
├── gradio_vc_app.py
├── pyproject.toml
└── src
    └── chatterbox
        ├── __init__.py
        ├── models
            ├── __init__.py
            ├── s3gen
            │   ├── __init__.py
            │   ├── configs.py
            │   ├── const.py
            │   ├── decoder.py
            │   ├── f0_predictor.py
            │   ├── flow.py
            │   ├── flow_matching.py
            │   ├── hifigan.py
            │   ├── matcha
            │   │   ├── decoder.py
            │   │   ├── flow_matching.py
            │   │   ├── text_encoder.py
            │   │   └── transformer.py
            │   ├── s3gen.py
            │   ├── transformer
            │   │   ├── __init__.py
            │   │   ├── activation.py
            │   │   ├── attention.py
            │   │   ├── convolution.py
            │   │   ├── embedding.py
            │   │   ├── encoder_layer.py
            │   │   ├── positionwise_feed_forward.py
            │   │   ├── subsampling.py
            │   │   └── upsample_encoder.py
            │   ├── utils
            │   │   ├── class_utils.py
            │   │   ├── mask.py
            │   │   └── mel.py
            │   └── xvector.py
            ├── s3tokenizer
            │   ├── __init__.py
            │   └── s3tokenizer.py
            ├── t3
            │   ├── __init__.py
            │   ├── inference
            │   │   ├── alignment_stream_analyzer.py
            │   │   └── t3_hf_backend.py
            │   ├── llama_configs.py
            │   ├── modules
            │   │   ├── cond_enc.py
            │   │   ├── learned_pos_emb.py
            │   │   ├── perceiver.py
            │   │   └── t3_config.py
            │   └── t3.py
            ├── tokenizers
            │   ├── __init__.py
            │   └── tokenizer.py
            ├── utils.py
            └── voice_encoder
            │   ├── __init__.py
            │   ├── config.py
            │   ├── melspec.py
            │   └── voice_encoder.py
        ├── tts.py
        └── vc.py


/.gitignore:
--------------------------------------------------------------------------------
 1 | .vscode
 2 | 
 3 | # Pylance
 4 | pyrightconfig.json
 5 | 
 6 | # Byte-compiled / optimized / DLL files
 7 | __pycache__/
 8 | *.py[cod]
 9 | *$py.class
10 | 
11 | # C extensions
12 | *.so
13 | 
14 | # Distribution / packaging
15 | .Python
16 | build/
17 | develop-eggs/
18 | dist/
19 | downloads/
20 | eggs/
21 | .eggs/
22 | lib/
23 | lib64/
24 | parts/
25 | sdist/
26 | var/
27 | wheels/
28 | *.egg-info/
29 | .installed.cfg
30 | *.egg
31 | MANIFEST
32 | 
33 | # PyInstaller
34 | #  Usually these files are written by a python script from a template
35 | #  before PyInstaller builds the exe, so as to inject date/other infos into it.
36 | *.manifest
37 | *.spec
38 | 
39 | # Installer logs
40 | pip-log.txt
41 | pip-delete-this-directory.txt
42 | 
43 | syn_out/
44 | checkpoints/
45 | .gradio
46 | 
47 | # Ignore generated sample .wav files
48 | **/*.wav
49 | 


--------------------------------------------------------------------------------
/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2025 Resemble AI
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
  1 | 
  2 | <img width="1200" alt="cb-big2" src="https://github.com/user-attachments/assets/bd8c5f03-e91d-4ee5-b680-57355da204d1" />
  3 | 
  4 | # Chatterbox TTS
  5 | 
  6 | [![Alt Text](https://img.shields.io/badge/listen-demo_samples-blue)](https://resemble-ai.github.io/chatterbox_demopage/)
  7 | [![Alt Text](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/ResembleAI/Chatterbox)
  8 | [![Alt Text](https://static-public.podonos.com/badges/insight-on-pdns-sm-dark.svg)](https://podonos.com/resembleai/chatterbox)
  9 | [![Discord](https://img.shields.io/discord/1377773249798344776?label=join%20discord&logo=discord&style=flat)](https://discord.gg/rJq9cRJBJ6)
 10 | 
 11 | _Made with ♥️ by <a href="https://resemble.ai" target="_blank"><img width="100" alt="resemble-logo-horizontal" src="https://github.com/user-attachments/assets/35cf756b-3506-4943-9c72-c05ddfa4e525" /></a>
 12 | 
 13 | We're excited to introduce Chatterbox, [Resemble AI's](https://resemble.ai) first production-grade open source TTS model. Licensed under MIT, Chatterbox has been benchmarked against leading closed-source systems like ElevenLabs, and is consistently preferred in side-by-side evaluations.
 14 | 
 15 | Whether you're working on memes, videos, games, or AI agents, Chatterbox brings your content to life. It's also the first open source TTS model to support **emotion exaggeration control**, a powerful feature that makes your voices stand out. Try it now on our [Hugging Face Gradio app.](https://huggingface.co/spaces/ResembleAI/Chatterbox)
 16 | 
 17 | If you like the model but need to scale or tune it for higher accuracy, check out our competitively priced TTS service (<a href="https://resemble.ai">link</a>). It delivers reliable performance with ultra-low latency of sub 200ms—ideal for production use in agents, applications, or interactive media.
 18 | 
 19 | # Key Details
 20 | - SoTA zeroshot TTS
 21 | - 0.5B Llama backbone
 22 | - Unique exaggeration/intensity control
 23 | - Ultra-stable with alignment-informed inference
 24 | - Trained on 0.5M hours of cleaned data
 25 | - Watermarked outputs
 26 | - Easy voice conversion script
 27 | - [Outperforms ElevenLabs](https://podonos.com/resembleai/chatterbox)
 28 | 
 29 | # Tips
 30 | - **General Use (TTS and Voice Agents):**
 31 |   - The default settings (`exaggeration=0.5`, `cfg_weight=0.5`) work well for most prompts.
 32 |   - If the reference speaker has a fast speaking style, lowering `cfg_weight` to around `0.3` can improve pacing.
 33 | 
 34 | - **Expressive or Dramatic Speech:**
 35 |   - Try lower `cfg_weight` values (e.g. `~0.3`) and increase `exaggeration` to around `0.7` or higher.
 36 |   - Higher `exaggeration` tends to speed up speech; reducing `cfg_weight` helps compensate with slower, more deliberate pacing.
 37 | 
 38 | 
 39 | # Installation
 40 | ```shell
41 | pip install chatterbox-tts
 42 |
```
 43 | 
 44 | Alternatively, you can install from source:
 45 | ```shell
46 | # conda create -yn chatterbox python=3.11
 47 | # conda activate chatterbox
 48 | 
 49 | git clone https://github.com/resemble-ai/chatterbox.git
 50 | cd chatterbox
 51 | pip install -e .
 52 |
```
 53 | We developed and tested Chatterbox on Python 3.11 on Debain 11 OS; the versions of the dependencies are pinned in `pyproject.toml` to ensure consistency. You can modify the code or dependencies in this installation mode.
 54 | 
 55 | 
 56 | # Usage
 57 | ```python
58 | import torchaudio as ta
 59 | from chatterbox.tts import ChatterboxTTS
 60 | 
 61 | model = ChatterboxTTS.from_pretrained(device="cuda")
 62 | 
 63 | text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
 64 | wav = model.generate(text)
 65 | ta.save("test-1.wav", wav, model.sr)
 66 | 
 67 | # If you want to synthesize with a different voice, specify the audio prompt
 68 | AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
 69 | wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
 70 | ta.save("test-2.wav", wav, model.sr)
 71 |
```
 72 | See `example_tts.py` and `example_vc.py` for more examples.
 73 | 
 74 | # Supported Lanugage
 75 | Currenlty only English.
 76 | 
 77 | # Acknowledgements
 78 | - [Cosyvoice](https://github.com/FunAudioLLM/CosyVoice)
 79 | - [Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)
 80 | - [HiFT-GAN](https://github.com/yl4579/HiFTNet)
 81 | - [Llama 3](https://github.com/meta-llama/llama3)
 82 | - [S3Tokenizer](https://github.com/xingchensong/S3Tokenizer)
 83 | 
 84 | # Built-in PerTh Watermarking for Responsible AI
 85 | 
 86 | Every audio file generated by Chatterbox includes [Resemble AI's Perth (Perceptual Threshold) Watermarker](https://github.com/resemble-ai/perth) - imperceptible neural watermarks that survive MP3 compression, audio editing, and common manipulations while maintaining nearly 100% detection accuracy.
 87 | 
 88 | 
 89 | ## Watermark extraction
 90 | 
 91 | You can look for the watermark using the following script.
 92 | 
 93 | ```python
94 | import perth
 95 | import librosa
 96 | 
 97 | AUDIO_PATH = "YOUR_FILE.wav"
 98 | 
 99 | # Load the watermarked audio
100 | watermarked_audio, sr = librosa.load(AUDIO_PATH, sr=None)
101 | 
102 | # Initialize watermarker (same as used for embedding)
103 | watermarker = perth.PerthImplicitWatermarker()
104 | 
105 | # Extract watermark
106 | watermark = watermarker.get_watermark(watermarked_audio, sample_rate=sr)
107 | print(f"Extracted watermark: {watermark}")
108 | # Output: 0.0 (no watermark) or 1.0 (watermarked)
109 |
```
110 | 
111 | 
112 | # Official Discord
113 | 
114 | 👋 Join us on [Discord](https://discord.gg/rJq9cRJBJ6) and let's build something awesome together!
115 | 
116 | # Disclaimer
117 | Don't use this model to do bad things. Prompts are sourced from freely available data on the internet.
118 | 


--------------------------------------------------------------------------------
/example_for_mac.py:
--------------------------------------------------------------------------------
 1 | import torch
 2 | import torchaudio as ta
 3 | from chatterbox.tts import ChatterboxTTS
 4 | 
 5 | # Detect device (Mac with M1/M2/M3/M4)
 6 | device = "mps" if torch.backends.mps.is_available() else "cpu"
 7 | map_location = torch.device(device)
 8 | 
 9 | torch_load_original = torch.load
10 | def patched_torch_load(*args, **kwargs):
11 |     if 'map_location' not in kwargs:
12 |         kwargs['map_location'] = map_location
13 |     return torch_load_original(*args, **kwargs)
14 | 
15 | torch.load = patched_torch_load
16 | 
17 | model = ChatterboxTTS.from_pretrained(device=device)
18 | text = "Today is the day. I want to move like a titan at dawn, sweat like a god forging lightning. No more excuses. From now on, my mornings will be temples of discipline. I am going to work out like the gods… every damn day."
19 | 
20 | # If you want to synthesize with a different voice, specify the audio prompt
21 | AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
22 | wav = model.generate(
23 |     text, 
24 |     audio_prompt_path=AUDIO_PROMPT_PATH,
25 |     exaggeration=2.0,
26 |     cfg_weight=0.5
27 |     )
28 | ta.save("test-2.wav", wav, model.sr)
29 | 


--------------------------------------------------------------------------------
/example_tts.py:
--------------------------------------------------------------------------------
 1 | import torchaudio as ta
 2 | import torch
 3 | from chatterbox.tts import ChatterboxTTS
 4 | 
 5 | # Automatically detect the best available device
 6 | if torch.cuda.is_available():
 7 |     device = "cuda"
 8 | elif torch.backends.mps.is_available():
 9 |     device = "mps"
10 | else:
11 |     device = "cpu"
12 | 
13 | print(f"Using device: {device}")
14 | 
15 | model = ChatterboxTTS.from_pretrained(device=device)
16 | 
17 | text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
18 | wav = model.generate(text)
19 | ta.save("test-1.wav", wav, model.sr)
20 | 
21 | # If you want to synthesize with a different voice, specify the audio prompt
22 | AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
23 | wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
24 | ta.save("test-2.wav", wav, model.sr)
25 | 


--------------------------------------------------------------------------------
/example_vc.py:
--------------------------------------------------------------------------------
 1 | import torch
 2 | import torchaudio as ta
 3 | 
 4 | from chatterbox.vc import ChatterboxVC
 5 | 
 6 | # Automatically detect the best available device
 7 | if torch.cuda.is_available():
 8 |     device = "cuda"
 9 | elif torch.backends.mps.is_available():
10 |     device = "mps"
11 | else:
12 |     device = "cpu"
13 | 
14 | print(f"Using device: {device}")
15 | 
16 | AUDIO_PATH = "YOUR_FILE.wav"
17 | TARGET_VOICE_PATH = "YOUR_FILE.wav"
18 | 
19 | model = ChatterboxVC.from_pretrained(device)
20 | wav = model.generate(
21 |     audio=AUDIO_PATH,
22 |     target_voice_path=TARGET_VOICE_PATH,
23 | )
24 | ta.save("testvc.wav", wav, model.sr)
25 | 


--------------------------------------------------------------------------------
/gradio_tts_app.py:
--------------------------------------------------------------------------------
 1 | import random
 2 | import numpy as np
 3 | import torch
 4 | import gradio as gr
 5 | from chatterbox.tts import ChatterboxTTS
 6 | 
 7 | 
 8 | DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
 9 | 
10 | 
11 | def set_seed(seed: int):
12 |     torch.manual_seed(seed)
13 |     torch.cuda.manual_seed(seed)
14 |     torch.cuda.manual_seed_all(seed)
15 |     random.seed(seed)
16 |     np.random.seed(seed)
17 | 
18 | 
19 | def load_model():
20 |     model = ChatterboxTTS.from_pretrained(DEVICE)
21 |     return model
22 | 
23 | 
24 | def generate(model, text, audio_prompt_path, exaggeration, temperature, seed_num, cfgw, min_p, top_p, repetition_penalty):
25 |     if model is None:
26 |         model = ChatterboxTTS.from_pretrained(DEVICE)
27 | 
28 |     if seed_num != 0:
29 |         set_seed(int(seed_num))
30 | 
31 |     wav = model.generate(
32 |         text,
33 |         audio_prompt_path=audio_prompt_path,
34 |         exaggeration=exaggeration,
35 |         temperature=temperature,
36 |         cfg_weight=cfgw,
37 |         min_p=min_p,
38 |         top_p=top_p,
39 |         repetition_penalty=repetition_penalty,
40 |     )
41 |     return (model.sr, wav.squeeze(0).numpy())
42 | 
43 | 
44 | with gr.Blocks() as demo:
45 |     model_state = gr.State(None)  # Loaded once per session/user
46 | 
47 |     with gr.Row():
48 |         with gr.Column():
49 |             text = gr.Textbox(
50 |                 value="Now let's make my mum's favourite. So three mars bars into the pan. Then we add the tuna and just stir for a bit, just let the chocolate and fish infuse. A sprinkle of olive oil and some tomato ketchup. Now smell that. Oh boy this is going to be incredible.",
51 |                 label="Text to synthesize (max chars 300)",
52 |                 max_lines=5
53 |             )
54 |             ref_wav = gr.Audio(sources=["upload", "microphone"], type="filepath", label="Reference Audio File", value=None)
55 |             exaggeration = gr.Slider(0.25, 2, step=.05, label="Exaggeration (Neutral = 0.5, extreme values can be unstable)", value=.5)
56 |             cfg_weight = gr.Slider(0.0, 1, step=.05, label="CFG/Pace", value=0.5)
57 | 
58 |             with gr.Accordion("More options", open=False):
59 |                 seed_num = gr.Number(value=0, label="Random seed (0 for random)")
60 |                 temp = gr.Slider(0.05, 5, step=.05, label="temperature", value=.8)
61 |                 min_p = gr.Slider(0.00, 1.00, step=0.01, label="min_p || Newer Sampler. Recommend 0.02 > 0.1. Handles Higher Temperatures better. 0.00 Disables", value=0.05)
62 |                 top_p = gr.Slider(0.00, 1.00, step=0.01, label="top_p || Original Sampler. 1.0 Disables(recommended). Original 0.8", value=1.00)
63 |                 repetition_penalty = gr.Slider(1.00, 2.00, step=0.1, label="repetition_penalty", value=1.2)
64 | 
65 |             run_btn = gr.Button("Generate", variant="primary")
66 | 
67 |         with gr.Column():
68 |             audio_output = gr.Audio(label="Output Audio")
69 | 
70 |     demo.load(fn=load_model, inputs=[], outputs=model_state)
71 | 
72 |     run_btn.click(
73 |         fn=generate,
74 |         inputs=[
75 |             model_state,
76 |             text,
77 |             ref_wav,
78 |             exaggeration,
79 |             temp,
80 |             seed_num,
81 |             cfg_weight,
82 |             min_p,
83 |             top_p,
84 |             repetition_penalty,
85 |         ],
86 |         outputs=audio_output,
87 |     )
88 | 
89 | if __name__ == "__main__":
90 |     demo.queue(
91 |         max_size=50,
92 |         default_concurrency_limit=1,
93 |     ).launch(share=True)
94 | 


--------------------------------------------------------------------------------
/gradio_vc_app.py:
--------------------------------------------------------------------------------
 1 | import torch
 2 | import gradio as gr
 3 | from chatterbox.vc import ChatterboxVC
 4 | 
 5 | 
 6 | DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
 7 | 
 8 | 
 9 | model = ChatterboxVC.from_pretrained(DEVICE)
10 | def generate(audio, target_voice_path):
11 |     wav = model.generate(
12 |         audio, target_voice_path=target_voice_path,
13 |     )
14 |     return model.sr, wav.squeeze(0).numpy()
15 | 
16 | 
17 | demo = gr.Interface(
18 |     generate,
19 |     [
20 |         gr.Audio(sources=["upload", "microphone"], type="filepath", label="Input audio file"),
21 |         gr.Audio(sources=["upload", "microphone"], type="filepath", label="Target voice audio file (if none, the default voice is used)", value=None),
22 |     ],
23 |     "audio",
24 | )
25 | 
26 | if __name__ == "__main__":
27 |     demo.launch()
28 | 


--------------------------------------------------------------------------------
/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [project]
 2 | name = "chatterbox-tts"
 3 | version = "0.1.2"
 4 | description = "Chatterbox: Open Source TTS and Voice Conversion by Resemble AI"
 5 | readme = "README.md"
 6 | requires-python = ">=3.9"
 7 | license = {file = "LICENSE"}
 8 | authors = [
 9 |     {name = "resemble-ai", email = "engineering@resemble.ai"}
10 | ]
11 | dependencies = [
12 |     "numpy>=1.26.0",
13 |     "librosa==0.11.0",
14 |     "s3tokenizer",
15 |     "torch==2.6.0",
16 |     "torchaudio==2.6.0",
17 |     "transformers==4.46.3",
18 |     "diffusers==0.29.0",
19 |     "resemble-perth==1.0.1",
20 |     "conformer==0.3.2",
21 |     "safetensors==0.5.3"
22 | ]
23 | 
24 | [project.urls]
25 | Homepage = "https://github.com/resemble-ai/chatterbox"
26 | Repository = "https://github.com/resemble-ai/chatterbox"
27 | 
28 | [build-system]
29 | requires = ["setuptools>=61.0"]
30 | build-backend = "setuptools.build_meta"
31 | 
32 | [tool.setuptools.packages.find]
33 | where = ["src"]
34 | 


--------------------------------------------------------------------------------
/src/chatterbox/__init__.py:
--------------------------------------------------------------------------------
 1 | try:
 2 |     from importlib.metadata import version
 3 | except ImportError:
 4 |     from importlib_metadata import version  # For Python <3.8
 5 | 
 6 | __version__ = version("chatterbox-tts")
 7 | 
 8 | 
 9 | from .tts import ChatterboxTTS
10 | from .vc import ChatterboxVC
11 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/resemble-ai/chatterbox/eb90621fa748f341a5b768aed0c0c12fc561894b/src/chatterbox/models/__init__.py


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/__init__.py:
--------------------------------------------------------------------------------
1 | from .s3gen import S3Token2Wav as S3Gen
2 | from .const import S3GEN_SR
3 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/configs.py:
--------------------------------------------------------------------------------
 1 | from ..utils import AttrDict
 2 | 
 3 | CFM_PARAMS = AttrDict({
 4 |     "sigma_min": 1e-06,
 5 |     "solver": "euler",
 6 |     "t_scheduler": "cosine",
 7 |     "training_cfg_rate": 0.2,
 8 |     "inference_cfg_rate": 0.7,
 9 |     "reg_loss_type": "l1"
10 | })
11 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/const.py:
--------------------------------------------------------------------------------
1 | S3GEN_SR = 24000
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/decoder.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Zhihao Du)
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | import torch
 15 | import torch.nn as nn
 16 | import torch.nn.functional as F
 17 | from einops import pack, rearrange, repeat
 18 | 
 19 | from .utils.mask import add_optional_chunk_mask
 20 | from .matcha.decoder import SinusoidalPosEmb, Block1D, ResnetBlock1D, Downsample1D, \
 21 |     TimestepEmbedding, Upsample1D
 22 | from .matcha.transformer import BasicTransformerBlock
 23 | 
 24 | 
 25 | def mask_to_bias(mask: torch.Tensor, dtype: torch.dtype) -> torch.Tensor:
 26 |     assert mask.dtype == torch.bool
 27 |     assert dtype in [torch.float32, torch.bfloat16, torch.float16]
 28 |     mask = mask.to(dtype)
 29 |     # attention mask bias
 30 |     # NOTE(Mddct): torch.finfo jit issues
 31 |     #     chunk_masks = (1.0 - chunk_masks) * torch.finfo(dtype).min
 32 |     mask = (1.0 - mask) * -1.0e+10
 33 |     return mask
 34 | 
 35 | 
 36 | 
 37 | class Transpose(torch.nn.Module):
 38 |     def __init__(self, dim0: int, dim1: int):
 39 |         super().__init__()
 40 |         self.dim0 = dim0
 41 |         self.dim1 = dim1
 42 | 
 43 |     def forward(self, x: torch.Tensor):
 44 |         x = torch.transpose(x, self.dim0, self.dim1)
 45 |         return x
 46 | 
 47 | 
 48 | class CausalBlock1D(Block1D):
 49 |     def __init__(self, dim: int, dim_out: int):
 50 |         super(CausalBlock1D, self).__init__(dim, dim_out)
 51 |         self.block = torch.nn.Sequential(
 52 |             CausalConv1d(dim, dim_out, 3),
 53 |             Transpose(1, 2),
 54 |             nn.LayerNorm(dim_out),
 55 |             Transpose(1, 2),
 56 |             nn.Mish(),
 57 |         )
 58 | 
 59 |     def forward(self, x: torch.Tensor, mask: torch.Tensor):
 60 |         output = self.block(x * mask)
 61 |         return output * mask
 62 | 
 63 | 
 64 | class CausalResnetBlock1D(ResnetBlock1D):
 65 |     def __init__(self, dim: int, dim_out: int, time_emb_dim: int, groups: int = 8):
 66 |         super(CausalResnetBlock1D, self).__init__(dim, dim_out, time_emb_dim, groups)
 67 |         self.block1 = CausalBlock1D(dim, dim_out)
 68 |         self.block2 = CausalBlock1D(dim_out, dim_out)
 69 | 
 70 | 
 71 | class CausalConv1d(torch.nn.Conv1d):
 72 |     def __init__(
 73 |         self,
 74 |         in_channels: int,
 75 |         out_channels: int,
 76 |         kernel_size: int,
 77 |         stride: int = 1,
 78 |         dilation: int = 1,
 79 |         groups: int = 1,
 80 |         bias: bool = True,
 81 |         padding_mode: str = 'zeros',
 82 |         device=None,
 83 |         dtype=None
 84 |     ) -> None:
 85 |         super(CausalConv1d, self).__init__(in_channels, out_channels,
 86 |                                            kernel_size, stride,
 87 |                                            padding=0, dilation=dilation,
 88 |                                            groups=groups, bias=bias,
 89 |                                            padding_mode=padding_mode,
 90 |                                            device=device, dtype=dtype)
 91 |         assert stride == 1
 92 |         self.causal_padding = (kernel_size - 1, 0)
 93 | 
 94 |     def forward(self, x: torch.Tensor):
 95 |         x = F.pad(x, self.causal_padding)
 96 |         x = super(CausalConv1d, self).forward(x)
 97 |         return x
 98 | 
 99 | 
100 | class ConditionalDecoder(nn.Module):
101 |     def __init__(
102 |         self,
103 |         in_channels=320,
104 |         out_channels=80,
105 |         causal=True,
106 |         channels=[256],
107 |         dropout=0.0,
108 |         attention_head_dim=64,
109 |         n_blocks=4,
110 |         num_mid_blocks=12,
111 |         num_heads=8,
112 |         act_fn="gelu",
113 |     ):
114 |         """
115 |         This decoder requires an input with the same shape of the target. So, if your text content
116 |         is shorter or longer than the outputs, please re-sampling it before feeding to the decoder.
117 |         """
118 |         super().__init__()
119 |         channels = tuple(channels)
120 |         self.in_channels = in_channels
121 |         self.out_channels = out_channels
122 |         self.causal = causal
123 |         self.time_embeddings = SinusoidalPosEmb(in_channels)
124 |         time_embed_dim = channels[0] * 4
125 |         self.time_mlp = TimestepEmbedding(
126 |             in_channels=in_channels,
127 |             time_embed_dim=time_embed_dim,
128 |             act_fn="silu",
129 |         )
130 |         self.down_blocks = nn.ModuleList([])
131 |         self.mid_blocks = nn.ModuleList([])
132 |         self.up_blocks = nn.ModuleList([])
133 | 
134 |         # NOTE jrm: `static_chunk_size` is missing?
135 |         self.static_chunk_size = 0
136 | 
137 |         output_channel = in_channels
138 |         for i in range(len(channels)):  # pylint: disable=consider-using-enumerate
139 |             input_channel = output_channel
140 |             output_channel = channels[i]
141 |             is_last = i == len(channels) - 1
142 |             resnet = CausalResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim) if self.causal else \
143 |                 ResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim)
144 |             transformer_blocks = nn.ModuleList(
145 |                 [
146 |                     BasicTransformerBlock(
147 |                         dim=output_channel,
148 |                         num_attention_heads=num_heads,
149 |                         attention_head_dim=attention_head_dim,
150 |                         dropout=dropout,
151 |                         activation_fn=act_fn,
152 |                     )
153 |                     for _ in range(n_blocks)
154 |                 ]
155 |             )
156 |             downsample = (
157 |                 Downsample1D(output_channel) if not is_last else
158 |                 CausalConv1d(output_channel, output_channel, 3) if self.causal else nn.Conv1d(output_channel, output_channel, 3, padding=1)
159 |             )
160 |             self.down_blocks.append(nn.ModuleList([resnet, transformer_blocks, downsample]))
161 | 
162 |         for _ in range(num_mid_blocks):
163 |             input_channel = channels[-1]
164 |             out_channels = channels[-1]
165 |             resnet = CausalResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim) if self.causal else \
166 |                 ResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim)
167 | 
168 |             transformer_blocks = nn.ModuleList(
169 |                 [
170 |                     BasicTransformerBlock(
171 |                         dim=output_channel,
172 |                         num_attention_heads=num_heads,
173 |                         attention_head_dim=attention_head_dim,
174 |                         dropout=dropout,
175 |                         activation_fn=act_fn,
176 |                     )
177 |                     for _ in range(n_blocks)
178 |                 ]
179 |             )
180 | 
181 |             self.mid_blocks.append(nn.ModuleList([resnet, transformer_blocks]))
182 | 
183 |         channels = channels[::-1] + (channels[0],)
184 |         for i in range(len(channels) - 1):
185 |             input_channel = channels[i] * 2
186 |             output_channel = channels[i + 1]
187 |             is_last = i == len(channels) - 2
188 |             resnet = CausalResnetBlock1D(
189 |                 dim=input_channel,
190 |                 dim_out=output_channel,
191 |                 time_emb_dim=time_embed_dim,
192 |             ) if self.causal else ResnetBlock1D(
193 |                 dim=input_channel,
194 |                 dim_out=output_channel,
195 |                 time_emb_dim=time_embed_dim,
196 |             )
197 |             transformer_blocks = nn.ModuleList(
198 |                 [
199 |                     BasicTransformerBlock(
200 |                         dim=output_channel,
201 |                         num_attention_heads=num_heads,
202 |                         attention_head_dim=attention_head_dim,
203 |                         dropout=dropout,
204 |                         activation_fn=act_fn,
205 |                     )
206 |                     for _ in range(n_blocks)
207 |                 ]
208 |             )
209 |             upsample = (
210 |                 Upsample1D(output_channel, use_conv_transpose=True)
211 |                 if not is_last
212 |                 else CausalConv1d(output_channel, output_channel, 3) if self.causal else nn.Conv1d(output_channel, output_channel, 3, padding=1)
213 |             )
214 |             self.up_blocks.append(nn.ModuleList([resnet, transformer_blocks, upsample]))
215 |         self.final_block = CausalBlock1D(channels[-1], channels[-1]) if self.causal else Block1D(channels[-1], channels[-1])
216 |         self.final_proj = nn.Conv1d(channels[-1], self.out_channels, 1)
217 |         self.initialize_weights()
218 | 
219 |     def initialize_weights(self):
220 |         for m in self.modules():
221 |             if isinstance(m, nn.Conv1d):
222 |                 nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
223 |                 if m.bias is not None:
224 |                     nn.init.constant_(m.bias, 0)
225 |             elif isinstance(m, nn.GroupNorm):
226 |                 nn.init.constant_(m.weight, 1)
227 |                 nn.init.constant_(m.bias, 0)
228 |             elif isinstance(m, nn.Linear):
229 |                 nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
230 |                 if m.bias is not None:
231 |                     nn.init.constant_(m.bias, 0)
232 | 
233 |     def forward(self, x, mask, mu, t, spks=None, cond=None):
234 |         """Forward pass of the UNet1DConditional model.
235 | 
236 |         Args:
237 |             x (torch.Tensor): shape (batch_size, in_channels, time)
238 |             mask (_type_): shape (batch_size, 1, time)
239 |             t (_type_): shape (batch_size)
240 |             spks (_type_, optional): shape: (batch_size, condition_channels). Defaults to None.
241 |             cond (_type_, optional): placeholder for future use. Defaults to None.
242 | 
243 |         Raises:
244 |             ValueError: _description_
245 |             ValueError: _description_
246 | 
247 |         Returns:
248 |             _type_: _description_
249 |         """
250 | 
251 |         t = self.time_embeddings(t).to(t.dtype)
252 |         t = self.time_mlp(t)
253 | 
254 |         x = pack([x, mu], "b * t")[0]
255 | 
256 |         if spks is not None:
257 |             spks = repeat(spks, "b c -> b c t", t=x.shape[-1])
258 |             x = pack([x, spks], "b * t")[0]
259 |         if cond is not None:
260 |             x = pack([x, cond], "b * t")[0]
261 | 
262 |         hiddens = []
263 |         masks = [mask]
264 |         for resnet, transformer_blocks, downsample in self.down_blocks:
265 |             mask_down = masks[-1]
266 |             x = resnet(x, mask_down, t)
267 |             x = rearrange(x, "b c t -> b t c").contiguous()
268 |             # attn_mask = torch.matmul(mask_down.transpose(1, 2).contiguous(), mask_down)
269 |             attn_mask = add_optional_chunk_mask(x, mask_down.bool(), False, False, 0, self.static_chunk_size, -1)
270 |             attn_mask = mask_to_bias(attn_mask == 1, x.dtype)
271 |             for transformer_block in transformer_blocks:
272 |                 x = transformer_block(
273 |                     hidden_states=x,
274 |                     attention_mask=attn_mask,
275 |                     timestep=t,
276 |                 )
277 |             x = rearrange(x, "b t c -> b c t").contiguous()
278 |             hiddens.append(x)  # Save hidden states for skip connections
279 |             x = downsample(x * mask_down)
280 |             masks.append(mask_down[:, :, ::2])
281 |         masks = masks[:-1]
282 |         mask_mid = masks[-1]
283 | 
284 |         for resnet, transformer_blocks in self.mid_blocks:
285 |             x = resnet(x, mask_mid, t)
286 |             x = rearrange(x, "b c t -> b t c").contiguous()
287 |             # attn_mask = torch.matmul(mask_mid.transpose(1, 2).contiguous(), mask_mid)
288 |             attn_mask = add_optional_chunk_mask(x, mask_mid.bool(), False, False, 0, self.static_chunk_size, -1)
289 |             attn_mask = mask_to_bias(attn_mask == 1, x.dtype)
290 |             for transformer_block in transformer_blocks:
291 |                 x = transformer_block(
292 |                     hidden_states=x,
293 |                     attention_mask=attn_mask,
294 |                     timestep=t,
295 |                 )
296 |             x = rearrange(x, "b t c -> b c t").contiguous()
297 | 
298 |         for resnet, transformer_blocks, upsample in self.up_blocks:
299 |             mask_up = masks.pop()
300 |             skip = hiddens.pop()
301 |             x = pack([x[:, :, :skip.shape[-1]], skip], "b * t")[0]
302 |             x = resnet(x, mask_up, t)
303 |             x = rearrange(x, "b c t -> b t c").contiguous()
304 |             # attn_mask = torch.matmul(mask_up.transpose(1, 2).contiguous(), mask_up)
305 |             attn_mask = add_optional_chunk_mask(x, mask_up.bool(), False, False, 0, self.static_chunk_size, -1)
306 |             attn_mask = mask_to_bias(attn_mask == 1, x.dtype)
307 |             for transformer_block in transformer_blocks:
308 |                 x = transformer_block(
309 |                     hidden_states=x,
310 |                     attention_mask=attn_mask,
311 |                     timestep=t,
312 |                 )
313 |             x = rearrange(x, "b t c -> b c t").contiguous()
314 |             x = upsample(x * mask_up)
315 |         x = self.final_block(x, mask_up)
316 |         output = self.final_proj(x * mask_up)
317 |         return output * mask
318 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/f0_predictor.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Kai Hu)
 2 | #
 3 | # Licensed under the Apache License, Version 2.0 (the "License");
 4 | # you may not use this file except in compliance with the License.
 5 | # You may obtain a copy of the License at
 6 | #
 7 | #     http://www.apache.org/licenses/LICENSE-2.0
 8 | #
 9 | # Unless required by applicable law or agreed to in writing, software
10 | # distributed under the License is distributed on an "AS IS" BASIS,
11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12 | # See the License for the specific language governing permissions and
13 | # limitations under the License.
14 | import torch
15 | import torch.nn as nn
16 | from torch.nn.utils.parametrizations import weight_norm
17 | 
18 | 
19 | class ConvRNNF0Predictor(nn.Module):
20 |     def __init__(self,
21 |                  num_class: int = 1,
22 |                  in_channels: int = 80,
23 |                  cond_channels: int = 512
24 |                  ):
25 |         super().__init__()
26 | 
27 |         self.num_class = num_class
28 |         self.condnet = nn.Sequential(
29 |             weight_norm(
30 |                 nn.Conv1d(in_channels, cond_channels, kernel_size=3, padding=1)
31 |             ),
32 |             nn.ELU(),
33 |             weight_norm(
34 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
35 |             ),
36 |             nn.ELU(),
37 |             weight_norm(
38 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
39 |             ),
40 |             nn.ELU(),
41 |             weight_norm(
42 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
43 |             ),
44 |             nn.ELU(),
45 |             weight_norm(
46 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
47 |             ),
48 |             nn.ELU(),
49 |         )
50 |         self.classifier = nn.Linear(in_features=cond_channels, out_features=self.num_class)
51 | 
52 |     def forward(self, x: torch.Tensor) -> torch.Tensor:
53 |         x = self.condnet(x)
54 |         x = x.transpose(1, 2)
55 |         return torch.abs(self.classifier(x).squeeze(-1))
56 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/flow.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Zhihao Du)
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | import logging
 15 | import random
 16 | from typing import Dict, Optional
 17 | import torch
 18 | import torch.nn as nn
 19 | from torch.nn import functional as F
 20 | from .utils.mask import make_pad_mask
 21 | from .configs import CFM_PARAMS
 22 | 
 23 | 
 24 | class MaskedDiffWithXvec(torch.nn.Module):
 25 |     def __init__(
 26 |         self,
 27 |         input_size: int = 512,
 28 |         output_size: int = 80,
 29 |         spk_embed_dim: int = 192,
 30 |         output_type: str = "mel",
 31 |         vocab_size: int = 4096,
 32 |         input_frame_rate: int = 50,
 33 |         only_mask_loss: bool = True,
 34 |         encoder: torch.nn.Module = None,
 35 |         length_regulator: torch.nn.Module = None,
 36 |         decoder: torch.nn.Module = None,
 37 |         decoder_conf: Dict = {
 38 |             'in_channels': 240,
 39 |             'out_channel': 80,
 40 |             'spk_emb_dim': 80,
 41 |             'n_spks': 1,
 42 |             'cfm_params': CFM_PARAMS,
 43 |             'decoder_params': {
 44 |                 'channels': [256, 256],
 45 |                 'dropout': 0.0,
 46 |                 'attention_head_dim': 64,
 47 |                 'n_blocks': 4,
 48 |                 'num_mid_blocks': 12,
 49 |                 'num_heads': 8,
 50 |                 'act_fn': 'gelu',
 51 |             }
 52 |         },
 53 |         mel_feat_conf: Dict = {
 54 |             'n_fft': 1024,
 55 |             'num_mels': 80,
 56 |             'sampling_rate': 22050,
 57 |             'hop_size': 256,
 58 |             'win_size': 1024,
 59 |             'fmin': 0,
 60 |             'fmax': 8000
 61 |         }
 62 |     ):
 63 |         super().__init__()
 64 |         self.input_size = input_size
 65 |         self.output_size = output_size
 66 |         self.decoder_conf = decoder_conf
 67 |         self.mel_feat_conf = mel_feat_conf
 68 |         self.vocab_size = vocab_size
 69 |         self.output_type = output_type
 70 |         self.input_frame_rate = input_frame_rate
 71 |         logging.info(f"input frame rate={self.input_frame_rate}")
 72 |         self.input_embedding = nn.Embedding(vocab_size, input_size)
 73 |         self.spk_embed_affine_layer = torch.nn.Linear(spk_embed_dim, output_size)
 74 |         self.encoder = encoder
 75 |         self.encoder_proj = torch.nn.Linear(self.encoder.output_size(), output_size)
 76 |         self.decoder = decoder
 77 |         self.length_regulator = length_regulator
 78 |         self.only_mask_loss = only_mask_loss
 79 | 
 80 |     def forward(
 81 |             self,
 82 |             batch: dict,
 83 |             device: torch.device,
 84 |     ) -> Dict[str, Optional[torch.Tensor]]:
 85 |         token = batch['speech_token'].to(device)
 86 |         token_len = batch['speech_token_len'].to(device)
 87 |         feat = batch['speech_feat'].to(device)
 88 |         feat_len = batch['speech_feat_len'].to(device)
 89 |         embedding = batch['embedding'].to(device)
 90 | 
 91 |         # xvec projection
 92 |         embedding = F.normalize(embedding, dim=1)
 93 |         embedding = self.spk_embed_affine_layer(embedding)
 94 | 
 95 |         # concat text and prompt_text
 96 |         mask = (~make_pad_mask(token_len)).float().unsqueeze(-1).to(device)
 97 |         token = self.input_embedding(torch.clamp(token, min=0)) * mask
 98 | 
 99 |         # text encode
100 |         h, h_lengths = self.encoder(token, token_len)
101 |         h = self.encoder_proj(h)
102 |         h, h_lengths = self.length_regulator(h, feat_len)
103 | 
104 |         # get conditions
105 |         conds = torch.zeros(feat.shape, device=token.device)
106 |         for i, j in enumerate(feat_len):
107 |             if random.random() < 0.5:
108 |                 continue
109 |             index = random.randint(0, int(0.3 * j))
110 |             conds[i, :index] = feat[i, :index]
111 |         conds = conds.transpose(1, 2)
112 | 
113 |         mask = (~make_pad_mask(feat_len)).to(h)
114 |         feat = F.interpolate(feat.unsqueeze(dim=1), size=h.shape[1:], mode="nearest").squeeze(dim=1)
115 |         loss, _ = self.decoder.compute_loss(
116 |             feat.transpose(1, 2).contiguous(),
117 |             mask.unsqueeze(1),
118 |             h.transpose(1, 2).contiguous(),
119 |             embedding,
120 |             cond=conds
121 |         )
122 |         return {'loss': loss}
123 | 
124 |     @torch.inference_mode()
125 |     def inference(self,
126 |                   token,
127 |                   token_len,
128 |                   prompt_token,
129 |                   prompt_token_len,
130 |                   prompt_feat,
131 |                   prompt_feat_len,
132 |                   embedding,
133 |                   flow_cache):
134 |         if self.fp16 is True:
135 |             prompt_feat = prompt_feat.half()
136 |             embedding = embedding.half()
137 | 
138 |         assert token.shape[0] == 1
139 |         # xvec projection
140 |         embedding = F.normalize(embedding, dim=1)
141 |         embedding = self.spk_embed_affine_layer(embedding)
142 | 
143 |         # concat text and prompt_text
144 |         token_len1, token_len2 = prompt_token.shape[1], token.shape[1]
145 |         token, token_len = torch.concat([prompt_token, token], dim=1), prompt_token_len + token_len
146 |         mask = (~make_pad_mask(token_len)).unsqueeze(-1).to(embedding)
147 |         token = self.input_embedding(torch.clamp(token, min=0)) * mask
148 | 
149 |         # text encode
150 |         h, h_lengths = self.encoder(token, token_len)
151 |         h = self.encoder_proj(h)
152 |         mel_len1, mel_len2 = prompt_feat.shape[1], int(token_len2 / self.input_frame_rate * 22050 / 256)
153 |         h, h_lengths = self.length_regulator.inference(h[:, :token_len1], h[:, token_len1:], mel_len1, mel_len2, self.input_frame_rate)
154 | 
155 |         # get conditions
156 |         conds = torch.zeros([1, mel_len1 + mel_len2, self.output_size], device=token.device).to(h.dtype)
157 |         conds[:, :mel_len1] = prompt_feat
158 |         conds = conds.transpose(1, 2)
159 | 
160 |         mask = (~make_pad_mask(torch.tensor([mel_len1 + mel_len2]))).to(h)
161 |         feat, flow_cache = self.decoder(
162 |             mu=h.transpose(1, 2).contiguous(),
163 |             mask=mask.unsqueeze(1),
164 |             spks=embedding,
165 |             cond=conds,
166 |             n_timesteps=10,
167 |             prompt_len=mel_len1,
168 |             flow_cache=flow_cache
169 |         )
170 |         feat = feat[:, :, mel_len1:]
171 |         assert feat.shape[2] == mel_len2
172 |         return feat.float(), flow_cache
173 | 
174 | 
175 | class CausalMaskedDiffWithXvec(torch.nn.Module):
176 |     def __init__(
177 |         self,
178 |         input_size: int = 512,
179 |         output_size: int = 80,
180 |         spk_embed_dim: int = 192,
181 |         output_type: str = "mel",
182 |         vocab_size: int = 6561,
183 |         input_frame_rate: int = 25,
184 |         only_mask_loss: bool = True,
185 |         token_mel_ratio: int = 2,
186 |         pre_lookahead_len: int = 3,
187 |         encoder: torch.nn.Module = None,
188 |         decoder: torch.nn.Module = None,
189 |         decoder_conf: Dict = {
190 |             'in_channels': 240,
191 |             'out_channel': 80,
192 |             'spk_emb_dim': 80,
193 |             'n_spks': 1,
194 |             'cfm_params': CFM_PARAMS,
195 |             'decoder_params': {
196 |                 'channels': [256, 256],
197 |                 'dropout': 0.0,
198 |                 'attention_head_dim': 64,
199 |                 'n_blocks': 4,
200 |                 'num_mid_blocks': 12,
201 |                 'num_heads': 8,
202 |                 'act_fn': 'gelu',
203 |             }
204 |         },
205 |         mel_feat_conf: Dict = {
206 |             'n_fft': 1024,
207 |             'num_mels': 80,
208 |             'sampling_rate': 22050,
209 |             'hop_size': 256,
210 |             'win_size': 1024,
211 |             'fmin': 0,
212 |             'fmax': 8000
213 |         }
214 |     ):
215 |         super().__init__()
216 |         self.input_size = input_size
217 |         self.output_size = output_size
218 |         self.decoder_conf = decoder_conf
219 |         self.mel_feat_conf = mel_feat_conf
220 |         self.vocab_size = vocab_size
221 |         self.output_type = output_type
222 |         self.input_frame_rate = input_frame_rate
223 |         logging.info(f"input frame rate={self.input_frame_rate}")
224 |         self.input_embedding = nn.Embedding(vocab_size, input_size)
225 |         self.spk_embed_affine_layer = torch.nn.Linear(spk_embed_dim, output_size)
226 |         self.encoder = encoder
227 |         self.encoder_proj = torch.nn.Linear(self.encoder.output_size(), output_size)
228 |         self.decoder = decoder
229 |         self.only_mask_loss = only_mask_loss
230 |         self.token_mel_ratio = token_mel_ratio
231 |         self.pre_lookahead_len = pre_lookahead_len
232 | 
233 |         # FIXME: this was missing - just putting it in as false
234 |         self.fp16 = False
235 | 
236 |     @torch.inference_mode()
237 |     def inference(self,
238 |                   token,
239 |                   token_len,
240 |                   prompt_token,
241 |                   prompt_token_len,
242 |                   prompt_feat,
243 |                   prompt_feat_len,
244 |                   embedding,
245 |                   finalize):
246 |         if self.fp16 is True:
247 |             prompt_feat = prompt_feat.half()
248 |             embedding = embedding.half()
249 | 
250 |         assert token.shape[0] == 1
251 |         # xvec projection
252 |         embedding = F.normalize(embedding, dim=1)
253 |         embedding = self.spk_embed_affine_layer(embedding)
254 | 
255 |         # concat text and prompt_text
256 |         token, token_len = torch.concat([prompt_token, token], dim=1), prompt_token_len + token_len
257 |         mask = (~make_pad_mask(token_len)).unsqueeze(-1).to(embedding)
258 |         token = self.input_embedding(torch.clamp(token, min=0)) * mask
259 | 
260 |         # text encode
261 |         h, h_lengths = self.encoder(token, token_len)
262 |         if finalize is False:
263 |             h = h[:, :-self.pre_lookahead_len * self.token_mel_ratio]
264 |         mel_len1, mel_len2 = prompt_feat.shape[1], h.shape[1] - prompt_feat.shape[1]
265 |         h = self.encoder_proj(h)
266 | 
267 |         # get conditions
268 |         conds = torch.zeros([1, mel_len1 + mel_len2, self.output_size], device=token.device).to(h.dtype)
269 |         conds[:, :mel_len1] = prompt_feat
270 |         conds = conds.transpose(1, 2)
271 | 
272 |         mask = (~make_pad_mask(torch.tensor([mel_len1 + mel_len2]))).to(h)
273 |         feat, _ = self.decoder(
274 |             mu=h.transpose(1, 2).contiguous(),
275 |             mask=mask.unsqueeze(1),
276 |             spks=embedding,
277 |             cond=conds,
278 |             n_timesteps=10
279 |         )
280 |         feat = feat[:, :, mel_len1:]
281 |         assert feat.shape[2] == mel_len2
282 |         return feat.float(), None  # NOTE jrm: why are they returning None here?
283 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/flow_matching.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Zhihao Du)
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | import threading
 15 | import torch
 16 | import torch.nn.functional as F
 17 | from .matcha.flow_matching import BASECFM
 18 | from .configs import CFM_PARAMS
 19 | 
 20 | 
 21 | class ConditionalCFM(BASECFM):
 22 |     def __init__(self, in_channels, cfm_params, n_spks=1, spk_emb_dim=64, estimator: torch.nn.Module = None):
 23 |         super().__init__(
 24 |             n_feats=in_channels,
 25 |             cfm_params=cfm_params,
 26 |             n_spks=n_spks,
 27 |             spk_emb_dim=spk_emb_dim,
 28 |         )
 29 |         self.t_scheduler = cfm_params.t_scheduler
 30 |         self.training_cfg_rate = cfm_params.training_cfg_rate
 31 |         self.inference_cfg_rate = cfm_params.inference_cfg_rate
 32 |         in_channels = in_channels + (spk_emb_dim if n_spks > 0 else 0)
 33 |         # Just change the architecture of the estimator here
 34 |         self.estimator = estimator
 35 |         self.lock = threading.Lock()
 36 | 
 37 |     @torch.inference_mode()
 38 |     def forward(self, mu, mask, n_timesteps, temperature=1.0, spks=None, cond=None, prompt_len=0, flow_cache=torch.zeros(1, 80, 0, 2)):
 39 |         """Forward diffusion
 40 | 
 41 |         Args:
 42 |             mu (torch.Tensor): output of encoder
 43 |                 shape: (batch_size, n_feats, mel_timesteps)
 44 |             mask (torch.Tensor): output_mask
 45 |                 shape: (batch_size, 1, mel_timesteps)
 46 |             n_timesteps (int): number of diffusion steps
 47 |             temperature (float, optional): temperature for scaling noise. Defaults to 1.0.
 48 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 49 |                 shape: (batch_size, spk_emb_dim)
 50 |             cond: Not used but kept for future purposes
 51 | 
 52 |         Returns:
 53 |             sample: generated mel-spectrogram
 54 |                 shape: (batch_size, n_feats, mel_timesteps)
 55 |         """
 56 | 
 57 |         z = torch.randn_like(mu).to(mu.device).to(mu.dtype) * temperature
 58 |         cache_size = flow_cache.shape[2]
 59 |         # fix prompt and overlap part mu and z
 60 |         if cache_size != 0:
 61 |             z[:, :, :cache_size] = flow_cache[:, :, :, 0]
 62 |             mu[:, :, :cache_size] = flow_cache[:, :, :, 1]
 63 |         z_cache = torch.concat([z[:, :, :prompt_len], z[:, :, -34:]], dim=2)
 64 |         mu_cache = torch.concat([mu[:, :, :prompt_len], mu[:, :, -34:]], dim=2)
 65 |         flow_cache = torch.stack([z_cache, mu_cache], dim=-1)
 66 | 
 67 |         t_span = torch.linspace(0, 1, n_timesteps + 1, device=mu.device, dtype=mu.dtype)
 68 |         if self.t_scheduler == 'cosine':
 69 |             t_span = 1 - torch.cos(t_span * 0.5 * torch.pi)
 70 |         return self.solve_euler(z, t_span=t_span, mu=mu, mask=mask, spks=spks, cond=cond), flow_cache
 71 | 
 72 |     def solve_euler(self, x, t_span, mu, mask, spks, cond):
 73 |         """
 74 |         Fixed euler solver for ODEs.
 75 |         Args:
 76 |             x (torch.Tensor): random noise
 77 |             t_span (torch.Tensor): n_timesteps interpolated
 78 |                 shape: (n_timesteps + 1,)
 79 |             mu (torch.Tensor): output of encoder
 80 |                 shape: (batch_size, n_feats, mel_timesteps)
 81 |             mask (torch.Tensor): output_mask
 82 |                 shape: (batch_size, 1, mel_timesteps)
 83 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 84 |                 shape: (batch_size, spk_emb_dim)
 85 |             cond: Not used but kept for future purposes
 86 |         """
 87 |         t, _, dt = t_span[0], t_span[-1], t_span[1] - t_span[0]
 88 |         t = t.unsqueeze(dim=0)
 89 | 
 90 |         # I am storing this because I can later plot it by putting a debugger here and saving it to a file
 91 |         # Or in future might add like a return_all_steps flag
 92 |         sol = []
 93 | 
 94 |         # Do not use concat, it may cause memory format changed and trt infer with wrong results!
 95 |         x_in = torch.zeros([2, 80, x.size(2)], device=x.device, dtype=x.dtype)
 96 |         mask_in = torch.zeros([2, 1, x.size(2)], device=x.device, dtype=x.dtype)
 97 |         mu_in = torch.zeros([2, 80, x.size(2)], device=x.device, dtype=x.dtype)
 98 |         t_in = torch.zeros([2], device=x.device, dtype=x.dtype)
 99 |         spks_in = torch.zeros([2, 80], device=x.device, dtype=x.dtype)
100 |         cond_in = torch.zeros([2, 80, x.size(2)], device=x.device, dtype=x.dtype)
101 |         for step in range(1, len(t_span)):
102 |             # Classifier-Free Guidance inference introduced in VoiceBox
103 |             x_in[:] = x
104 |             mask_in[:] = mask
105 |             mu_in[0] = mu
106 |             t_in[:] = t.unsqueeze(0)
107 |             spks_in[0] = spks
108 |             cond_in[0] = cond
109 |             dphi_dt = self.forward_estimator(
110 |                 x_in, mask_in,
111 |                 mu_in, t_in,
112 |                 spks_in,
113 |                 cond_in
114 |             )
115 |             dphi_dt, cfg_dphi_dt = torch.split(dphi_dt, [x.size(0), x.size(0)], dim=0)
116 |             dphi_dt = ((1.0 + self.inference_cfg_rate) * dphi_dt - self.inference_cfg_rate * cfg_dphi_dt)
117 |             x = x + dt * dphi_dt
118 |             t = t + dt
119 |             sol.append(x)
120 |             if step < len(t_span) - 1:
121 |                 dt = t_span[step + 1] - t
122 | 
123 |         return sol[-1].float()
124 | 
125 |     def forward_estimator(self, x, mask, mu, t, spks, cond):
126 |         if isinstance(self.estimator, torch.nn.Module):
127 |             return self.estimator.forward(x, mask, mu, t, spks, cond)
128 |         else:
129 |             with self.lock:
130 |                 self.estimator.set_input_shape('x', (2, 80, x.size(2)))
131 |                 self.estimator.set_input_shape('mask', (2, 1, x.size(2)))
132 |                 self.estimator.set_input_shape('mu', (2, 80, x.size(2)))
133 |                 self.estimator.set_input_shape('t', (2,))
134 |                 self.estimator.set_input_shape('spks', (2, 80))
135 |                 self.estimator.set_input_shape('cond', (2, 80, x.size(2)))
136 |                 # run trt engine
137 |                 self.estimator.execute_v2([x.contiguous().data_ptr(),
138 |                                            mask.contiguous().data_ptr(),
139 |                                            mu.contiguous().data_ptr(),
140 |                                            t.contiguous().data_ptr(),
141 |                                            spks.contiguous().data_ptr(),
142 |                                            cond.contiguous().data_ptr(),
143 |                                            x.data_ptr()])
144 |             return x
145 | 
146 |     def compute_loss(self, x1, mask, mu, spks=None, cond=None):
147 |         """Computes diffusion loss
148 | 
149 |         Args:
150 |             x1 (torch.Tensor): Target
151 |                 shape: (batch_size, n_feats, mel_timesteps)
152 |             mask (torch.Tensor): target mask
153 |                 shape: (batch_size, 1, mel_timesteps)
154 |             mu (torch.Tensor): output of encoder
155 |                 shape: (batch_size, n_feats, mel_timesteps)
156 |             spks (torch.Tensor, optional): speaker embedding. Defaults to None.
157 |                 shape: (batch_size, spk_emb_dim)
158 | 
159 |         Returns:
160 |             loss: conditional flow matching loss
161 |             y: conditional flow
162 |                 shape: (batch_size, n_feats, mel_timesteps)
163 |         """
164 |         b, _, t = mu.shape
165 | 
166 |         # random timestep
167 |         t = torch.rand([b, 1, 1], device=mu.device, dtype=mu.dtype)
168 |         if self.t_scheduler == 'cosine':
169 |             t = 1 - torch.cos(t * 0.5 * torch.pi)
170 |         # sample noise p(x_0)
171 |         z = torch.randn_like(x1)
172 | 
173 |         y = (1 - (1 - self.sigma_min) * t) * z + t * x1
174 |         u = x1 - (1 - self.sigma_min) * z
175 | 
176 |         # during training, we randomly drop condition to trade off mode coverage and sample fidelity
177 |         if self.training_cfg_rate > 0:
178 |             cfg_mask = torch.rand(b, device=x1.device) > self.training_cfg_rate
179 |             mu = mu * cfg_mask.view(-1, 1, 1)
180 |             spks = spks * cfg_mask.view(-1, 1)
181 |             cond = cond * cfg_mask.view(-1, 1, 1)
182 | 
183 |         pred = self.estimator(y, mask, mu, t.squeeze(), spks, cond)
184 |         loss = F.mse_loss(pred * mask, u * mask, reduction="sum") / (torch.sum(mask) * u.shape[1])
185 |         return loss, y
186 | 
187 | 
188 | class CausalConditionalCFM(ConditionalCFM):
189 |     def __init__(self, in_channels=240, cfm_params=CFM_PARAMS, n_spks=1, spk_emb_dim=80, estimator=None):
190 |         super().__init__(in_channels, cfm_params, n_spks, spk_emb_dim, estimator)
191 |         self.rand_noise = torch.randn([1, 80, 50 * 300])
192 | 
193 |     @torch.inference_mode()
194 |     def forward(self, mu, mask, n_timesteps, temperature=1.0, spks=None, cond=None):
195 |         """Forward diffusion
196 | 
197 |         Args:
198 |             mu (torch.Tensor): output of encoder
199 |                 shape: (batch_size, n_feats, mel_timesteps)
200 |             mask (torch.Tensor): output_mask
201 |                 shape: (batch_size, 1, mel_timesteps)
202 |             n_timesteps (int): number of diffusion steps
203 |             temperature (float, optional): temperature for scaling noise. Defaults to 1.0.
204 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
205 |                 shape: (batch_size, spk_emb_dim)
206 |             cond: Not used but kept for future purposes
207 | 
208 |         Returns:
209 |             sample: generated mel-spectrogram
210 |                 shape: (batch_size, n_feats, mel_timesteps)
211 |         """
212 | 
213 |         z = self.rand_noise[:, :, :mu.size(2)].to(mu.device).to(mu.dtype) * temperature
214 |         # fix prompt and overlap part mu and z
215 |         t_span = torch.linspace(0, 1, n_timesteps + 1, device=mu.device, dtype=mu.dtype)
216 |         if self.t_scheduler == 'cosine':
217 |             t_span = 1 - torch.cos(t_span * 0.5 * torch.pi)
218 |         return self.solve_euler(z, t_span=t_span, mu=mu, mask=mask, spks=spks, cond=cond), None
219 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/matcha/flow_matching.py:
--------------------------------------------------------------------------------
  1 | from abc import ABC
  2 | 
  3 | import torch
  4 | import torch.nn.functional as F
  5 | 
  6 | from .decoder import Decoder
  7 | 
  8 | 
  9 | class BASECFM(torch.nn.Module, ABC):
 10 |     def __init__(
 11 |         self,
 12 |         n_feats,
 13 |         cfm_params,
 14 |         n_spks=1,
 15 |         spk_emb_dim=128,
 16 |     ):
 17 |         super().__init__()
 18 |         self.n_feats = n_feats
 19 |         self.n_spks = n_spks
 20 |         self.spk_emb_dim = spk_emb_dim
 21 |         self.solver = cfm_params.solver
 22 |         if hasattr(cfm_params, "sigma_min"):
 23 |             self.sigma_min = cfm_params.sigma_min
 24 |         else:
 25 |             self.sigma_min = 1e-4
 26 | 
 27 |         self.estimator = None
 28 | 
 29 |     @torch.inference_mode()
 30 |     def forward(self, mu, mask, n_timesteps, temperature=1.0, spks=None, cond=None):
 31 |         """Forward diffusion
 32 | 
 33 |         Args:
 34 |             mu (torch.Tensor): output of encoder
 35 |                 shape: (batch_size, n_feats, mel_timesteps)
 36 |             mask (torch.Tensor): output_mask
 37 |                 shape: (batch_size, 1, mel_timesteps)
 38 |             n_timesteps (int): number of diffusion steps
 39 |             temperature (float, optional): temperature for scaling noise. Defaults to 1.0.
 40 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 41 |                 shape: (batch_size, spk_emb_dim)
 42 |             cond: Not used but kept for future purposes
 43 | 
 44 |         Returns:
 45 |             sample: generated mel-spectrogram
 46 |                 shape: (batch_size, n_feats, mel_timesteps)
 47 |         """
 48 |         z = torch.randn_like(mu) * temperature
 49 |         t_span = torch.linspace(0, 1, n_timesteps + 1, device=mu.device)
 50 |         return self.solve_euler(z, t_span=t_span, mu=mu, mask=mask, spks=spks, cond=cond)
 51 | 
 52 |     def solve_euler(self, x, t_span, mu, mask, spks, cond):
 53 |         """
 54 |         Fixed euler solver for ODEs.
 55 |         Args:
 56 |             x (torch.Tensor): random noise
 57 |             t_span (torch.Tensor): n_timesteps interpolated
 58 |                 shape: (n_timesteps + 1,)
 59 |             mu (torch.Tensor): output of encoder
 60 |                 shape: (batch_size, n_feats, mel_timesteps)
 61 |             mask (torch.Tensor): output_mask
 62 |                 shape: (batch_size, 1, mel_timesteps)
 63 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 64 |                 shape: (batch_size, spk_emb_dim)
 65 |             cond: Not used but kept for future purposes
 66 |         """
 67 |         t, _, dt = t_span[0], t_span[-1], t_span[1] - t_span[0]
 68 | 
 69 |         # I am storing this because I can later plot it by putting a debugger here and saving it to a file
 70 |         # Or in future might add like a return_all_steps flag
 71 |         sol = []
 72 | 
 73 |         for step in range(1, len(t_span)):
 74 |             dphi_dt = self.estimator(x, mask, mu, t, spks, cond)
 75 | 
 76 |             x = x + dt * dphi_dt
 77 |             t = t + dt
 78 |             sol.append(x)
 79 |             if step < len(t_span) - 1:
 80 |                 dt = t_span[step + 1] - t
 81 | 
 82 |         return sol[-1]
 83 | 
 84 |     def compute_loss(self, x1, mask, mu, spks=None, cond=None):
 85 |         """Computes diffusion loss
 86 | 
 87 |         Args:
 88 |             x1 (torch.Tensor): Target
 89 |                 shape: (batch_size, n_feats, mel_timesteps)
 90 |             mask (torch.Tensor): target mask
 91 |                 shape: (batch_size, 1, mel_timesteps)
 92 |             mu (torch.Tensor): output of encoder
 93 |                 shape: (batch_size, n_feats, mel_timesteps)
 94 |             spks (torch.Tensor, optional): speaker embedding. Defaults to None.
 95 |                 shape: (batch_size, spk_emb_dim)
 96 | 
 97 |         Returns:
 98 |             loss: conditional flow matching loss
 99 |             y: conditional flow
100 |                 shape: (batch_size, n_feats, mel_timesteps)
101 |         """
102 |         b, _, t = mu.shape
103 | 
104 |         # random timestep
105 |         t = torch.rand([b, 1, 1], device=mu.device, dtype=mu.dtype)
106 |         # sample noise p(x_0)
107 |         z = torch.randn_like(x1)
108 | 
109 |         y = (1 - (1 - self.sigma_min) * t) * z + t * x1
110 |         u = x1 - (1 - self.sigma_min) * z
111 | 
112 |         loss = F.mse_loss(self.estimator(y, mask, mu, t.squeeze(), spks), u, reduction="sum") / (
113 |             torch.sum(mask) * u.shape[1]
114 |         )
115 |         return loss, y
116 | 
117 | 
118 | class CFM(BASECFM):
119 |     def __init__(self, in_channels, out_channel, cfm_params, decoder_params, n_spks=1, spk_emb_dim=64):
120 |         super().__init__(
121 |             n_feats=in_channels,
122 |             cfm_params=cfm_params,
123 |             n_spks=n_spks,
124 |             spk_emb_dim=spk_emb_dim,
125 |         )
126 | 
127 |         in_channels = in_channels + (spk_emb_dim if n_spks > 1 else 0)
128 |         # Just change the architecture of the estimator here
129 |         self.estimator = Decoder(in_channels=in_channels, out_channels=out_channel, **decoder_params)
130 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/matcha/transformer.py:
--------------------------------------------------------------------------------
  1 | from typing import Any, Dict, Optional
  2 | 
  3 | import torch
  4 | import torch.nn as nn
  5 | from diffusers.models.attention import (
  6 |     GEGLU,
  7 |     GELU,
  8 |     AdaLayerNorm,
  9 |     AdaLayerNormZero,
 10 |     ApproximateGELU,
 11 | )
 12 | from diffusers.models.attention_processor import Attention
 13 | from diffusers.models.lora import LoRACompatibleLinear
 14 | from diffusers.utils.torch_utils import maybe_allow_in_graph
 15 | 
 16 | 
 17 | class SnakeBeta(nn.Module):
 18 |     """
 19 |     A modified Snake function which uses separate parameters for the magnitude of the periodic components
 20 |     Shape:
 21 |         - Input: (B, C, T)
 22 |         - Output: (B, C, T), same shape as the input
 23 |     Parameters:
 24 |         - alpha - trainable parameter that controls frequency
 25 |         - beta - trainable parameter that controls magnitude
 26 |     References:
 27 |         - This activation function is a modified version based on this paper by Liu Ziyin, Tilman Hartwig, Masahito Ueda:
 28 |         https://arxiv.org/abs/2006.08195
 29 |     Examples:
 30 |         >>> a1 = snakebeta(256)
 31 |         >>> x = torch.randn(256)
 32 |         >>> x = a1(x)
 33 |     """
 34 | 
 35 |     def __init__(self, in_features, out_features, alpha=1.0, alpha_trainable=True, alpha_logscale=True):
 36 |         """
 37 |         Initialization.
 38 |         INPUT:
 39 |             - in_features: shape of the input
 40 |             - alpha - trainable parameter that controls frequency
 41 |             - beta - trainable parameter that controls magnitude
 42 |             alpha is initialized to 1 by default, higher values = higher-frequency.
 43 |             beta is initialized to 1 by default, higher values = higher-magnitude.
 44 |             alpha will be trained along with the rest of your model.
 45 |         """
 46 |         super().__init__()
 47 |         self.in_features = out_features if isinstance(out_features, list) else [out_features]
 48 |         self.proj = LoRACompatibleLinear(in_features, out_features)
 49 | 
 50 |         # initialize alpha
 51 |         self.alpha_logscale = alpha_logscale
 52 |         if self.alpha_logscale:  # log scale alphas initialized to zeros
 53 |             self.alpha = nn.Parameter(torch.zeros(self.in_features) * alpha)
 54 |             self.beta = nn.Parameter(torch.zeros(self.in_features) * alpha)
 55 |         else:  # linear scale alphas initialized to ones
 56 |             self.alpha = nn.Parameter(torch.ones(self.in_features) * alpha)
 57 |             self.beta = nn.Parameter(torch.ones(self.in_features) * alpha)
 58 | 
 59 |         self.alpha.requires_grad = alpha_trainable
 60 |         self.beta.requires_grad = alpha_trainable
 61 | 
 62 |         self.no_div_by_zero = 0.000000001
 63 | 
 64 |     def forward(self, x):
 65 |         """
 66 |         Forward pass of the function.
 67 |         Applies the function to the input elementwise.
 68 |         SnakeBeta ∶= x + 1/b * sin^2 (xa)
 69 |         """
 70 |         x = self.proj(x)
 71 |         if self.alpha_logscale:
 72 |             alpha = torch.exp(self.alpha)
 73 |             beta = torch.exp(self.beta)
 74 |         else:
 75 |             alpha = self.alpha
 76 |             beta = self.beta
 77 | 
 78 |         x = x + (1.0 / (beta + self.no_div_by_zero)) * torch.pow(torch.sin(x * alpha), 2)
 79 | 
 80 |         return x
 81 | 
 82 | 
 83 | class FeedForward(nn.Module):
 84 |     r"""
 85 |     A feed-forward layer.
 86 | 
 87 |     Parameters:
 88 |         dim (`int`): The number of channels in the input.
 89 |         dim_out (`int`, *optional*): The number of channels in the output. If not given, defaults to `dim`.
 90 |         mult (`int`, *optional*, defaults to 4): The multiplier to use for the hidden dimension.
 91 |         dropout (`float`, *optional*, defaults to 0.0): The dropout probability to use.
 92 |         activation_fn (`str`, *optional*, defaults to `"geglu"`): Activation function to be used in feed-forward.
 93 |         final_dropout (`bool` *optional*, defaults to False): Apply a final dropout.
 94 |     """
 95 | 
 96 |     def __init__(
 97 |         self,
 98 |         dim: int,
 99 |         dim_out: Optional[int] = None,
100 |         mult: int = 4,
101 |         dropout: float = 0.0,
102 |         activation_fn: str = "geglu",
103 |         final_dropout: bool = False,
104 |     ):
105 |         super().__init__()
106 |         inner_dim = int(dim * mult)
107 |         dim_out = dim_out if dim_out is not None else dim
108 | 
109 |         if activation_fn == "gelu":
110 |             act_fn = GELU(dim, inner_dim)
111 |         if activation_fn == "gelu-approximate":
112 |             act_fn = GELU(dim, inner_dim, approximate="tanh")
113 |         elif activation_fn == "geglu":
114 |             act_fn = GEGLU(dim, inner_dim)
115 |         elif activation_fn == "geglu-approximate":
116 |             act_fn = ApproximateGELU(dim, inner_dim)
117 |         elif activation_fn == "snakebeta":
118 |             act_fn = SnakeBeta(dim, inner_dim)
119 | 
120 |         self.net = nn.ModuleList([])
121 |         # project in
122 |         self.net.append(act_fn)
123 |         # project dropout
124 |         self.net.append(nn.Dropout(dropout))
125 |         # project out
126 |         self.net.append(LoRACompatibleLinear(inner_dim, dim_out))
127 |         # FF as used in Vision Transformer, MLP-Mixer, etc. have a final dropout
128 |         if final_dropout:
129 |             self.net.append(nn.Dropout(dropout))
130 | 
131 |     def forward(self, hidden_states):
132 |         for module in self.net:
133 |             hidden_states = module(hidden_states)
134 |         return hidden_states
135 | 
136 | 
137 | @maybe_allow_in_graph
138 | class BasicTransformerBlock(nn.Module):
139 |     r"""
140 |     A basic Transformer block.
141 | 
142 |     Parameters:
143 |         dim (`int`): The number of channels in the input and output.
144 |         num_attention_heads (`int`): The number of heads to use for multi-head attention.
145 |         attention_head_dim (`int`): The number of channels in each head.
146 |         dropout (`float`, *optional*, defaults to 0.0): The dropout probability to use.
147 |         cross_attention_dim (`int`, *optional*): The size of the encoder_hidden_states vector for cross attention.
148 |         only_cross_attention (`bool`, *optional*):
149 |             Whether to use only cross-attention layers. In this case two cross attention layers are used.
150 |         double_self_attention (`bool`, *optional*):
151 |             Whether to use two self-attention layers. In this case no cross attention layers are used.
152 |         activation_fn (`str`, *optional*, defaults to `"geglu"`): Activation function to be used in feed-forward.
153 |         num_embeds_ada_norm (:
154 |             obj: `int`, *optional*): The number of diffusion steps used during training. See `Transformer2DModel`.
155 |         attention_bias (:
156 |             obj: `bool`, *optional*, defaults to `False`): Configure if the attentions should contain a bias parameter.
157 |     """
158 | 
159 |     def __init__(
160 |         self,
161 |         dim: int,
162 |         num_attention_heads: int,
163 |         attention_head_dim: int,
164 |         dropout=0.0,
165 |         cross_attention_dim: Optional[int] = None,
166 |         activation_fn: str = "geglu",
167 |         num_embeds_ada_norm: Optional[int] = None,
168 |         attention_bias: bool = False,
169 |         only_cross_attention: bool = False,
170 |         double_self_attention: bool = False,
171 |         upcast_attention: bool = False,
172 |         norm_elementwise_affine: bool = True,
173 |         norm_type: str = "layer_norm",
174 |         final_dropout: bool = False,
175 |     ):
176 |         super().__init__()
177 |         self.only_cross_attention = only_cross_attention
178 | 
179 |         self.use_ada_layer_norm_zero = (num_embeds_ada_norm is not None) and norm_type == "ada_norm_zero"
180 |         self.use_ada_layer_norm = (num_embeds_ada_norm is not None) and norm_type == "ada_norm"
181 | 
182 |         if norm_type in ("ada_norm", "ada_norm_zero") and num_embeds_ada_norm is None:
183 |             raise ValueError(
184 |                 f"`norm_type` is set to {norm_type}, but `num_embeds_ada_norm` is not defined. Please make sure to"
185 |                 f" define `num_embeds_ada_norm` if setting `norm_type` to {norm_type}."
186 |             )
187 | 
188 |         # Define 3 blocks. Each block has its own normalization layer.
189 |         # 1. Self-Attn
190 |         if self.use_ada_layer_norm:
191 |             self.norm1 = AdaLayerNorm(dim, num_embeds_ada_norm)
192 |         elif self.use_ada_layer_norm_zero:
193 |             self.norm1 = AdaLayerNormZero(dim, num_embeds_ada_norm)
194 |         else:
195 |             self.norm1 = nn.LayerNorm(dim, elementwise_affine=norm_elementwise_affine)
196 |         self.attn1 = Attention(
197 |             query_dim=dim,
198 |             heads=num_attention_heads,
199 |             dim_head=attention_head_dim,
200 |             dropout=dropout,
201 |             bias=attention_bias,
202 |             cross_attention_dim=cross_attention_dim if only_cross_attention else None,
203 |             upcast_attention=upcast_attention,
204 |         )
205 | 
206 |         # 2. Cross-Attn
207 |         if cross_attention_dim is not None or double_self_attention:
208 |             # We currently only use AdaLayerNormZero for self attention where there will only be one attention block.
209 |             # I.e. the number of returned modulation chunks from AdaLayerZero would not make sense if returned during
210 |             # the second cross attention block.
211 |             self.norm2 = (
212 |                 AdaLayerNorm(dim, num_embeds_ada_norm)
213 |                 if self.use_ada_layer_norm
214 |                 else nn.LayerNorm(dim, elementwise_affine=norm_elementwise_affine)
215 |             )
216 |             self.attn2 = Attention(
217 |                 query_dim=dim,
218 |                 cross_attention_dim=cross_attention_dim if not double_self_attention else None,
219 |                 heads=num_attention_heads,
220 |                 dim_head=attention_head_dim,
221 |                 dropout=dropout,
222 |                 bias=attention_bias,
223 |                 upcast_attention=upcast_attention,
224 |                 # scale_qk=False, # uncomment this to not to use flash attention
225 |             )  # is self-attn if encoder_hidden_states is none
226 |         else:
227 |             self.norm2 = None
228 |             self.attn2 = None
229 | 
230 |         # 3. Feed-forward
231 |         self.norm3 = nn.LayerNorm(dim, elementwise_affine=norm_elementwise_affine)
232 |         self.ff = FeedForward(dim, dropout=dropout, activation_fn=activation_fn, final_dropout=final_dropout)
233 | 
234 |         # let chunk size default to None
235 |         self._chunk_size = None
236 |         self._chunk_dim = 0
237 | 
238 |     def set_chunk_feed_forward(self, chunk_size: Optional[int], dim: int):
239 |         # Sets chunk feed-forward
240 |         self._chunk_size = chunk_size
241 |         self._chunk_dim = dim
242 | 
243 |     def forward(
244 |         self,
245 |         hidden_states: torch.FloatTensor,
246 |         attention_mask: Optional[torch.FloatTensor] = None,
247 |         encoder_hidden_states: Optional[torch.FloatTensor] = None,
248 |         encoder_attention_mask: Optional[torch.FloatTensor] = None,
249 |         timestep: Optional[torch.LongTensor] = None,
250 |         cross_attention_kwargs: Dict[str, Any] = None,
251 |         class_labels: Optional[torch.LongTensor] = None,
252 |     ):
253 |         # Notice that normalization is always applied before the real computation in the following blocks.
254 |         # 1. Self-Attention
255 |         if self.use_ada_layer_norm:
256 |             norm_hidden_states = self.norm1(hidden_states, timestep)
257 |         elif self.use_ada_layer_norm_zero:
258 |             norm_hidden_states, gate_msa, shift_mlp, scale_mlp, gate_mlp = self.norm1(
259 |                 hidden_states, timestep, class_labels, hidden_dtype=hidden_states.dtype
260 |             )
261 |         else:
262 |             norm_hidden_states = self.norm1(hidden_states)
263 | 
264 |         cross_attention_kwargs = cross_attention_kwargs if cross_attention_kwargs is not None else {}
265 | 
266 |         attn_output = self.attn1(
267 |             norm_hidden_states,
268 |             encoder_hidden_states=encoder_hidden_states if self.only_cross_attention else None,
269 |             attention_mask=encoder_attention_mask if self.only_cross_attention else attention_mask,
270 |             **cross_attention_kwargs,
271 |         )
272 |         if self.use_ada_layer_norm_zero:
273 |             attn_output = gate_msa.unsqueeze(1) * attn_output
274 |         hidden_states = attn_output + hidden_states
275 | 
276 |         # 2. Cross-Attention
277 |         if self.attn2 is not None:
278 |             norm_hidden_states = (
279 |                 self.norm2(hidden_states, timestep) if self.use_ada_layer_norm else self.norm2(hidden_states)
280 |             )
281 | 
282 |             attn_output = self.attn2(
283 |                 norm_hidden_states,
284 |                 encoder_hidden_states=encoder_hidden_states,
285 |                 attention_mask=encoder_attention_mask,
286 |                 **cross_attention_kwargs,
287 |             )
288 |             hidden_states = attn_output + hidden_states
289 | 
290 |         # 3. Feed-forward
291 |         norm_hidden_states = self.norm3(hidden_states)
292 | 
293 |         if self.use_ada_layer_norm_zero:
294 |             norm_hidden_states = norm_hidden_states * (1 + scale_mlp[:, None]) + shift_mlp[:, None]
295 | 
296 |         if self._chunk_size is not None:
297 |             # "feed_forward_chunk_size" can be used to save memory
298 |             if norm_hidden_states.shape[self._chunk_dim] % self._chunk_size != 0:
299 |                 raise ValueError(
300 |                     f"`hidden_states` dimension to be chunked: {norm_hidden_states.shape[self._chunk_dim]} has to be divisible by chunk size: {self._chunk_size}. Make sure to set an appropriate `chunk_size` when calling `unet.enable_forward_chunking`."
301 |                 )
302 | 
303 |             num_chunks = norm_hidden_states.shape[self._chunk_dim] // self._chunk_size
304 |             ff_output = torch.cat(
305 |                 [self.ff(hid_slice) for hid_slice in norm_hidden_states.chunk(num_chunks, dim=self._chunk_dim)],
306 |                 dim=self._chunk_dim,
307 |             )
308 |         else:
309 |             ff_output = self.ff(norm_hidden_states)
310 | 
311 |         if self.use_ada_layer_norm_zero:
312 |             ff_output = gate_mlp.unsqueeze(1) * ff_output
313 | 
314 |         hidden_states = ff_output + hidden_states
315 | 
316 |         return hidden_states
317 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/s3gen.py:
--------------------------------------------------------------------------------
  1 | # Modified from CosyVoice https://github.com/FunAudioLLM/CosyVoice
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | 
 15 | import logging
 16 | 
 17 | import numpy as np
 18 | import torch
 19 | import torchaudio as ta
 20 | from functools import lru_cache
 21 | from typing import Optional
 22 | 
 23 | from ..s3tokenizer import S3_SR, SPEECH_VOCAB_SIZE, S3Tokenizer
 24 | from .const import S3GEN_SR
 25 | from .flow import CausalMaskedDiffWithXvec
 26 | from .xvector import CAMPPlus
 27 | from .utils.mel import mel_spectrogram
 28 | from .f0_predictor import ConvRNNF0Predictor
 29 | from .hifigan import HiFTGenerator
 30 | from .transformer.upsample_encoder import UpsampleConformerEncoder
 31 | from .flow_matching import CausalConditionalCFM
 32 | from .decoder import ConditionalDecoder
 33 | from .configs import CFM_PARAMS
 34 | 
 35 | 
 36 | def drop_invalid_tokens(x):
 37 |     assert len(x.shape) <= 2 and x.shape[0] == 1, "only batch size of one allowed for now"
 38 |     return x[x < SPEECH_VOCAB_SIZE]
 39 | 
 40 | 
 41 | # TODO: global resampler cache
 42 | @lru_cache(100)
 43 | def get_resampler(src_sr, dst_sr, device):
 44 |     return ta.transforms.Resample(src_sr, dst_sr).to(device)
 45 | 
 46 | 
 47 | class S3Token2Mel(torch.nn.Module):
 48 |     """
 49 |     CosyVoice2's CFM decoder maps S3 speech tokens to mel-spectrograms.
 50 | 
 51 |     TODO: make these modules configurable?
 52 |     """
 53 |     def __init__(self):
 54 |         super().__init__()
 55 |         self.tokenizer = S3Tokenizer("speech_tokenizer_v2_25hz")
 56 |         self.mel_extractor = mel_spectrogram # TODO: make it a torch module?
 57 |         self.speaker_encoder = CAMPPlus()  # use default args
 58 | 
 59 |         encoder = UpsampleConformerEncoder(
 60 |             output_size=512,
 61 |             attention_heads=8,
 62 |             linear_units=2048,
 63 |             num_blocks=6,
 64 |             dropout_rate=0.1,
 65 |             positional_dropout_rate=0.1,
 66 |             attention_dropout_rate=0.1,
 67 |             normalize_before=True,
 68 |             input_layer='linear',
 69 |             pos_enc_layer_type='rel_pos_espnet',
 70 |             selfattention_layer_type='rel_selfattn',
 71 |             input_size=512,
 72 |             use_cnn_module=False,
 73 |             macaron_style=False,
 74 |         )
 75 | 
 76 |         estimator = ConditionalDecoder(
 77 |             in_channels=320,
 78 |             out_channels=80,
 79 |             causal=True,
 80 |             channels=[256],
 81 |             dropout=0.0,
 82 |             attention_head_dim=64,
 83 |             n_blocks=4,
 84 |             num_mid_blocks=12,
 85 |             num_heads=8,
 86 |             act_fn='gelu',
 87 |         )
 88 |         cfm_params = CFM_PARAMS
 89 |         decoder = CausalConditionalCFM(
 90 |             spk_emb_dim=80,
 91 |             cfm_params=cfm_params,
 92 |             estimator=estimator,
 93 |         )
 94 | 
 95 |         self.flow = CausalMaskedDiffWithXvec(
 96 |             encoder=encoder,
 97 |             decoder=decoder
 98 |         )
 99 | 
100 |         self.resamplers = {}
101 | 
102 |     @property
103 |     def device(self):
104 |         params = self.tokenizer.parameters()
105 |         return next(params).device
106 | 
107 |     def embed_ref(
108 |         self,
109 |         ref_wav: torch.Tensor,
110 |         ref_sr: int,
111 |         device="auto",
112 |         ref_fade_out=True,
113 |     ):
114 |         device = self.device if device == "auto" else device
115 |         if isinstance(ref_wav, np.ndarray):
116 |             ref_wav = torch.from_numpy(ref_wav).float()
117 | 
118 |         if ref_wav.device != device:
119 |             ref_wav = ref_wav.to(device)
120 | 
121 |         if len(ref_wav.shape) == 1:
122 |             ref_wav = ref_wav.unsqueeze(0)  # (B, L)
123 | 
124 |         if ref_wav.size(1) > 10 * ref_sr:
125 |             print("WARNING: cosydec received ref longer than 10s")
126 | 
127 |         ref_wav_24 = ref_wav
128 |         if ref_sr != S3GEN_SR:
129 |             ref_wav_24 = get_resampler(ref_sr, S3GEN_SR, device)(ref_wav)
130 | 
131 |         ref_mels_24 = self.mel_extractor(ref_wav_24).transpose(1, 2).to(device)
132 |         ref_mels_24_len = None
133 | 
134 |         # Resample to 16kHz
135 |         ref_wav_16 = get_resampler(ref_sr, S3_SR, device)(ref_wav).to(device)
136 | 
137 |         # Speaker embedding
138 |         ref_x_vector = self.speaker_encoder.inference(ref_wav_16)
139 | 
140 |         # Tokenize 16khz reference
141 |         ref_speech_tokens, ref_speech_token_lens = self.tokenizer(ref_wav_16)
142 | 
143 |         # Make sure mel_len = 2 * stoken_len (happens when the input is not padded to multiple of 40ms)
144 |         if ref_mels_24.shape[1] != 2 * ref_speech_tokens.shape[1]:
145 |             logging.warning(
146 |                 "Reference mel length is not equal to 2 * reference token length.\n"
147 |             )
148 |             ref_speech_tokens = ref_speech_tokens[:, :ref_mels_24.shape[1] // 2]
149 |             ref_speech_token_lens[0] = ref_speech_tokens.shape[1]
150 | 
151 |         return dict(
152 |             prompt_token=ref_speech_tokens.to(device),
153 |             prompt_token_len=ref_speech_token_lens,
154 |             prompt_feat=ref_mels_24,
155 |             prompt_feat_len=ref_mels_24_len,
156 |             embedding=ref_x_vector,
157 |         )
158 | 
159 |     def forward(
160 |         self,
161 |         speech_tokens: torch.LongTensor,
162 |         # locally-computed ref embedding (mutex with ref_dict)
163 |         ref_wav: Optional[torch.Tensor],
164 |         ref_sr: Optional[int],
165 |         # pre-computed ref embedding (prod API)
166 |         ref_dict: Optional[dict] = None,
167 |         finalize: bool = False,
168 |     ):
169 |         """
170 |         Generate waveforms from S3 speech tokens and a reference waveform, which the speaker timbre is inferred from.
171 | 
172 |         NOTE:
173 |         - The speaker encoder accepts 16 kHz waveform.
174 |         - S3TokenizerV2 accepts 16 kHz waveform.
175 |         - The mel-spectrogram for the reference assumes 24 kHz input signal.
176 |         - This function is designed for batch_size=1 only.
177 | 
178 |         Args
179 |         ----
180 |         - `speech_tokens`: S3 speech tokens [B=1, T]
181 |         - `ref_wav`: reference waveform (`torch.Tensor` with shape=[B=1, T])
182 |         - `ref_sr`: reference sample rate
183 |         - `finalize`: whether streaming is finished or not. Note that if False, the last 3 tokens will be ignored.
184 |         """
185 |         assert (ref_wav is None) ^ (ref_dict is None), f"Must provide exactly one of ref_wav or ref_dict (got {ref_wav} and {ref_dict})"
186 | 
187 |         if ref_dict is None:
188 |             ref_dict = self.embed_ref(ref_wav, ref_sr)
189 |         else:
190 |             # type/device casting (all values will be numpy if it's from a prod API call)
191 |             for rk in list(ref_dict):
192 |                 if isinstance(ref_dict[rk], np.ndarray):
193 |                     ref_dict[rk] = torch.from_numpy(ref_dict[rk])
194 |                 if torch.is_tensor(ref_dict[rk]):
195 |                     ref_dict[rk] = ref_dict[rk].to(self.device)
196 | 
197 |         if len(speech_tokens.shape) == 1:
198 |             speech_tokens = speech_tokens.unsqueeze(0)
199 | 
200 |         # assert speech_tokens.shape[0] == 1, "only batch size of one allowed for now"
201 |         speech_token_lens = torch.LongTensor([speech_tokens.size(1)]).to(self.device)
202 | 
203 |         output_mels, _ = self.flow.inference(
204 |             token=speech_tokens,
205 |             token_len=speech_token_lens,
206 |             finalize=finalize,
207 |             **ref_dict,
208 |         )
209 |         return output_mels
210 | 
211 | 
212 | class S3Token2Wav(S3Token2Mel):
213 |     """
214 |     The decoder of CosyVoice2 is a concat of token-to-mel (CFM) and a mel-to-waveform (HiFiGAN) modules.
215 | 
216 |     TODO: make these modules configurable?
217 |     """
218 | 
219 |     def __init__(self):
220 |         super().__init__()
221 | 
222 |         f0_predictor = ConvRNNF0Predictor()
223 |         self.mel2wav = HiFTGenerator(
224 |             sampling_rate=S3GEN_SR,
225 |             upsample_rates=[8, 5, 3],
226 |             upsample_kernel_sizes=[16, 11, 7],
227 |             source_resblock_kernel_sizes=[7, 7, 11],
228 |             source_resblock_dilation_sizes=[[1, 3, 5], [1, 3, 5], [1, 3, 5]],
229 |             f0_predictor=f0_predictor,
230 |         )
231 | 
232 |         # silence out a few ms and fade audio in to reduce artifacts
233 |         n_trim = S3GEN_SR // 50  # 20ms = half of a frame
234 |         trim_fade = torch.zeros(2 * n_trim)
235 |         trim_fade[n_trim:] = (torch.cos(torch.linspace(torch.pi, 0, n_trim)) + 1) / 2
236 |         self.register_buffer("trim_fade", trim_fade, persistent=False) # (buffers get automatic device casting)
237 | 
238 |     def forward(
239 |         self,
240 |         speech_tokens,
241 |         # locally-computed ref embedding (mutex with ref_dict)
242 |         ref_wav: Optional[torch.Tensor],
243 |         ref_sr: Optional[int],
244 |         # pre-computed ref embedding (prod API)
245 |         ref_dict: Optional[dict] = None,
246 |         finalize: bool = False
247 |     ):
248 |         output_mels = super().forward(speech_tokens, ref_wav=ref_wav, ref_sr=ref_sr, ref_dict=ref_dict, finalize=finalize)
249 | 
250 |         # TODO jrm: ignoring the speed control (mel interpolation) and the HiFTGAN caching mechanisms for now.
251 |         hift_cache_source = torch.zeros(1, 1, 0).to(self.device)
252 | 
253 |         output_wavs, *_ = self.mel2wav.inference(speech_feat=output_mels, cache_source=hift_cache_source)
254 | 
255 |         if not self.training:
256 |             # NOTE: ad-hoc method to reduce "spillover" from the reference clip.
257 |             output_wavs[:, :len(self.trim_fade)] *= self.trim_fade
258 | 
259 |         return output_wavs
260 | 
261 |     @torch.inference_mode()
262 |     def flow_inference(
263 |         self,
264 |         speech_tokens,
265 |         # locally-computed ref embedding (mutex with ref_dict)
266 |         ref_wav: Optional[torch.Tensor] = None,
267 |         ref_sr: Optional[int] = None,
268 |         # pre-computed ref embedding (prod API)
269 |         ref_dict: Optional[dict] = None,
270 |         finalize: bool = False,
271 |     ):
272 |         return super().forward(speech_tokens, ref_wav=ref_wav, ref_sr=ref_sr, ref_dict=ref_dict, finalize=finalize)
273 | 
274 |     @torch.inference_mode()
275 |     def hift_inference(self, speech_feat, cache_source: torch.Tensor = None):
276 |         if cache_source is None:
277 |             cache_source = torch.zeros(1, 1, 0).to(self.device)
278 |         return self.mel2wav.inference(speech_feat=speech_feat, cache_source=cache_source)
279 | 
280 |     @torch.inference_mode()
281 |     def inference(
282 |         self,
283 |         speech_tokens,
284 |         # locally-computed ref embedding (mutex with ref_dict)
285 |         ref_wav: Optional[torch.Tensor] = None,
286 |         ref_sr: Optional[int] = None,
287 |         # pre-computed ref embedding (prod API)
288 |         ref_dict: Optional[dict] = None,
289 |         cache_source: torch.Tensor = None, # NOTE: this arg is for streaming, it can probably be removed here
290 |         finalize: bool = True,
291 |     ):
292 |         output_mels = self.flow_inference(speech_tokens, ref_wav=ref_wav, ref_sr=ref_sr, ref_dict=ref_dict, finalize=finalize)
293 |         output_wavs, output_sources = self.hift_inference(output_mels, cache_source)
294 | 
295 |         # NOTE: ad-hoc method to reduce "spillover" from the reference clip.
296 |         output_wavs[:, :len(self.trim_fade)] *= self.trim_fade
297 | 
298 |         return output_wavs, output_sources
299 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/resemble-ai/chatterbox/eb90621fa748f341a5b768aed0c0c12fc561894b/src/chatterbox/models/s3gen/transformer/__init__.py


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/activation.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) 2020 Johns Hopkins University (Shinji Watanabe)
 2 | #               2020 Northwestern Polytechnical University (Pengcheng Guo)
 3 | #               2020 Mobvoi Inc (Binbin Zhang)
 4 | #               2024 Alibaba Inc (Xiang Lyu)
 5 | #
 6 | # Licensed under the Apache License, Version 2.0 (the "License");
 7 | # you may not use this file except in compliance with the License.
 8 | # You may obtain a copy of the License at
 9 | #
10 | #   http://www.apache.org/licenses/LICENSE-2.0
11 | #
12 | # Unless required by applicable law or agreed to in writing, software
13 | # distributed under the License is distributed on an "AS IS" BASIS,
14 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
15 | # See the License for the specific language governing permissions and
16 | # limitations under the License.
17 | """Swish() activation function for Conformer."""
18 | 
19 | import torch
20 | from torch import nn, sin, pow
21 | from torch.nn import Parameter
22 | 
23 | 
24 | class Swish(torch.nn.Module):
25 |     """Construct an Swish object."""
26 | 
27 |     def forward(self, x: torch.Tensor) -> torch.Tensor:
28 |         """Return Swish activation function."""
29 |         return x * torch.sigmoid(x)
30 | 
31 | 
32 | # Implementation adapted from https://github.com/EdwardDixon/snake under the MIT license.
33 | #   LICENSE is in incl_licenses directory.
34 | class Snake(nn.Module):
35 |     '''
36 |     Implementation of a sine-based periodic activation function
37 |     Shape:
38 |         - Input: (B, C, T)
39 |         - Output: (B, C, T), same shape as the input
40 |     Parameters:
41 |         - alpha - trainable parameter
42 |     References:
43 |         - This activation function is from this paper by Liu Ziyin, Tilman Hartwig, Masahito Ueda:
44 |         https://arxiv.org/abs/2006.08195
45 |     Examples:
46 |         >>> a1 = snake(256)
47 |         >>> x = torch.randn(256)
48 |         >>> x = a1(x)
49 |     '''
50 |     def __init__(self, in_features, alpha=1.0, alpha_trainable=True, alpha_logscale=False):
51 |         '''
52 |         Initialization.
53 |         INPUT:
54 |             - in_features: shape of the input
55 |             - alpha: trainable parameter
56 |             alpha is initialized to 1 by default, higher values = higher-frequency.
57 |             alpha will be trained along with the rest of your model.
58 |         '''
59 |         super(Snake, self).__init__()
60 |         self.in_features = in_features
61 | 
62 |         # initialize alpha
63 |         self.alpha_logscale = alpha_logscale
64 |         if self.alpha_logscale:  # log scale alphas initialized to zeros
65 |             self.alpha = Parameter(torch.zeros(in_features) * alpha)
66 |         else:  # linear scale alphas initialized to ones
67 |             self.alpha = Parameter(torch.ones(in_features) * alpha)
68 | 
69 |         self.alpha.requires_grad = alpha_trainable
70 | 
71 |         self.no_div_by_zero = 0.000000001
72 | 
73 |     def forward(self, x):
74 |         '''
75 |         Forward pass of the function.
76 |         Applies the function to the input elementwise.
77 |         Snake ∶= x + 1/a * sin^2 (xa)
78 |         '''
79 |         alpha = self.alpha.unsqueeze(0).unsqueeze(-1)  # line up with x to [B, C, T]
80 |         if self.alpha_logscale:
81 |             alpha = torch.exp(alpha)
82 |         x = x + (1.0 / (alpha + self.no_div_by_zero)) * pow(sin(x * alpha), 2)
83 | 
84 |         return x
85 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/convolution.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2020 Mobvoi Inc. (authors: Binbin Zhang, Di Wu)
  2 | #               2024 Alibaba Inc (Xiang Lyu)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #     http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """ConvolutionModule definition."""
 17 | 
 18 | from typing import Tuple
 19 | 
 20 | import torch
 21 | from torch import nn
 22 | 
 23 | 
 24 | class ConvolutionModule(nn.Module):
 25 |     """ConvolutionModule in Conformer model."""
 26 | 
 27 |     def __init__(self,
 28 |                  channels: int,
 29 |                  kernel_size: int = 15,
 30 |                  activation: nn.Module = nn.ReLU(),
 31 |                  norm: str = "batch_norm",
 32 |                  causal: bool = False,
 33 |                  bias: bool = True):
 34 |         """Construct an ConvolutionModule object.
 35 |         Args:
 36 |             channels (int): The number of channels of conv layers.
 37 |             kernel_size (int): Kernel size of conv layers.
 38 |             causal (int): Whether use causal convolution or not
 39 |         """
 40 |         super().__init__()
 41 | 
 42 |         self.pointwise_conv1 = nn.Conv1d(
 43 |             channels,
 44 |             2 * channels,
 45 |             kernel_size=1,
 46 |             stride=1,
 47 |             padding=0,
 48 |             bias=bias,
 49 |         )
 50 |         # self.lorder is used to distinguish if it's a causal convolution,
 51 |         # if self.lorder > 0: it's a causal convolution, the input will be
 52 |         #    padded with self.lorder frames on the left in forward.
 53 |         # else: it's a symmetrical convolution
 54 |         if causal:
 55 |             padding = 0
 56 |             self.lorder = kernel_size - 1
 57 |         else:
 58 |             # kernel_size should be an odd number for none causal convolution
 59 |             assert (kernel_size - 1) % 2 == 0
 60 |             padding = (kernel_size - 1) // 2
 61 |             self.lorder = 0
 62 |         self.depthwise_conv = nn.Conv1d(
 63 |             channels,
 64 |             channels,
 65 |             kernel_size,
 66 |             stride=1,
 67 |             padding=padding,
 68 |             groups=channels,
 69 |             bias=bias,
 70 |         )
 71 | 
 72 |         assert norm in ['batch_norm', 'layer_norm']
 73 |         if norm == "batch_norm":
 74 |             self.use_layer_norm = False
 75 |             self.norm = nn.BatchNorm1d(channels)
 76 |         else:
 77 |             self.use_layer_norm = True
 78 |             self.norm = nn.LayerNorm(channels)
 79 | 
 80 |         self.pointwise_conv2 = nn.Conv1d(
 81 |             channels,
 82 |             channels,
 83 |             kernel_size=1,
 84 |             stride=1,
 85 |             padding=0,
 86 |             bias=bias,
 87 |         )
 88 |         self.activation = activation
 89 | 
 90 |     def forward(
 91 |         self,
 92 |         x: torch.Tensor,
 93 |         mask_pad: torch.Tensor = torch.ones((0, 0, 0), dtype=torch.bool),
 94 |         cache: torch.Tensor = torch.zeros((0, 0, 0)),
 95 |     ) -> Tuple[torch.Tensor, torch.Tensor]:
 96 |         """Compute convolution module.
 97 |         Args:
 98 |             x (torch.Tensor): Input tensor (#batch, time, channels).
 99 |             mask_pad (torch.Tensor): used for batch padding (#batch, 1, time),
100 |                 (0, 0, 0) means fake mask.
101 |             cache (torch.Tensor): left context cache, it is only
102 |                 used in causal convolution (#batch, channels, cache_t),
103 |                 (0, 0, 0) meas fake cache.
104 |         Returns:
105 |             torch.Tensor: Output tensor (#batch, time, channels).
106 |         """
107 |         # exchange the temporal dimension and the feature dimension
108 |         x = x.transpose(1, 2)  # (#batch, channels, time)
109 | 
110 |         # mask batch padding
111 |         if mask_pad.size(2) > 0:  # time > 0
112 |             x.masked_fill_(~mask_pad, 0.0)
113 | 
114 |         if self.lorder > 0:
115 |             if cache.size(2) == 0:  # cache_t == 0
116 |                 x = nn.functional.pad(x, (self.lorder, 0), 'constant', 0.0)
117 |             else:
118 |                 assert cache.size(0) == x.size(0)  # equal batch
119 |                 assert cache.size(1) == x.size(1)  # equal channel
120 |                 x = torch.cat((cache, x), dim=2)
121 |             assert (x.size(2) > self.lorder)
122 |             new_cache = x[:, :, -self.lorder:]
123 |         else:
124 |             # It's better we just return None if no cache is required,
125 |             # However, for JIT export, here we just fake one tensor instead of
126 |             # None.
127 |             new_cache = torch.zeros((0, 0, 0), dtype=x.dtype, device=x.device)
128 | 
129 |         # GLU mechanism
130 |         x = self.pointwise_conv1(x)  # (batch, 2*channel, dim)
131 |         x = nn.functional.glu(x, dim=1)  # (batch, channel, dim)
132 | 
133 |         # 1D Depthwise Conv
134 |         x = self.depthwise_conv(x)
135 |         if self.use_layer_norm:
136 |             x = x.transpose(1, 2)
137 |         x = self.activation(self.norm(x))
138 |         if self.use_layer_norm:
139 |             x = x.transpose(1, 2)
140 |         x = self.pointwise_conv2(x)
141 |         # mask batch padding
142 |         if mask_pad.size(2) > 0:  # time > 0
143 |             x.masked_fill_(~mask_pad, 0.0)
144 | 
145 |         return x.transpose(1, 2), new_cache
146 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/embedding.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2020 Mobvoi Inc. (authors: Binbin Zhang, Di Wu)
  2 | #               2024 Alibaba Inc (Xiang Lyu)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #     http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """Positonal Encoding Module."""
 17 | 
 18 | import math
 19 | from typing import Tuple, Union
 20 | 
 21 | import torch
 22 | import torch.nn.functional as F
 23 | import numpy as np
 24 | 
 25 | 
 26 | class PositionalEncoding(torch.nn.Module):
 27 |     """Positional encoding.
 28 | 
 29 |     :param int d_model: embedding dim
 30 |     :param float dropout_rate: dropout rate
 31 |     :param int max_len: maximum input length
 32 | 
 33 |     PE(pos, 2i)   = sin(pos/(10000^(2i/dmodel)))
 34 |     PE(pos, 2i+1) = cos(pos/(10000^(2i/dmodel)))
 35 |     """
 36 | 
 37 |     def __init__(self,
 38 |                  d_model: int,
 39 |                  dropout_rate: float,
 40 |                  max_len: int = 5000,
 41 |                  reverse: bool = False):
 42 |         """Construct an PositionalEncoding object."""
 43 |         super().__init__()
 44 |         self.d_model = d_model
 45 |         self.xscale = math.sqrt(self.d_model)
 46 |         self.dropout = torch.nn.Dropout(p=dropout_rate)
 47 |         self.max_len = max_len
 48 | 
 49 |         self.pe = torch.zeros(self.max_len, self.d_model)
 50 |         position = torch.arange(0, self.max_len,
 51 |                                 dtype=torch.float32).unsqueeze(1)
 52 |         div_term = torch.exp(
 53 |             torch.arange(0, self.d_model, 2, dtype=torch.float32) *
 54 |             -(math.log(10000.0) / self.d_model))
 55 |         self.pe[:, 0::2] = torch.sin(position * div_term)
 56 |         self.pe[:, 1::2] = torch.cos(position * div_term)
 57 |         self.pe = self.pe.unsqueeze(0)
 58 | 
 59 |     def forward(self,
 60 |                 x: torch.Tensor,
 61 |                 offset: Union[int, torch.Tensor] = 0) \
 62 |             -> Tuple[torch.Tensor, torch.Tensor]:
 63 |         """Add positional encoding.
 64 | 
 65 |         Args:
 66 |             x (torch.Tensor): Input. Its shape is (batch, time, ...)
 67 |             offset (int, torch.tensor): position offset
 68 | 
 69 |         Returns:
 70 |             torch.Tensor: Encoded tensor. Its shape is (batch, time, ...)
 71 |             torch.Tensor: for compatibility to RelPositionalEncoding
 72 |         """
 73 | 
 74 |         self.pe = self.pe.to(x.device)
 75 |         pos_emb = self.position_encoding(offset, x.size(1), False)
 76 |         x = x * self.xscale + pos_emb
 77 |         return self.dropout(x), self.dropout(pos_emb)
 78 | 
 79 |     def position_encoding(self,
 80 |                           offset: Union[int, torch.Tensor],
 81 |                           size: int,
 82 |                           apply_dropout: bool = True) -> torch.Tensor:
 83 |         """ For getting encoding in a streaming fashion
 84 | 
 85 |         Attention!!!!!
 86 |         we apply dropout only once at the whole utterance level in a none
 87 |         streaming way, but will call this function several times with
 88 |         increasing input size in a streaming scenario, so the dropout will
 89 |         be applied several times.
 90 | 
 91 |         Args:
 92 |             offset (int or torch.tensor): start offset
 93 |             size (int): required size of position encoding
 94 | 
 95 |         Returns:
 96 |             torch.Tensor: Corresponding encoding
 97 |         """
 98 |         # How to subscript a Union type:
 99 |         #   https://github.com/pytorch/pytorch/issues/69434
100 |         if isinstance(offset, int):
101 |             assert offset + size <= self.max_len
102 |             pos_emb = self.pe[:, offset:offset + size]
103 |         elif isinstance(offset, torch.Tensor) and offset.dim() == 0:  # scalar
104 |             assert offset + size <= self.max_len
105 |             pos_emb = self.pe[:, offset:offset + size]
106 |         else:  # for batched streaming decoding on GPU
107 |             assert torch.max(offset) + size <= self.max_len
108 |             index = offset.unsqueeze(1) + \
109 |                 torch.arange(0, size).to(offset.device)  # B X T
110 |             flag = index > 0
111 |             # remove negative offset
112 |             index = index * flag
113 |             pos_emb = F.embedding(index, self.pe[0])  # B X T X d_model
114 | 
115 |         if apply_dropout:
116 |             pos_emb = self.dropout(pos_emb)
117 |         return pos_emb
118 | 
119 | 
120 | class RelPositionalEncoding(PositionalEncoding):
121 |     """Relative positional encoding module.
122 |     See : Appendix B in https://arxiv.org/abs/1901.02860
123 |     Args:
124 |         d_model (int): Embedding dimension.
125 |         dropout_rate (float): Dropout rate.
126 |         max_len (int): Maximum input length.
127 |     """
128 | 
129 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 5000):
130 |         """Initialize class."""
131 |         super().__init__(d_model, dropout_rate, max_len, reverse=True)
132 | 
133 |     def forward(self,
134 |                 x: torch.Tensor,
135 |                 offset: Union[int, torch.Tensor] = 0) \
136 |             -> Tuple[torch.Tensor, torch.Tensor]:
137 |         """Compute positional encoding.
138 |         Args:
139 |             x (torch.Tensor): Input tensor (batch, time, `*`).
140 |         Returns:
141 |             torch.Tensor: Encoded tensor (batch, time, `*`).
142 |             torch.Tensor: Positional embedding tensor (1, time, `*`).
143 |         """
144 |         self.pe = self.pe.to(x.device)
145 |         x = x * self.xscale
146 |         pos_emb = self.position_encoding(offset, x.size(1), False)
147 |         return self.dropout(x), self.dropout(pos_emb)
148 | 
149 | 
150 | class WhisperPositionalEncoding(PositionalEncoding):
151 |     """ Sinusoids position encoding used in openai-whisper.encoder
152 |     """
153 | 
154 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 1500):
155 |         super().__init__(d_model, dropout_rate, max_len)
156 |         self.xscale = 1.0
157 |         log_timescale_increment = np.log(10000) / (d_model // 2 - 1)
158 |         inv_timescales = torch.exp(-log_timescale_increment *
159 |                                    torch.arange(d_model // 2))
160 |         scaled_time = torch.arange(max_len)[:, np.newaxis] * \
161 |             inv_timescales[np.newaxis, :]
162 |         pe = torch.cat([torch.sin(scaled_time), torch.cos(scaled_time)], dim=1)
163 |         delattr(self, "pe")
164 |         self.register_buffer("pe", pe.unsqueeze(0))
165 | 
166 | 
167 | class LearnablePositionalEncoding(PositionalEncoding):
168 |     """ Learnable position encoding used in openai-whisper.decoder
169 |     """
170 | 
171 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 448):
172 |         super().__init__(d_model, dropout_rate, max_len)
173 |         # NOTE(xcsong): overwrite self.pe & self.xscale
174 |         self.pe = torch.nn.Parameter(torch.empty(1, max_len, d_model))
175 |         self.xscale = 1.0
176 | 
177 | 
178 | class NoPositionalEncoding(torch.nn.Module):
179 |     """ No position encoding
180 |     """
181 | 
182 |     def __init__(self, d_model: int, dropout_rate: float):
183 |         super().__init__()
184 |         self.d_model = d_model
185 |         self.dropout = torch.nn.Dropout(p=dropout_rate)
186 | 
187 |     def forward(self,
188 |                 x: torch.Tensor,
189 |                 offset: Union[int, torch.Tensor] = 0) \
190 |             -> Tuple[torch.Tensor, torch.Tensor]:
191 |         """ Just return zero vector for interface compatibility
192 |         """
193 |         pos_emb = torch.zeros(1, x.size(1), self.d_model).to(x.device)
194 |         return self.dropout(x), pos_emb
195 | 
196 |     def position_encoding(self, offset: Union[int, torch.Tensor],
197 |                           size: int) -> torch.Tensor:
198 |         return torch.zeros(1, size, self.d_model)
199 | 
200 | 
201 | class EspnetRelPositionalEncoding(torch.nn.Module):
202 |     """Relative positional encoding module (new implementation).
203 | 
204 |     Details can be found in https://github.com/espnet/espnet/pull/2816.
205 | 
206 |     See : Appendix B in https://arxiv.org/abs/1901.02860
207 | 
208 |     Args:
209 |         d_model (int): Embedding dimension.
210 |         dropout_rate (float): Dropout rate.
211 |         max_len (int): Maximum input length.
212 | 
213 |     """
214 | 
215 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 5000):
216 |         """Construct an PositionalEncoding object."""
217 |         super(EspnetRelPositionalEncoding, self).__init__()
218 |         self.d_model = d_model
219 |         self.xscale = math.sqrt(self.d_model)
220 |         self.dropout = torch.nn.Dropout(p=dropout_rate)
221 |         self.pe = None
222 |         self.extend_pe(torch.tensor(0.0).expand(1, max_len))
223 | 
224 |     def extend_pe(self, x: torch.Tensor):
225 |         """Reset the positional encodings."""
226 |         if self.pe is not None:
227 |             # self.pe contains both positive and negative parts
228 |             # the length of self.pe is 2 * input_len - 1
229 |             if self.pe.size(1) >= x.size(1) * 2 - 1:
230 |                 if self.pe.dtype != x.dtype or self.pe.device != x.device:
231 |                     self.pe = self.pe.to(dtype=x.dtype, device=x.device)
232 |                 return
233 |         # Suppose `i` means to the position of query vecotr and `j` means the
234 |         # position of key vector. We use position relative positions when keys
235 |         # are to the left (i>j) and negative relative positions otherwise (i<j).
236 |         pe_positive = torch.zeros(x.size(1), self.d_model)
237 |         pe_negative = torch.zeros(x.size(1), self.d_model)
238 |         position = torch.arange(0, x.size(1), dtype=torch.float32).unsqueeze(1)
239 |         div_term = torch.exp(
240 |             torch.arange(0, self.d_model, 2, dtype=torch.float32)
241 |             * -(math.log(10000.0) / self.d_model)
242 |         )
243 |         pe_positive[:, 0::2] = torch.sin(position * div_term)
244 |         pe_positive[:, 1::2] = torch.cos(position * div_term)
245 |         pe_negative[:, 0::2] = torch.sin(-1 * position * div_term)
246 |         pe_negative[:, 1::2] = torch.cos(-1 * position * div_term)
247 | 
248 |         # Reserve the order of positive indices and concat both positive and
249 |         # negative indices. This is used to support the shifting trick
250 |         # as in https://arxiv.org/abs/1901.02860
251 |         pe_positive = torch.flip(pe_positive, [0]).unsqueeze(0)
252 |         pe_negative = pe_negative[1:].unsqueeze(0)
253 |         pe = torch.cat([pe_positive, pe_negative], dim=1)
254 |         self.pe = pe.to(device=x.device, dtype=x.dtype)
255 | 
256 |     def forward(self, x: torch.Tensor, offset: Union[int, torch.Tensor] = 0) \
257 |             -> Tuple[torch.Tensor, torch.Tensor]:
258 |         """Add positional encoding.
259 | 
260 |         Args:
261 |             x (torch.Tensor): Input tensor (batch, time, `*`).
262 | 
263 |         Returns:
264 |             torch.Tensor: Encoded tensor (batch, time, `*`).
265 | 
266 |         """
267 |         self.extend_pe(x)
268 |         x = x * self.xscale
269 |         pos_emb = self.position_encoding(size=x.size(1), offset=offset)
270 |         return self.dropout(x), self.dropout(pos_emb)
271 | 
272 |     def position_encoding(self,
273 |                           offset: Union[int, torch.Tensor],
274 |                           size: int) -> torch.Tensor:
275 |         """ For getting encoding in a streaming fashion
276 | 
277 |         Attention!!!!!
278 |         we apply dropout only once at the whole utterance level in a none
279 |         streaming way, but will call this function several times with
280 |         increasing input size in a streaming scenario, so the dropout will
281 |         be applied several times.
282 | 
283 |         Args:
284 |             offset (int or torch.tensor): start offset
285 |             size (int): required size of position encoding
286 | 
287 |         Returns:
288 |             torch.Tensor: Corresponding encoding
289 |         """
290 |         pos_emb = self.pe[
291 |             :,
292 |             self.pe.size(1) // 2 - size + 1: self.pe.size(1) // 2 + size,
293 |         ]
294 |         return pos_emb
295 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/encoder_layer.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2021 Mobvoi Inc (Binbin Zhang, Di Wu)
  2 | #               2022 Xingchen Song (sxc19@mails.tsinghua.edu.cn)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #   http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """Encoder self-attention layer definition."""
 17 | 
 18 | from typing import Optional, Tuple
 19 | 
 20 | import torch
 21 | from torch import nn
 22 | 
 23 | 
 24 | class TransformerEncoderLayer(nn.Module):
 25 |     """Encoder layer module.
 26 | 
 27 |     Args:
 28 |         size (int): Input dimension.
 29 |         self_attn (torch.nn.Module): Self-attention module instance.
 30 |             `MultiHeadedAttention` or `RelPositionMultiHeadedAttention`
 31 |             instance can be used as the argument.
 32 |         feed_forward (torch.nn.Module): Feed-forward module instance.
 33 |             `PositionwiseFeedForward`, instance can be used as the argument.
 34 |         dropout_rate (float): Dropout rate.
 35 |         normalize_before (bool):
 36 |             True: use layer_norm before each sub-block.
 37 |             False: to use layer_norm after each sub-block.
 38 |     """
 39 | 
 40 |     def __init__(
 41 |         self,
 42 |         size: int,
 43 |         self_attn: torch.nn.Module,
 44 |         feed_forward: torch.nn.Module,
 45 |         dropout_rate: float,
 46 |         normalize_before: bool = True,
 47 |     ):
 48 |         """Construct an EncoderLayer object."""
 49 |         super().__init__()
 50 |         self.self_attn = self_attn
 51 |         self.feed_forward = feed_forward
 52 |         self.norm1 = nn.LayerNorm(size, eps=1e-12)
 53 |         self.norm2 = nn.LayerNorm(size, eps=1e-12)
 54 |         self.dropout = nn.Dropout(dropout_rate)
 55 |         self.size = size
 56 |         self.normalize_before = normalize_before
 57 | 
 58 |     def forward(
 59 |         self,
 60 |         x: torch.Tensor,
 61 |         mask: torch.Tensor,
 62 |         pos_emb: torch.Tensor,
 63 |         mask_pad: torch.Tensor = torch.ones((0, 0, 0), dtype=torch.bool),
 64 |         att_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
 65 |         cnn_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
 66 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
 67 |         """Compute encoded features.
 68 | 
 69 |         Args:
 70 |             x (torch.Tensor): (#batch, time, size)
 71 |             mask (torch.Tensor): Mask tensor for the input (#batch, time，time),
 72 |                 (0, 0, 0) means fake mask.
 73 |             pos_emb (torch.Tensor): just for interface compatibility
 74 |                 to ConformerEncoderLayer
 75 |             mask_pad (torch.Tensor): does not used in transformer layer,
 76 |                 just for unified api with conformer.
 77 |             att_cache (torch.Tensor): Cache tensor of the KEY & VALUE
 78 |                 (#batch=1, head, cache_t1, d_k * 2), head * d_k == size.
 79 |             cnn_cache (torch.Tensor): Convolution cache in conformer layer
 80 |                 (#batch=1, size, cache_t2), not used here, it's for interface
 81 |                 compatibility to ConformerEncoderLayer.
 82 |         Returns:
 83 |             torch.Tensor: Output tensor (#batch, time, size).
 84 |             torch.Tensor: Mask tensor (#batch, time, time).
 85 |             torch.Tensor: att_cache tensor,
 86 |                 (#batch=1, head, cache_t1 + time, d_k * 2).
 87 |             torch.Tensor: cnn_cahce tensor (#batch=1, size, cache_t2).
 88 | 
 89 |         """
 90 |         residual = x
 91 |         if self.normalize_before:
 92 |             x = self.norm1(x)
 93 |         x_att, new_att_cache = self.self_attn(x, x, x, mask, pos_emb=pos_emb, cache=att_cache)
 94 |         x = residual + self.dropout(x_att)
 95 |         if not self.normalize_before:
 96 |             x = self.norm1(x)
 97 | 
 98 |         residual = x
 99 |         if self.normalize_before:
100 |             x = self.norm2(x)
101 |         x = residual + self.dropout(self.feed_forward(x))
102 |         if not self.normalize_before:
103 |             x = self.norm2(x)
104 | 
105 |         fake_cnn_cache = torch.zeros((0, 0, 0), dtype=x.dtype, device=x.device)
106 |         return x, mask, new_att_cache, fake_cnn_cache
107 | 
108 | 
109 | class ConformerEncoderLayer(nn.Module):
110 |     """Encoder layer module.
111 |     Args:
112 |         size (int): Input dimension.
113 |         self_attn (torch.nn.Module): Self-attention module instance.
114 |             `MultiHeadedAttention` or `RelPositionMultiHeadedAttention`
115 |             instance can be used as the argument.
116 |         feed_forward (torch.nn.Module): Feed-forward module instance.
117 |             `PositionwiseFeedForward` instance can be used as the argument.
118 |         feed_forward_macaron (torch.nn.Module): Additional feed-forward module
119 |              instance.
120 |             `PositionwiseFeedForward` instance can be used as the argument.
121 |         conv_module (torch.nn.Module): Convolution module instance.
122 |             `ConvlutionModule` instance can be used as the argument.
123 |         dropout_rate (float): Dropout rate.
124 |         normalize_before (bool):
125 |             True: use layer_norm before each sub-block.
126 |             False: use layer_norm after each sub-block.
127 |     """
128 | 
129 |     def __init__(
130 |         self,
131 |         size: int,
132 |         self_attn: torch.nn.Module,
133 |         feed_forward: Optional[nn.Module] = None,
134 |         feed_forward_macaron: Optional[nn.Module] = None,
135 |         conv_module: Optional[nn.Module] = None,
136 |         dropout_rate: float = 0.1,
137 |         normalize_before: bool = True,
138 |     ):
139 |         """Construct an EncoderLayer object."""
140 |         super().__init__()
141 |         self.self_attn = self_attn
142 |         self.feed_forward = feed_forward
143 |         self.feed_forward_macaron = feed_forward_macaron
144 |         self.conv_module = conv_module
145 |         self.norm_ff = nn.LayerNorm(size, eps=1e-12)  # for the FNN module
146 |         self.norm_mha = nn.LayerNorm(size, eps=1e-12)  # for the MHA module
147 |         if feed_forward_macaron is not None:
148 |             self.norm_ff_macaron = nn.LayerNorm(size, eps=1e-12)
149 |             self.ff_scale = 0.5
150 |         else:
151 |             self.ff_scale = 1.0
152 |         if self.conv_module is not None:
153 |             self.norm_conv = nn.LayerNorm(size, eps=1e-12)  # for the CNN module
154 |             self.norm_final = nn.LayerNorm(
155 |                 size, eps=1e-12)  # for the final output of the block
156 |         self.dropout = nn.Dropout(dropout_rate)
157 |         self.size = size
158 |         self.normalize_before = normalize_before
159 | 
160 |     def forward(
161 |         self,
162 |         x: torch.Tensor,
163 |         mask: torch.Tensor,
164 |         pos_emb: torch.Tensor,
165 |         mask_pad: torch.Tensor = torch.ones((0, 0, 0), dtype=torch.bool),
166 |         att_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
167 |         cnn_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
168 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
169 |         """Compute encoded features.
170 | 
171 |         Args:
172 |             x (torch.Tensor): (#batch, time, size)
173 |             mask (torch.Tensor): Mask tensor for the input (#batch, time，time),
174 |                 (0, 0, 0) means fake mask.
175 |             pos_emb (torch.Tensor): positional encoding, must not be None
176 |                 for ConformerEncoderLayer.
177 |             mask_pad (torch.Tensor): batch padding mask used for conv module.
178 |                 (#batch, 1，time), (0, 0, 0) means fake mask.
179 |             att_cache (torch.Tensor): Cache tensor of the KEY & VALUE
180 |                 (#batch=1, head, cache_t1, d_k * 2), head * d_k == size.
181 |             cnn_cache (torch.Tensor): Convolution cache in conformer layer
182 |                 (#batch=1, size, cache_t2)
183 |         Returns:
184 |             torch.Tensor: Output tensor (#batch, time, size).
185 |             torch.Tensor: Mask tensor (#batch, time, time).
186 |             torch.Tensor: att_cache tensor,
187 |                 (#batch=1, head, cache_t1 + time, d_k * 2).
188 |             torch.Tensor: cnn_cahce tensor (#batch, size, cache_t2).
189 |         """
190 | 
191 |         # whether to use macaron style
192 |         if self.feed_forward_macaron is not None:
193 |             residual = x
194 |             if self.normalize_before:
195 |                 x = self.norm_ff_macaron(x)
196 |             x = residual + self.ff_scale * self.dropout(
197 |                 self.feed_forward_macaron(x))
198 |             if not self.normalize_before:
199 |                 x = self.norm_ff_macaron(x)
200 | 
201 |         # multi-headed self-attention module
202 |         residual = x
203 |         if self.normalize_before:
204 |             x = self.norm_mha(x)
205 |         x_att, new_att_cache = self.self_attn(x, x, x, mask, pos_emb,
206 |                                               att_cache)
207 |         x = residual + self.dropout(x_att)
208 |         if not self.normalize_before:
209 |             x = self.norm_mha(x)
210 | 
211 |         # convolution module
212 |         # Fake new cnn cache here, and then change it in conv_module
213 |         new_cnn_cache = torch.zeros((0, 0, 0), dtype=x.dtype, device=x.device)
214 |         if self.conv_module is not None:
215 |             residual = x
216 |             if self.normalize_before:
217 |                 x = self.norm_conv(x)
218 |             x, new_cnn_cache = self.conv_module(x, mask_pad, cnn_cache)
219 |             x = residual + self.dropout(x)
220 | 
221 |             if not self.normalize_before:
222 |                 x = self.norm_conv(x)
223 | 
224 |         # feed forward module
225 |         residual = x
226 |         if self.normalize_before:
227 |             x = self.norm_ff(x)
228 | 
229 |         x = residual + self.ff_scale * self.dropout(self.feed_forward(x))
230 |         if not self.normalize_before:
231 |             x = self.norm_ff(x)
232 | 
233 |         if self.conv_module is not None:
234 |             x = self.norm_final(x)
235 | 
236 |         return x, mask, new_att_cache, new_cnn_cache
237 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/positionwise_feed_forward.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2019 Shigeki Karita
  2 | #               2020 Mobvoi Inc (Binbin Zhang)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #   http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | """Positionwise feed forward layer definition."""
 16 | 
 17 | import torch
 18 | 
 19 | 
 20 | class PositionwiseFeedForward(torch.nn.Module):
 21 |     """Positionwise feed forward layer.
 22 | 
 23 |     FeedForward are appied on each position of the sequence.
 24 |     The output dim is same with the input dim.
 25 | 
 26 |     Args:
 27 |         idim (int): Input dimenstion.
 28 |         hidden_units (int): The number of hidden units.
 29 |         dropout_rate (float): Dropout rate.
 30 |         activation (torch.nn.Module): Activation function
 31 |     """
 32 | 
 33 |     def __init__(
 34 |             self,
 35 |             idim: int,
 36 |             hidden_units: int,
 37 |             dropout_rate: float,
 38 |             activation: torch.nn.Module = torch.nn.ReLU(),
 39 |     ):
 40 |         """Construct a PositionwiseFeedForward object."""
 41 |         super(PositionwiseFeedForward, self).__init__()
 42 |         self.w_1 = torch.nn.Linear(idim, hidden_units)
 43 |         self.activation = activation
 44 |         self.dropout = torch.nn.Dropout(dropout_rate)
 45 |         self.w_2 = torch.nn.Linear(hidden_units, idim)
 46 | 
 47 |     def forward(self, xs: torch.Tensor) -> torch.Tensor:
 48 |         """Forward function.
 49 | 
 50 |         Args:
 51 |             xs: input tensor (B, L, D)
 52 |         Returns:
 53 |             output tensor, (B, L, D)
 54 |         """
 55 |         return self.w_2(self.dropout(self.activation(self.w_1(xs))))
 56 | 
 57 | 
 58 | class MoEFFNLayer(torch.nn.Module):
 59 |     """
 60 |     Mixture of expert with Positionwise feed forward layer
 61 |     See also figure 1 in https://arxiv.org/pdf/2305.15663.pdf
 62 |     The output dim is same with the input dim.
 63 | 
 64 |     Modified from https://github.com/Lightning-AI/lit-gpt/pull/823
 65 |                   https://github.com/mistralai/mistral-src/blob/b46d6/moe_one_file_ref.py#L203-L219
 66 |     Args:
 67 |         n_expert: number of expert.
 68 |         n_expert_per_token: The actual number of experts used for each frame
 69 |         idim (int): Input dimenstion.
 70 |         hidden_units (int): The number of hidden units.
 71 |         dropout_rate (float): Dropout rate.
 72 |         activation (torch.nn.Module): Activation function
 73 |     """
 74 | 
 75 |     def __init__(
 76 |             self,
 77 |             n_expert: int,
 78 |             n_expert_per_token: int,
 79 |             idim: int,
 80 |             hidden_units: int,
 81 |             dropout_rate: float,
 82 |             activation: torch.nn.Module = torch.nn.ReLU(),
 83 |     ):
 84 |         super(MoEFFNLayer, self).__init__()
 85 |         self.gate = torch.nn.Linear(idim, n_expert, bias=False)
 86 |         self.experts = torch.nn.ModuleList(
 87 |             PositionwiseFeedForward(idim, hidden_units, dropout_rate,
 88 |                                     activation) for _ in range(n_expert))
 89 |         self.n_expert_per_token = n_expert_per_token
 90 | 
 91 |     def forward(self, xs: torch.Tensor) -> torch.Tensor:
 92 |         """Foward function.
 93 |         Args:
 94 |             xs: input tensor (B, L, D)
 95 |         Returns:
 96 |             output tensor, (B, L, D)
 97 | 
 98 |         """
 99 |         B, L, D = xs.size(
100 |         )  # batch size, sequence length, embedding dimension (idim)
101 |         xs = xs.view(-1, D)  # (B*L, D)
102 |         router = self.gate(xs)  # (B*L, n_expert)
103 |         logits, indices = torch.topk(
104 |             router, self.n_expert_per_token
105 |         )  # probs:(B*L, n_expert), indices: (B*L, n_expert)
106 |         weights = torch.nn.functional.softmax(
107 |             logits, dim=1,
108 |             dtype=torch.float).to(dtype=xs.dtype)  # (B*L, n_expert_per_token)
109 |         output = torch.zeros_like(xs)  # (B*L, D)
110 |         for i, expert in enumerate(self.experts):
111 |             mask = indices == i
112 |             batch_idx, ith_expert = torch.where(mask)
113 |             output[batch_idx] += weights[batch_idx, ith_expert, None] * expert(
114 |                 xs[batch_idx])
115 |         return output.view(B, L, D)
116 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/subsampling.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2021 Mobvoi Inc (Binbin Zhang, Di Wu)
  2 | #               2024 Alibaba Inc (Xiang Lyu)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #   http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """Subsampling layer definition."""
 17 | 
 18 | from typing import Tuple, Union
 19 | 
 20 | import torch
 21 | 
 22 | 
 23 | class BaseSubsampling(torch.nn.Module):
 24 | 
 25 |     def __init__(self):
 26 |         super().__init__()
 27 |         self.right_context = 0
 28 |         self.subsampling_rate = 1
 29 | 
 30 |     def position_encoding(self, offset: Union[int, torch.Tensor],
 31 |                           size: int) -> torch.Tensor:
 32 |         return self.pos_enc.position_encoding(offset, size)
 33 | 
 34 | 
 35 | class EmbedinigNoSubsampling(BaseSubsampling):
 36 |     """Embedding input without subsampling
 37 |     """
 38 | 
 39 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
 40 |                  pos_enc_class: torch.nn.Module):
 41 |         super().__init__()
 42 |         self.embed = torch.nn.Embedding(idim, odim)
 43 |         self.pos_enc = pos_enc_class
 44 | 
 45 |     def forward(
 46 |         self,
 47 |         x: torch.Tensor,
 48 |         x_mask: torch.Tensor,
 49 |         offset: Union[int, torch.Tensor] = 0
 50 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
 51 |         """Input x.
 52 | 
 53 |         Args:
 54 |             x (torch.Tensor): Input tensor (#batch, time, idim).
 55 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
 56 | 
 57 |         Returns:
 58 |             torch.Tensor: linear input tensor (#batch, time', odim),
 59 |                 where time' = time .
 60 |             torch.Tensor: linear input mask (#batch, 1, time'),
 61 |                 where time' = time .
 62 | 
 63 |         """
 64 |         x = self.embed(x)
 65 |         x, pos_emb = self.pos_enc(x, offset)
 66 |         return x, pos_emb, x_mask
 67 | 
 68 | 
 69 | class LinearNoSubsampling(BaseSubsampling):
 70 |     """Linear transform the input without subsampling
 71 | 
 72 |     Args:
 73 |         idim (int): Input dimension.
 74 |         odim (int): Output dimension.
 75 |         dropout_rate (float): Dropout rate.
 76 | 
 77 |     """
 78 | 
 79 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
 80 |                  pos_enc_class: torch.nn.Module):
 81 |         """Construct an linear object."""
 82 |         super().__init__()
 83 |         self.out = torch.nn.Sequential(
 84 |             torch.nn.Linear(idim, odim),
 85 |             torch.nn.LayerNorm(odim, eps=1e-5),
 86 |             torch.nn.Dropout(dropout_rate),
 87 |         )
 88 |         self.pos_enc = pos_enc_class
 89 |         self.right_context = 0
 90 |         self.subsampling_rate = 1
 91 | 
 92 |     def forward(
 93 |         self,
 94 |         x: torch.Tensor,
 95 |         x_mask: torch.Tensor,
 96 |         offset: Union[int, torch.Tensor] = 0
 97 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
 98 |         """Input x.
 99 | 
100 |         Args:
101 |             x (torch.Tensor): Input tensor (#batch, time, idim).
102 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
103 | 
104 |         Returns:
105 |             torch.Tensor: linear input tensor (#batch, time', odim),
106 |                 where time' = time .
107 |             torch.Tensor: linear input mask (#batch, 1, time'),
108 |                 where time' = time .
109 | 
110 |         """
111 |         x = self.out(x)
112 |         x, pos_emb = self.pos_enc(x, offset)
113 |         return x, pos_emb, x_mask
114 | 
115 | 
116 | class Conv1dSubsampling2(BaseSubsampling):
117 |     """Convolutional 1D subsampling (to 1/2 length).
118 |        It is designed for Whisper, ref:
119 |        https://github.com/openai/whisper/blob/main/whisper/model.py
120 | 
121 |     Args:
122 |         idim (int): Input dimension.
123 |         odim (int): Output dimension.
124 |         dropout_rate (float): Dropout rate.
125 | 
126 |     """
127 | 
128 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
129 |                  pos_enc_class: torch.nn.Module):
130 |         """Construct an Conv1dSubsampling2 object."""
131 |         super().__init__()
132 |         self.conv = torch.nn.Sequential(
133 |             torch.nn.Conv1d(idim, odim, kernel_size=3, padding=1),
134 |             torch.nn.GELU(),
135 |             torch.nn.Conv1d(odim, odim, kernel_size=3, stride=2, padding=1),
136 |             torch.nn.GELU(),
137 |         )
138 |         self.pos_enc = pos_enc_class
139 |         # The right context for every conv layer is computed by:
140 |         # (kernel_size - 1) * frame_rate_of_this_layer
141 |         self.subsampling_rate = 2
142 |         # 4 = (3 - 1) * 1 + (3 - 1) * 1
143 |         self.right_context = 4
144 | 
145 |     def forward(
146 |         self,
147 |         x: torch.Tensor,
148 |         x_mask: torch.Tensor,
149 |         offset: Union[int, torch.Tensor] = 0
150 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
151 |         """Subsample x.
152 | 
153 |         Args:
154 |             x (torch.Tensor): Input tensor (#batch, time, idim).
155 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
156 | 
157 |         Returns:
158 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
159 |                 where time' = time // 2.
160 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
161 |                 where time' = time // 2.
162 |             torch.Tensor: positional encoding
163 | 
164 |         """
165 |         time = x.size(1)
166 |         x = x.transpose(1, 2)  # (b, f, t)
167 |         x = self.conv(x)
168 |         x = x.transpose(1, 2)  # (b, t, f)
169 |         x, pos_emb = self.pos_enc(x, offset)
170 |         return x, pos_emb, x_mask[:, :, (time + 1) % 2::2]
171 | 
172 | 
173 | class Conv2dSubsampling4(BaseSubsampling):
174 |     """Convolutional 2D subsampling (to 1/4 length).
175 | 
176 |     Args:
177 |         idim (int): Input dimension.
178 |         odim (int): Output dimension.
179 |         dropout_rate (float): Dropout rate.
180 | 
181 |     """
182 | 
183 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
184 |                  pos_enc_class: torch.nn.Module):
185 |         """Construct an Conv2dSubsampling4 object."""
186 |         super().__init__()
187 |         self.conv = torch.nn.Sequential(
188 |             torch.nn.Conv2d(1, odim, 3, 2),
189 |             torch.nn.ReLU(),
190 |             torch.nn.Conv2d(odim, odim, 3, 2),
191 |             torch.nn.ReLU(),
192 |         )
193 |         self.out = torch.nn.Sequential(
194 |             torch.nn.Linear(odim * (((idim - 1) // 2 - 1) // 2), odim))
195 |         self.pos_enc = pos_enc_class
196 |         # The right context for every conv layer is computed by:
197 |         # (kernel_size - 1) * frame_rate_of_this_layer
198 |         self.subsampling_rate = 4
199 |         # 6 = (3 - 1) * 1 + (3 - 1) * 2
200 |         self.right_context = 6
201 | 
202 |     def forward(
203 |         self,
204 |         x: torch.Tensor,
205 |         x_mask: torch.Tensor,
206 |         offset: Union[int, torch.Tensor] = 0
207 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
208 |         """Subsample x.
209 | 
210 |         Args:
211 |             x (torch.Tensor): Input tensor (#batch, time, idim).
212 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
213 | 
214 |         Returns:
215 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
216 |                 where time' = time // 4.
217 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
218 |                 where time' = time // 4.
219 |             torch.Tensor: positional encoding
220 | 
221 |         """
222 |         x = x.unsqueeze(1)  # (b, c=1, t, f)
223 |         x = self.conv(x)
224 |         b, c, t, f = x.size()
225 |         x = self.out(x.transpose(1, 2).contiguous().view(b, t, c * f))
226 |         x, pos_emb = self.pos_enc(x, offset)
227 |         return x, pos_emb, x_mask[:, :, 2::2][:, :, 2::2]
228 | 
229 | 
230 | class Conv2dSubsampling6(BaseSubsampling):
231 |     """Convolutional 2D subsampling (to 1/6 length).
232 |     Args:
233 |         idim (int): Input dimension.
234 |         odim (int): Output dimension.
235 |         dropout_rate (float): Dropout rate.
236 |         pos_enc (torch.nn.Module): Custom position encoding layer.
237 |     """
238 | 
239 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
240 |                  pos_enc_class: torch.nn.Module):
241 |         """Construct an Conv2dSubsampling6 object."""
242 |         super().__init__()
243 |         self.conv = torch.nn.Sequential(
244 |             torch.nn.Conv2d(1, odim, 3, 2),
245 |             torch.nn.ReLU(),
246 |             torch.nn.Conv2d(odim, odim, 5, 3),
247 |             torch.nn.ReLU(),
248 |         )
249 |         self.linear = torch.nn.Linear(odim * (((idim - 1) // 2 - 2) // 3),
250 |                                       odim)
251 |         self.pos_enc = pos_enc_class
252 |         # 10 = (3 - 1) * 1 + (5 - 1) * 2
253 |         self.subsampling_rate = 6
254 |         self.right_context = 10
255 | 
256 |     def forward(
257 |         self,
258 |         x: torch.Tensor,
259 |         x_mask: torch.Tensor,
260 |         offset: Union[int, torch.Tensor] = 0
261 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
262 |         """Subsample x.
263 |         Args:
264 |             x (torch.Tensor): Input tensor (#batch, time, idim).
265 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
266 | 
267 |         Returns:
268 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
269 |                 where time' = time // 6.
270 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
271 |                 where time' = time // 6.
272 |             torch.Tensor: positional encoding
273 |         """
274 |         x = x.unsqueeze(1)  # (b, c, t, f)
275 |         x = self.conv(x)
276 |         b, c, t, f = x.size()
277 |         x = self.linear(x.transpose(1, 2).contiguous().view(b, t, c * f))
278 |         x, pos_emb = self.pos_enc(x, offset)
279 |         return x, pos_emb, x_mask[:, :, 2::2][:, :, 4::3]
280 | 
281 | 
282 | class Conv2dSubsampling8(BaseSubsampling):
283 |     """Convolutional 2D subsampling (to 1/8 length).
284 | 
285 |     Args:
286 |         idim (int): Input dimension.
287 |         odim (int): Output dimension.
288 |         dropout_rate (float): Dropout rate.
289 | 
290 |     """
291 | 
292 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
293 |                  pos_enc_class: torch.nn.Module):
294 |         """Construct an Conv2dSubsampling8 object."""
295 |         super().__init__()
296 |         self.conv = torch.nn.Sequential(
297 |             torch.nn.Conv2d(1, odim, 3, 2),
298 |             torch.nn.ReLU(),
299 |             torch.nn.Conv2d(odim, odim, 3, 2),
300 |             torch.nn.ReLU(),
301 |             torch.nn.Conv2d(odim, odim, 3, 2),
302 |             torch.nn.ReLU(),
303 |         )
304 |         self.linear = torch.nn.Linear(
305 |             odim * ((((idim - 1) // 2 - 1) // 2 - 1) // 2), odim)
306 |         self.pos_enc = pos_enc_class
307 |         self.subsampling_rate = 8
308 |         # 14 = (3 - 1) * 1 + (3 - 1) * 2 + (3 - 1) * 4
309 |         self.right_context = 14
310 | 
311 |     def forward(
312 |         self,
313 |         x: torch.Tensor,
314 |         x_mask: torch.Tensor,
315 |         offset: Union[int, torch.Tensor] = 0
316 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
317 |         """Subsample x.
318 | 
319 |         Args:
320 |             x (torch.Tensor): Input tensor (#batch, time, idim).
321 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
322 | 
323 |         Returns:
324 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
325 |                 where time' = time // 8.
326 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
327 |                 where time' = time // 8.
328 |             torch.Tensor: positional encoding
329 |         """
330 |         x = x.unsqueeze(1)  # (b, c, t, f)
331 |         x = self.conv(x)
332 |         b, c, t, f = x.size()
333 |         x = self.linear(x.transpose(1, 2).contiguous().view(b, t, c * f))
334 |         x, pos_emb = self.pos_enc(x, offset)
335 |         return x, pos_emb, x_mask[:, :, 2::2][:, :, 2::2][:, :, 2::2]
336 | 
337 | 
338 | class LegacyLinearNoSubsampling(BaseSubsampling):
339 |     """Linear transform the input without subsampling
340 | 
341 |     Args:
342 |         idim (int): Input dimension.
343 |         odim (int): Output dimension.
344 |         dropout_rate (float): Dropout rate.
345 | 
346 |     """
347 | 
348 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
349 |                  pos_enc_class: torch.nn.Module):
350 |         """Construct an linear object."""
351 |         super().__init__()
352 |         self.out = torch.nn.Sequential(
353 |             torch.nn.Linear(idim, odim),
354 |             torch.nn.LayerNorm(odim, eps=1e-5),
355 |             torch.nn.Dropout(dropout_rate),
356 |             torch.nn.ReLU(),
357 |         )
358 |         self.pos_enc = pos_enc_class
359 |         self.right_context = 0
360 |         self.subsampling_rate = 1
361 | 
362 |     def forward(
363 |         self,
364 |         x: torch.Tensor,
365 |         x_mask: torch.Tensor,
366 |         offset: Union[int, torch.Tensor] = 0
367 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
368 |         """Input x.
369 | 
370 |         Args:
371 |             x (torch.Tensor): Input tensor (#batch, time, idim).
372 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
373 | 
374 |         Returns:
375 |             torch.Tensor: linear input tensor (#batch, time', odim),
376 |                 where time' = time .
377 |             torch.Tensor: linear input mask (#batch, 1, time'),
378 |                 where time' = time .
379 | 
380 |         """
381 |         x = self.out(x)
382 |         x, pos_emb = self.pos_enc(x, offset)
383 |         return x, pos_emb, x_mask
384 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/utils/class_utils.py:
--------------------------------------------------------------------------------
 1 | # Copyright [2023-11-28] <sxc19@mails.tsinghua.edu.cn, Xingchen Song>
 2 | #            2024 Alibaba Inc (authors: Xiang Lyu)
 3 | #
 4 | # Licensed under the Apache License, Version 2.0 (the "License");
 5 | # you may not use this file except in compliance with the License.
 6 | # You may obtain a copy of the License at
 7 | #
 8 | #     http://www.apache.org/licenses/LICENSE-2.0
 9 | #
10 | # Unless required by applicable law or agreed to in writing, software
11 | # distributed under the License is distributed on an "AS IS" BASIS,
12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
13 | # See the License for the specific language governing permissions and
14 | # limitations under the License.
15 | import torch
16 | 
17 | from ..transformer.activation import Swish
18 | from ..transformer.subsampling import (
19 |     LinearNoSubsampling,
20 |     EmbedinigNoSubsampling,
21 |     Conv1dSubsampling2,
22 |     Conv2dSubsampling4,
23 |     Conv2dSubsampling6,
24 |     Conv2dSubsampling8,
25 | )
26 | from ..transformer.embedding import (
27 |     PositionalEncoding,
28 |     RelPositionalEncoding,
29 |     WhisperPositionalEncoding,
30 |     LearnablePositionalEncoding,
31 |     NoPositionalEncoding)
32 | from ..transformer.attention import (MultiHeadedAttention,
33 |     RelPositionMultiHeadedAttention)
34 | from ..transformer.embedding import EspnetRelPositionalEncoding
35 | from ..transformer.subsampling import LegacyLinearNoSubsampling
36 | 
37 | 
38 | COSYVOICE_ACTIVATION_CLASSES = {
39 |     "hardtanh": torch.nn.Hardtanh,
40 |     "tanh": torch.nn.Tanh,
41 |     "relu": torch.nn.ReLU,
42 |     "selu": torch.nn.SELU,
43 |     "swish": getattr(torch.nn, "SiLU", Swish),
44 |     "gelu": torch.nn.GELU,
45 | }
46 | 
47 | COSYVOICE_SUBSAMPLE_CLASSES = {
48 |     "linear": LinearNoSubsampling,
49 |     "linear_legacy": LegacyLinearNoSubsampling,
50 |     "embed": EmbedinigNoSubsampling,
51 |     "conv1d2": Conv1dSubsampling2,
52 |     "conv2d": Conv2dSubsampling4,
53 |     "conv2d6": Conv2dSubsampling6,
54 |     "conv2d8": Conv2dSubsampling8,
55 |     'paraformer_dummy': torch.nn.Identity
56 | }
57 | 
58 | COSYVOICE_EMB_CLASSES = {
59 |     "embed": PositionalEncoding,
60 |     "abs_pos": PositionalEncoding,
61 |     "rel_pos": RelPositionalEncoding,
62 |     "rel_pos_espnet": EspnetRelPositionalEncoding,
63 |     "no_pos": NoPositionalEncoding,
64 |     "abs_pos_whisper": WhisperPositionalEncoding,
65 |     "embed_learnable_pe": LearnablePositionalEncoding,
66 | }
67 | 
68 | COSYVOICE_ATTENTION_CLASSES = {
69 |     "selfattn": MultiHeadedAttention,
70 |     "rel_selfattn": RelPositionMultiHeadedAttention,
71 | }
72 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/utils/mask.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2019 Shigeki Karita
  2 | #               2020 Mobvoi Inc (Binbin Zhang)
  3 | #               2024 Alibaba Inc (authors: Xiang Lyu)
  4 | #
  5 | # Licensed under the Apache License, Version 2.0 (the "License");
  6 | # you may not use this file except in compliance with the License.
  7 | # You may obtain a copy of the License at
  8 | #
  9 | #   http://www.apache.org/licenses/LICENSE-2.0
 10 | #
 11 | # Unless required by applicable law or agreed to in writing, software
 12 | # distributed under the License is distributed on an "AS IS" BASIS,
 13 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14 | # See the License for the specific language governing permissions and
 15 | # limitations under the License.
 16 | 
 17 | import torch
 18 | 
 19 | '''
 20 | def subsequent_mask(
 21 |         size: int,
 22 |         device: torch.device = torch.device("cpu"),
 23 | ) -> torch.Tensor:
 24 |     """Create mask for subsequent steps (size, size).
 25 | 
 26 |     This mask is used only in decoder which works in an auto-regressive mode.
 27 |     This means the current step could only do attention with its left steps.
 28 | 
 29 |     In encoder, fully attention is used when streaming is not necessary and
 30 |     the sequence is not long. In this  case, no attention mask is needed.
 31 | 
 32 |     When streaming is need, chunk-based attention is used in encoder. See
 33 |     subsequent_chunk_mask for the chunk-based attention mask.
 34 | 
 35 |     Args:
 36 |         size (int): size of mask
 37 |         str device (str): "cpu" or "cuda" or torch.Tensor.device
 38 |         dtype (torch.device): result dtype
 39 | 
 40 |     Returns:
 41 |         torch.Tensor: mask
 42 | 
 43 |     Examples:
 44 |         >>> subsequent_mask(3)
 45 |         [[1, 0, 0],
 46 |          [1, 1, 0],
 47 |          [1, 1, 1]]
 48 |     """
 49 |     ret = torch.ones(size, size, device=device, dtype=torch.bool)
 50 |     return torch.tril(ret)
 51 | '''
 52 | 
 53 | 
 54 | def subsequent_chunk_mask(
 55 |         size: int,
 56 |         chunk_size: int,
 57 |         num_left_chunks: int = -1,
 58 |         device: torch.device = torch.device("cpu"),
 59 | ) -> torch.Tensor:
 60 |     """Create mask for subsequent steps (size, size) with chunk size,
 61 |        this is for streaming encoder
 62 | 
 63 |     Args:
 64 |         size (int): size of mask
 65 |         chunk_size (int): size of chunk
 66 |         num_left_chunks (int): number of left chunks
 67 |             <0: use full chunk
 68 |             >=0: use num_left_chunks
 69 |         device (torch.device): "cpu" or "cuda" or torch.Tensor.device
 70 | 
 71 |     Returns:
 72 |         torch.Tensor: mask
 73 | 
 74 |     Examples:
 75 |         >>> subsequent_chunk_mask(4, 2)
 76 |         [[1, 1, 0, 0],
 77 |          [1, 1, 0, 0],
 78 |          [1, 1, 1, 1],
 79 |          [1, 1, 1, 1]]
 80 |     """
 81 |     # NOTE this modified implementation meets onnx export requirements, but it doesn't support num_left_chunks
 82 |     # actually this is not needed after we have inference cache implemented, will remove it later
 83 |     pos_idx = torch.arange(size, device=device)
 84 |     block_value = (torch.div(pos_idx, chunk_size, rounding_mode='trunc') + 1) * chunk_size
 85 |     ret = pos_idx.unsqueeze(0) < block_value.unsqueeze(1)
 86 |     return ret
 87 | 
 88 | 
 89 | def add_optional_chunk_mask(xs: torch.Tensor,
 90 |                             masks: torch.Tensor,
 91 |                             use_dynamic_chunk: bool,
 92 |                             use_dynamic_left_chunk: bool,
 93 |                             decoding_chunk_size: int,
 94 |                             static_chunk_size: int,
 95 |                             num_decoding_left_chunks: int,
 96 |                             enable_full_context: bool = True):
 97 |     """ Apply optional mask for encoder.
 98 | 
 99 |     Args:
100 |         xs (torch.Tensor): padded input, (B, L, D), L for max length
101 |         mask (torch.Tensor): mask for xs, (B, 1, L)
102 |         use_dynamic_chunk (bool): whether to use dynamic chunk or not
103 |         use_dynamic_left_chunk (bool): whether to use dynamic left chunk for
104 |             training.
105 |         decoding_chunk_size (int): decoding chunk size for dynamic chunk, it's
106 |             0: default for training, use random dynamic chunk.
107 |             <0: for decoding, use full chunk.
108 |             >0: for decoding, use fixed chunk size as set.
109 |         static_chunk_size (int): chunk size for static chunk training/decoding
110 |             if it's greater than 0, if use_dynamic_chunk is true,
111 |             this parameter will be ignored
112 |         num_decoding_left_chunks: number of left chunks, this is for decoding,
113 |             the chunk size is decoding_chunk_size.
114 |             >=0: use num_decoding_left_chunks
115 |             <0: use all left chunks
116 |         enable_full_context (bool):
117 |             True: chunk size is either [1, 25] or full context(max_len)
118 |             False: chunk size ~ U[1, 25]
119 | 
120 |     Returns:
121 |         torch.Tensor: chunk mask of the input xs.
122 |     """
123 |     # Whether to use chunk mask or not
124 |     if use_dynamic_chunk:
125 |         max_len = xs.size(1)
126 |         if decoding_chunk_size < 0:
127 |             chunk_size = max_len
128 |             num_left_chunks = -1
129 |         elif decoding_chunk_size > 0:
130 |             chunk_size = decoding_chunk_size
131 |             num_left_chunks = num_decoding_left_chunks
132 |         else:
133 |             # chunk size is either [1, 25] or full context(max_len).
134 |             # Since we use 4 times subsampling and allow up to 1s(100 frames)
135 |             # delay, the maximum frame is 100 / 4 = 25.
136 |             chunk_size = torch.randint(1, max_len, (1, )).item()
137 |             num_left_chunks = -1
138 |             if chunk_size > max_len // 2 and enable_full_context:
139 |                 chunk_size = max_len
140 |             else:
141 |                 chunk_size = chunk_size % 25 + 1
142 |                 if use_dynamic_left_chunk:
143 |                     max_left_chunks = (max_len - 1) // chunk_size
144 |                     num_left_chunks = torch.randint(0, max_left_chunks,
145 |                                                     (1, )).item()
146 |         chunk_masks = subsequent_chunk_mask(xs.size(1), chunk_size,
147 |                                             num_left_chunks,
148 |                                             xs.device)  # (L, L)
149 |         chunk_masks = chunk_masks.unsqueeze(0)  # (1, L, L)
150 |         chunk_masks = masks & chunk_masks  # (B, L, L)
151 |     elif static_chunk_size > 0:
152 |         num_left_chunks = num_decoding_left_chunks
153 |         chunk_masks = subsequent_chunk_mask(xs.size(1), static_chunk_size,
154 |                                             num_left_chunks,
155 |                                             xs.device)  # (L, L)
156 |         chunk_masks = chunk_masks.unsqueeze(0)  # (1, L, L)
157 |         chunk_masks = masks & chunk_masks  # (B, L, L)
158 |     else:
159 |         chunk_masks = masks
160 |     assert chunk_masks.dtype == torch.bool
161 |     if (chunk_masks.sum(dim=-1) == 0).sum().item() != 0:
162 |         logging.warning('get chunk_masks all false at some timestep, force set to true, make sure they are masked in futuer computation!')
163 |         chunk_masks[chunk_masks.sum(dim=-1)==0] = True
164 |     return chunk_masks
165 | 
166 | 
167 | def make_pad_mask(lengths: torch.Tensor, max_len: int = 0) -> torch.Tensor:
168 |     """Make mask tensor containing indices of padded part.
169 | 
170 |     See description of make_non_pad_mask.
171 | 
172 |     Args:
173 |         lengths (torch.Tensor): Batch of lengths (B,).
174 |     Returns:
175 |         torch.Tensor: Mask tensor containing indices of padded part.
176 | 
177 |     Examples:
178 |         >>> lengths = [5, 3, 2]
179 |         >>> make_pad_mask(lengths)
180 |         masks = [[0, 0, 0, 0 ,0],
181 |                  [0, 0, 0, 1, 1],
182 |                  [0, 0, 1, 1, 1]]
183 |     """
184 |     batch_size = lengths.size(0)
185 |     max_len = max_len if max_len > 0 else lengths.max().item()
186 |     seq_range = torch.arange(0,
187 |                              max_len,
188 |                              dtype=torch.int64,
189 |                              device=lengths.device)
190 |     seq_range_expand = seq_range.unsqueeze(0).expand(batch_size, max_len)
191 |     seq_length_expand = lengths.unsqueeze(-1)
192 |     mask = seq_range_expand >= seq_length_expand
193 |     return mask
194 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/utils/mel.py:
--------------------------------------------------------------------------------
 1 | """mel-spectrogram extraction in Matcha-TTS"""
 2 | from librosa.filters import mel as librosa_mel_fn
 3 | import torch
 4 | import numpy as np
 5 | 
 6 | 
 7 | # NOTE: they decalred these global vars
 8 | mel_basis = {}
 9 | hann_window = {}
10 | 
11 | 
12 | def dynamic_range_compression_torch(x, C=1, clip_val=1e-5):
13 |     return torch.log(torch.clamp(x, min=clip_val) * C)
14 | 
15 | 
16 | def spectral_normalize_torch(magnitudes):
17 |     output = dynamic_range_compression_torch(magnitudes)
18 |     return output
19 | 
20 | """
21 | feat_extractor: !name:matcha.utils.audio.mel_spectrogram
22 |     n_fft: 1920
23 |     num_mels: 80
24 |     sampling_rate: 24000
25 |     hop_size: 480
26 |     win_size: 1920
27 |     fmin: 0
28 |     fmax: 8000
29 |     center: False
30 | 
31 | """
32 | 
33 | def mel_spectrogram(y, n_fft=1920, num_mels=80, sampling_rate=24000, hop_size=480, win_size=1920,
34 |                     fmin=0, fmax=8000, center=False):
35 |     """Copied from https://github.com/shivammehta25/Matcha-TTS/blob/main/matcha/utils/audio.py
36 |     Set default values according to Cosyvoice's config.
37 |     """
38 | 
39 |     if isinstance(y, np.ndarray):
40 |         y = torch.tensor(y).float()
41 | 
42 |     if len(y.shape) == 1:
43 |         y = y[None, ]
44 | 
45 |     if torch.min(y) < -1.0:
46 |         print("min value is ", torch.min(y))
47 |     if torch.max(y) > 1.0:
48 |         print("max value is ", torch.max(y))
49 | 
50 |     global mel_basis, hann_window  # pylint: disable=global-statement,global-variable-not-assigned
51 |     if f"{str(fmax)}_{str(y.device)}" not in mel_basis:
52 |         mel = librosa_mel_fn(sr=sampling_rate, n_fft=n_fft, n_mels=num_mels, fmin=fmin, fmax=fmax)
53 |         mel_basis[str(fmax) + "_" + str(y.device)] = torch.from_numpy(mel).float().to(y.device)
54 |         hann_window[str(y.device)] = torch.hann_window(win_size).to(y.device)
55 | 
56 |     y = torch.nn.functional.pad(
57 |         y.unsqueeze(1), (int((n_fft - hop_size) / 2), int((n_fft - hop_size) / 2)), mode="reflect"
58 |     )
59 |     y = y.squeeze(1)
60 | 
61 |     spec = torch.view_as_real(
62 |         torch.stft(
63 |             y,
64 |             n_fft,
65 |             hop_length=hop_size,
66 |             win_length=win_size,
67 |             window=hann_window[str(y.device)],
68 |             center=center,
69 |             pad_mode="reflect",
70 |             normalized=False,
71 |             onesided=True,
72 |             return_complex=True,
73 |         )
74 |     )
75 | 
76 |     spec = torch.sqrt(spec.pow(2).sum(-1) + (1e-9))
77 | 
78 |     spec = torch.matmul(mel_basis[str(fmax) + "_" + str(y.device)], spec)
79 |     spec = spectral_normalize_torch(spec)
80 | 
81 |     return spec
82 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3tokenizer/__init__.py:
--------------------------------------------------------------------------------
 1 | from .s3tokenizer import (
 2 |     S3_SR,
 3 |     S3_HOP,
 4 |     S3_TOKEN_HOP,
 5 |     S3_TOKEN_RATE,
 6 |     SPEECH_VOCAB_SIZE,
 7 |     S3Tokenizer,
 8 | )
 9 | 
10 | 
11 | SOS = SPEECH_VOCAB_SIZE
12 | EOS = SPEECH_VOCAB_SIZE + 1
13 | 
14 | 
15 | 
16 | def drop_invalid_tokens(x):
17 |     """Drop SoS and EoS"""
18 |     assert len(x.shape) == 1 or (len(x.shape) == 2 and x.shape[0] == 1), "only batch size of one allowed for now"
19 |     if SOS in x:
20 |         s = (x == SOS).nonzero(as_tuple=True)[0].squeeze(0) + 1
21 |     else:
22 |         s = 0
23 | 
24 |     if EOS in x:
25 |         e = (x == EOS).nonzero(as_tuple=True)[0].squeeze(0)
26 |     else:
27 |         e = None
28 | 
29 |     x = x[s: e]
30 |     return x
31 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3tokenizer/s3tokenizer.py:
--------------------------------------------------------------------------------
  1 | from typing import List, Tuple
  2 | 
  3 | import numpy as np
  4 | import librosa
  5 | import torch
  6 | import torch.nn.functional as F
  7 | from s3tokenizer.utils import padding
  8 | from s3tokenizer.model_v2 import (
  9 |     S3TokenizerV2,
 10 |     ModelConfig,
 11 | )
 12 | 
 13 | 
 14 | # Sampling rate of the inputs to S3TokenizerV2
 15 | S3_SR = 16_000
 16 | S3_HOP = 160  # 100 frames/sec
 17 | S3_TOKEN_HOP = 640  # 25 tokens/sec
 18 | S3_TOKEN_RATE = 25
 19 | SPEECH_VOCAB_SIZE = 6561
 20 | 
 21 | 
 22 | class S3Tokenizer(S3TokenizerV2):
 23 |     """
 24 |     s3tokenizer.S3TokenizerV2 with the following changes:
 25 |     - a more integrated `forward`
 26 |     - compute `log_mel_spectrogram` using `_mel_filters` and `window` in `register_buffers`
 27 |     """
 28 | 
 29 |     ignore_state_dict_missing = ("_mel_filters", "window")
 30 | 
 31 |     def __init__(
 32 |         self,
 33 |         name: str="speech_tokenizer_v2_25hz",
 34 |         config: ModelConfig = ModelConfig()
 35 |     ):
 36 |         super().__init__(name)
 37 | 
 38 |         self.n_fft = 400
 39 |         _mel_filters = librosa.filters.mel(
 40 |             sr=S3_SR,
 41 |             n_fft=self.n_fft,
 42 |             n_mels=config.n_mels
 43 |         )
 44 |         self.register_buffer(
 45 |             "_mel_filters",
 46 |             torch.FloatTensor(_mel_filters),
 47 |         )
 48 | 
 49 |         self.register_buffer(
 50 |             "window",
 51 |             torch.hann_window(self.n_fft),
 52 |         )
 53 | 
 54 |     def pad(self, wavs, sr) -> List[torch.Tensor]:
 55 |         """
 56 |         Given a list of wavs with the same `sample_rate`, pad them so that the length is multiple of 40ms (S3 runs at 25 token/sec).
 57 |         """
 58 |         processed_wavs = []
 59 |         for wav in wavs:
 60 |             if isinstance(wav, np.ndarray):
 61 |                 wav = torch.from_numpy(wav)
 62 |             if wav.dim() == 1:
 63 |                 wav = wav.unsqueeze(0)
 64 | 
 65 |             n_tokens = (wav.shape[1] / sr) * S3_TOKEN_RATE
 66 |             n_tokens = np.ceil(n_tokens)
 67 |             intended_wav_len = n_tokens * (sr / S3_TOKEN_RATE)
 68 |             intended_wav_len = int(intended_wav_len)
 69 |             wav = torch.nn.functional.pad(
 70 |                 wav,
 71 |                 (0, intended_wav_len - wav.shape[-1]),
 72 |                 mode="constant",
 73 |                 value=0
 74 |             )
 75 |             processed_wavs.append(wav)
 76 |         return processed_wavs
 77 | 
 78 |     def _prepare_audio(self, wavs):
 79 |         """Prepare a list of audios for s3tokenizer processing."""
 80 |         processed_wavs = []
 81 |         for wav in wavs:
 82 |             if isinstance(wav, np.ndarray):
 83 |                 wav = torch.from_numpy(wav)
 84 |             if wav.dim() == 1:
 85 |                 wav = wav.unsqueeze(0)
 86 | 
 87 |             processed_wavs.append(wav)
 88 |         return processed_wavs
 89 | 
 90 |     @torch.no_grad()
 91 |     def forward(
 92 |         self,
 93 |         wavs: torch.Tensor,
 94 |         accelerator: 'Accelerator'=None,
 95 |         max_len: int=None,
 96 |     ) -> Tuple[torch.Tensor, torch.LongTensor]:
 97 |         """
 98 |         NOTE: mel-spec has a hop size of 160 points (100 frame/sec).
 99 |         FIXME: this class inherits `nn.Module` but doesn't accept `torch.Tensor` and handles a list of wavs one by one, which is unexpected.
100 | 
101 |         Args
102 |         ----
103 |         - `wavs`: 16 kHz speech audio
104 |         - `max_len` max length to truncate the output sequence to (25 token/sec).
105 |         NOTE: please pad the waveform if longer sequence is needed.
106 |         """
107 |         processed_wavs = self._prepare_audio(wavs)
108 |         mels, mel_lens = [], []
109 |         for wav in processed_wavs:
110 |             wav = wav.to(self.device)
111 |             mel = self.log_mel_spectrogram(wav)  # [B=1, F, T]
112 |             if max_len is not None:
113 |                 mel = mel[..., :max_len * 4]  # num_mel_frames = 4 * num_tokens
114 |             mels.append(mel.squeeze(0))
115 | 
116 |         mels, mel_lens = padding(mels)
117 |         if accelerator is None:
118 |             tokenizer = self
119 |         else:
120 |             tokenizer = accelerator.unwrap_model(self)
121 | 
122 |         speech_tokens, speech_token_lens = tokenizer.quantize(mels, mel_lens.to(self.device))
123 |         return (
124 |             speech_tokens.long().detach(),
125 |             speech_token_lens.long().detach(),
126 |         )
127 | 
128 |     def log_mel_spectrogram(
129 |         self,
130 |         audio: torch.Tensor,
131 |         padding: int = 0,
132 |     ):
133 |         """
134 |         Compute the log-Mel spectrogram of
135 | 
136 |         Parameters
137 |         ----------
138 |         audio: torch.Tensor, shape = (*)
139 |             The path to audio or either a NumPy array or Tensor containing the
140 |             audio waveform in 16 kHz
141 | 
142 |         padding: int
143 |             Number of zero samples to pad to the right
144 | 
145 |         Returns
146 |         -------
147 |         torch.Tensor, shape = (128, n_frames)
148 |             A Tensor that contains the Mel spectrogram
149 |         """
150 |         if not torch.is_tensor(audio):
151 |             audio = torch.from_numpy(audio)
152 | 
153 |         audio = audio.to(self.device)
154 |         if padding > 0:
155 |             audio = F.pad(audio, (0, padding))
156 |         stft = torch.stft(
157 |             audio, self.n_fft, S3_HOP,
158 |             window=self.window.to(self.device),
159 |             return_complex=True
160 |         )
161 |         magnitudes = stft[..., :-1].abs()**2
162 | 
163 |         mel_spec = self._mel_filters.to(self.device) @ magnitudes
164 | 
165 |         log_spec = torch.clamp(mel_spec, min=1e-10).log10()
166 |         log_spec = torch.maximum(log_spec, log_spec.max() - 8.0)
167 |         log_spec = (log_spec + 4.0) / 4.0
168 |         return log_spec
169 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/__init__.py:
--------------------------------------------------------------------------------
1 | from .t3 import T3
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/inference/alignment_stream_analyzer.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2025 Resemble AI
  2 | # Author: John Meade, Jeremy Hsu
  3 | # MIT License
  4 | import logging
  5 | import torch
  6 | from dataclasses import dataclass
  7 | from types import MethodType
  8 | 
  9 | 
 10 | logger = logging.getLogger(__name__)
 11 | 
 12 | 
 13 | @dataclass
 14 | class AlignmentAnalysisResult:
 15 |     # was this frame detected as being part of a noisy beginning chunk with potential hallucinations?
 16 |     false_start: bool
 17 |     # was this frame detected as being part of a long tail with potential hallucinations?
 18 |     long_tail: bool
 19 |     # was this frame detected as repeating existing text content?
 20 |     repetition: bool
 21 |     # was the alignment position of this frame too far from the previous frame?
 22 |     discontinuity: bool
 23 |     # has inference reached the end of the text tokens? eg, this remains false if inference stops early
 24 |     complete: bool
 25 |     # approximate position in the text token sequence. Can be used for generating online timestamps.
 26 |     position: int
 27 | 
 28 | 
 29 | class AlignmentStreamAnalyzer:
 30 |     def __init__(self, tfmr, queue, text_tokens_slice, alignment_layer_idx=9, eos_idx=0):
 31 |         """
 32 |         Some transformer TTS models implicitly solve text-speech alignment in one or more of their self-attention
 33 |         activation maps. This module exploits this to perform online integrity checks which streaming.
 34 |         A hook is injected into the specified attention layer, and heuristics are used to determine alignment
 35 |         position, repetition, etc.
 36 | 
 37 |         NOTE: currently requires no queues.
 38 |         """
 39 |         # self.queue = queue
 40 |         self.text_tokens_slice = (i, j) = text_tokens_slice
 41 |         self.eos_idx = eos_idx
 42 |         self.alignment = torch.zeros(0, j-i)
 43 |         # self.alignment_bin = torch.zeros(0, j-i)
 44 |         self.curr_frame_pos = 0
 45 |         self.text_position = 0
 46 | 
 47 |         self.started = False
 48 |         self.started_at = None
 49 | 
 50 |         self.complete = False
 51 |         self.completed_at = None
 52 | 
 53 |         # Using `output_attentions=True` is incompatible with optimized attention kernels, so
 54 |         # using it for all layers slows things down too much. We can apply it to just one layer
 55 |         # by intercepting the kwargs and adding a forward hook (credit: jrm)
 56 |         self.last_aligned_attn = None
 57 |         self._add_attention_spy(tfmr, alignment_layer_idx)
 58 | 
 59 |     def _add_attention_spy(self, tfmr, alignment_layer_idx):
 60 |         """
 61 |         Adds a forward hook to a specific attention layer to collect outputs.
 62 |         Using `output_attentions=True` is incompatible with optimized attention kernels, so
 63 |         using it for all layers slows things down too much.
 64 |         (credit: jrm)
 65 |         """
 66 | 
 67 |         def attention_forward_hook(module, input, output):
 68 |             """
 69 |             See `LlamaAttention.forward`; the output is a 3-tuple: `attn_output, attn_weights, past_key_value`.
 70 |             NOTE:
 71 |             - When `output_attentions=True`, `LlamaSdpaAttention.forward` calls `LlamaAttention.forward`.
 72 |             - `attn_output` has shape [B, H, T0, T0] for the 0th entry, and [B, H, 1, T0+i] for the rest i-th.
 73 |             """
 74 |             step_attention = output[1].cpu() # (B, 16, N, N)
 75 |             self.last_aligned_attn = step_attention[0].mean(0) # (N, N)
 76 | 
 77 |         target_layer = tfmr.layers[alignment_layer_idx].self_attn
 78 |         hook_handle = target_layer.register_forward_hook(attention_forward_hook)
 79 | 
 80 |         # Backup original forward
 81 |         original_forward = target_layer.forward
 82 |         def patched_forward(self, *args, **kwargs):
 83 |             kwargs['output_attentions'] = True
 84 |             return original_forward(*args, **kwargs)
 85 | 
 86 |         # TODO: how to unpatch it?
 87 |         target_layer.forward = MethodType(patched_forward, target_layer)
 88 | 
 89 |     def step(self, logits):
 90 |         """
 91 |         Emits an AlignmentAnalysisResult into the output queue, and potentially modifies the logits to force an EOS.
 92 |         """
 93 |         # extract approximate alignment matrix chunk (1 frame at a time after the first chunk)
 94 |         aligned_attn = self.last_aligned_attn # (N, N)
 95 |         i, j = self.text_tokens_slice
 96 |         if self.curr_frame_pos == 0:
 97 |             # first chunk has conditioning info, text tokens, and BOS token
 98 |             A_chunk = aligned_attn[j:, i:j].clone().cpu() # (T, S)
 99 |         else:
100 |             # subsequent chunks have 1 frame due to KV-caching
101 |             A_chunk = aligned_attn[:, i:j].clone().cpu() # (1, S)
102 | 
103 |         # TODO: monotonic masking; could have issue b/c spaces are often skipped.
104 |         A_chunk[:, self.curr_frame_pos + 1:] = 0
105 | 
106 | 
107 |         self.alignment = torch.cat((self.alignment, A_chunk), dim=0)
108 | 
109 |         A = self.alignment
110 |         T, S = A.shape
111 | 
112 |         # update position
113 |         cur_text_posn = A_chunk[-1].argmax()
114 |         discontinuity = not(-4 < cur_text_posn - self.text_position < 7) # NOTE: very lenient!
115 |         if not discontinuity:
116 |             self.text_position = cur_text_posn
117 | 
118 |         # Hallucinations at the start of speech show up as activations at the bottom of the attention maps!
119 |         # To mitigate this, we just wait until there are no activations far off-diagonal in the last 2 tokens,
120 |         # and there are some strong activations in the first few tokens.
121 |         false_start = (not self.started) and (A[-2:, -2:].max() > 0.1 or A[:, :4].max() < 0.5)
122 |         self.started = not false_start
123 |         if self.started and self.started_at is None:
124 |             self.started_at = T
125 | 
126 |         # Is generation likely complete?
127 |         self.complete = self.complete or self.text_position >= S - 3
128 |         if self.complete and self.completed_at is None:
129 |             self.completed_at = T
130 | 
131 |         # NOTE: EOS rarely assigned activations, and second-last token is often punctuation, so use last 3 tokens.
132 |         # NOTE: due to the false-start behaviour, we need to make sure we skip activations for the first few tokens.
133 |         last_text_token_duration = A[15:, -3:].sum()
134 | 
135 |         # Activations for the final token that last too long are likely hallucinations.
136 |         long_tail = self.complete and (A[self.completed_at:, -3:].sum(dim=0).max() >= 10) # 400ms
137 | 
138 |         # If there are activations in previous tokens after generation has completed, assume this is a repetition error.
139 |         repetition = self.complete and (A[self.completed_at:, :-5].max(dim=1).values.sum() > 5)
140 | 
141 |         # If a bad ending is detected, force emit EOS by modifying logits
142 |         # NOTE: this means logits may be inconsistent with latents!
143 |         if long_tail or repetition:
144 |             logger.warn(f"forcing EOS token, {long_tail=}, {repetition=}")
145 |             # (±2**15 is safe for all dtypes >= 16bit)
146 |             logits = -(2**15) * torch.ones_like(logits)
147 |             logits[..., self.eos_idx] = 2**15
148 | 
149 |         # Suppress EoS to prevent early termination
150 |         if cur_text_posn < S - 3: # FIXME: arbitrary
151 |             logits[..., self.eos_idx] = -2**15
152 | 
153 |         self.curr_frame_pos += 1
154 |         return logits
155 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/inference/t3_hf_backend.py:
--------------------------------------------------------------------------------
  1 | from typing import Optional
  2 | 
  3 | import torch
  4 | from torch import nn as nn
  5 | from transformers import LlamaConfig, LlamaModel, LlamaPreTrainedModel, GenerationMixin
  6 | from transformers.modeling_outputs import CausalLMOutputWithCrossAttentions
  7 | 
  8 | 
  9 | class T3HuggingfaceBackend(LlamaPreTrainedModel, GenerationMixin):
 10 |     """
 11 |     Override some HuggingFace interface methods so we can use the standard `generate` method with our
 12 |     custom embedding / logit layers.
 13 | 
 14 |     NOTE: need to extend "*PreTrainedModel" to avoid re-initializing weights!
 15 |     """
 16 | 
 17 |     def __init__(
 18 |         self,
 19 |         config: LlamaConfig,
 20 |         llama: LlamaModel,
 21 |         *,
 22 |         speech_enc,
 23 |         speech_head,
 24 |         latents_queue=None,
 25 |         logits_queue=None,
 26 |         alignment_stream_analyzer: 'AlignmentStreamAnalyzer'=None,
 27 |     ):
 28 |         super().__init__(config)
 29 |         self.model = llama
 30 |         self.speech_enc = speech_enc
 31 |         self.speech_head = speech_head
 32 |         self._added_cond = False
 33 |         self.alignment_stream_analyzer = alignment_stream_analyzer
 34 | 
 35 |     @torch.inference_mode()
 36 |     def prepare_inputs_for_generation(
 37 |         self, input_ids: torch.Tensor, decoder_cond: torch.Tensor, use_cache: bool, past_key_values=None,
 38 |         # This argument was introduced in some recent version of transformers (>=4.29.1)
 39 |         cache_position=None
 40 |     ):
 41 |         """
 42 |         This is a method used by huggingface's generate() method.
 43 |         Overridden here to apply our custom speech token embedding layer.
 44 | 
 45 |         :param input_ids: (B, S) int64 tensors of input tokens.
 46 |         :param decoder_cond: (B, T, C) float32 tensor of conditioning (prefixed to <input_embeds>)
 47 |         """
 48 | 
 49 |         # Make use of the kv cache: only the last input ID is new, we trim away all the ones before
 50 |         if not use_cache:
 51 |             past_key_values = None
 52 |         if past_key_values is not None:
 53 |             input_ids = input_ids[:, -1:]
 54 | 
 55 |         # custom speech token embedding layer
 56 |         inputs_embeds = self.speech_enc(input_ids)
 57 | 
 58 |         # prefix decoder conditioning if applicable
 59 |         if not self._added_cond:
 60 |             assert past_key_values is not None # should be first step
 61 |             if decoder_cond.size(0) != inputs_embeds.size(0):
 62 |                 decoder_cond = decoder_cond.expand(inputs_embeds.size(0), -1, -1)
 63 |             inputs_embeds = torch.cat([decoder_cond, inputs_embeds], dim=1)
 64 |             self._added_cond = True
 65 | 
 66 |         return {
 67 |             "inputs_embeds": inputs_embeds,
 68 |             "past_key_values": past_key_values,
 69 |             "use_cache": use_cache,
 70 |         }
 71 | 
 72 |     @torch.inference_mode()
 73 |     def forward(
 74 |         self,
 75 |         inputs_embeds: torch.Tensor,
 76 |         past_key_values: Optional[torch.Tensor]=None,
 77 |         use_cache=True,
 78 |         output_attentions=False,
 79 |         output_hidden_states=True,
 80 |         return_dict=True,
 81 |     ):
 82 |         """
 83 |         This is a method used by huggingface's generate() method.
 84 |         Overridden here to apply our custom layer norm and speech logit projection layers.
 85 | 
 86 |         :param inputs_embeds: (B, S, C) float32 tensor of conditioning inputs. If past key values are given,
 87 |         S should be 1.
 88 |         """
 89 |         is_large_input = inputs_embeds.size(1) != 1
 90 |         has_cache = past_key_values is not None and len(past_key_values) > 0
 91 |         assert not (is_large_input and has_cache)
 92 |         assert return_dict
 93 |         assert output_hidden_states
 94 | 
 95 |         tfmr_out = self.model(
 96 |             inputs_embeds=inputs_embeds,
 97 |             past_key_values=past_key_values,
 98 |             use_cache=use_cache,
 99 |             output_attentions=output_attentions,
100 |             output_hidden_states=output_hidden_states,
101 |             return_dict=True,
102 |         )
103 |         hidden_states = tfmr_out.hidden_states[-1]  # (B, seq, dim)
104 | 
105 |         logits = self.speech_head(hidden_states)
106 |         # assert inputs_embeds.size(0) == 1 # (disabled for CFG)
107 | 
108 |         # NOTE: hallucination handler may modify logits to force emit an EOS token
109 |         # logits = self.alignment_stream_analyzer.step(logits)
110 | 
111 |         return CausalLMOutputWithCrossAttentions(
112 |             logits=logits,
113 |             past_key_values=tfmr_out.past_key_values,
114 |             hidden_states=tfmr_out.hidden_states,
115 |             attentions=tfmr_out.attentions,
116 |         )
117 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/llama_configs.py:
--------------------------------------------------------------------------------
 1 | LLAMA_520M_CONFIG_DICT = dict(
 2 |     # Arbitrary small number that won't cause problems when loading.
 3 |     # These param are unused due to custom input layers.
 4 |     vocab_size=8,
 5 |     # default params needed for loading most pretrained 1B weights
 6 |     max_position_embeddings=131072,
 7 |     hidden_size=1024,
 8 |     intermediate_size=4096,
 9 |     num_hidden_layers=30,
10 |     num_attention_heads=16,
11 |     attn_implementation="sdpa",
12 |     head_dim=64,
13 |     tie_word_embeddings=False,
14 |     hidden_act="silu",
15 |     attention_bias=False,
16 |     attention_dropout=0.0,
17 |     initializer_range=0.02,
18 |     mlp_bias=False,
19 |     model_type="llama",
20 |     num_key_value_heads=16,
21 |     pretraining_tp=1,
22 |     rms_norm_eps=1e-05,
23 |     rope_scaling=dict(
24 |         factor=8.0,
25 |         high_freq_factor=4.0,
26 |         low_freq_factor=1.0,
27 |         original_max_position_embeddings=8192,
28 |         rope_type="llama3"
29 |     ),
30 |     rope_theta=500000.0,
31 |     torch_dtype="bfloat16",
32 |     use_cache=True,
33 | )
34 | 
35 | LLAMA_CONFIGS = {
36 |     "Llama_520M": LLAMA_520M_CONFIG_DICT,
37 | }
38 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/cond_enc.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass
 2 | from typing import Optional
 3 | 
 4 | import torch
 5 | from torch import nn, Tensor
 6 | 
 7 | from .perceiver import Perceiver
 8 | from .t3_config import T3Config
 9 | 
10 | 
11 | @dataclass
12 | class T3Cond:
13 |     """
14 |     Dataclass container for most / all conditioning info.
15 |     TODO: serialization methods aren't used, keeping them around for convenience
16 |     """
17 | 
18 |     speaker_emb: Tensor
19 |     clap_emb: Optional[Tensor] = None
20 |     cond_prompt_speech_tokens: Optional[Tensor] = None
21 |     cond_prompt_speech_emb: Optional[Tensor] = None
22 |     emotion_adv: Optional[Tensor] = 0.5
23 | 
24 |     def to(self, *, device=None, dtype=None):
25 |         "Cast to a device and dtype. Dtype casting is ignored for long/int tensors."
26 |         for k, v in self.__dict__.items():
27 |             if torch.is_tensor(v):
28 |                 is_fp = type(v.view(-1)[0].item()) is not int
29 |                 setattr(self, k, v.to(device=device, dtype=dtype if is_fp else None))
30 |         return self
31 | 
32 |     def save(self, fpath):
33 |         torch.save(self.__dict__, fpath)
34 | 
35 |     @staticmethod
36 |     def load(fpath, map_location="cpu"):
37 |         kwargs = torch.load(fpath, map_location=map_location, weights_only=True)
38 |         return T3Cond(**kwargs)
39 | 
40 | 
41 | class T3CondEnc(nn.Module):
42 |     """
43 |     Handle all non-text conditioning, like speaker embeddings / prompts, CLAP, emotion, etc.
44 |     """
45 | 
46 |     def __init__(self, hp: T3Config):
47 |         super().__init__()
48 |         self.hp = hp
49 |         if hp.encoder_type == "voice_encoder":
50 |             self.spkr_enc = nn.Linear(hp.speaker_embed_size, hp.n_channels)
51 |         else:
52 |             raise NotImplementedError(str(hp.encoder_type))
53 | 
54 |         # emotion adv
55 |         self.emotion_adv_fc = None
56 |         if hp.emotion_adv:
57 |             self.emotion_adv_fc = nn.Linear(1, hp.n_channels, bias=False)
58 | 
59 |         # perceiver resampler
60 |         self.perceiver = None
61 |         if hp.use_perceiver_resampler:
62 |             self.perceiver = Perceiver()
63 | 
64 |     def forward(self, cond: T3Cond):
65 |         # Validate
66 |         assert (cond.cond_prompt_speech_tokens is None) == (cond.cond_prompt_speech_emb is None), \
67 |             "no embeddings for cond_prompt_speech_tokens"
68 | 
69 |         # Speaker embedding projection
70 |         cond_spkr = self.spkr_enc(cond.speaker_emb.view(-1, self.hp.speaker_embed_size))[:, None]  # (B, 1, dim)
71 |         empty = torch.zeros_like(cond_spkr[:, :0])  # (B, 0, dim)
72 | 
73 |         # TODO CLAP
74 |         assert cond.clap_emb is None, "clap_embed not implemented"
75 |         cond_clap = empty  # (B, 0, dim)
76 | 
77 |         # Cond prompt
78 |         cond_prompt_speech_emb = cond.cond_prompt_speech_emb
79 |         if cond_prompt_speech_emb is None:
80 |             cond_prompt_speech_emb = empty  # (B, 0, dim)
81 |         elif self.hp.use_perceiver_resampler:
82 |             cond_prompt_speech_emb = self.perceiver(cond_prompt_speech_emb)
83 | 
84 |         # Emotion Adv: must provide a value if this model uses emotion conditioning
85 |         cond_emotion_adv = empty  # (B, 0, dim)
86 |         if self.hp.emotion_adv:
87 |             assert cond.emotion_adv is not None
88 |             cond_emotion_adv = self.emotion_adv_fc(cond.emotion_adv.view(-1, 1, 1))
89 | 
90 |         # Concat and return
91 |         cond_embeds = torch.cat((
92 |             cond_spkr,
93 |             cond_clap,
94 |             cond_prompt_speech_emb,
95 |             cond_emotion_adv,
96 |         ), dim=1)
97 |         return cond_embeds
98 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/learned_pos_emb.py:
--------------------------------------------------------------------------------
 1 | from typing import Union
 2 | 
 3 | import torch
 4 | from torch import nn, Tensor
 5 | 
 6 | 
 7 | class LearnedPositionEmbeddings(nn.Module):
 8 |     def __init__(self, seq_len, model_dim, init=.02):
 9 |         super().__init__()
10 |         self.emb = nn.Embedding(seq_len, model_dim)
11 |         # Initializing this way is standard for GPT-2
12 |         self.emb.weight.data.normal_(mean=0.0, std=init)
13 | 
14 |     def forward(self, x):
15 |         """
16 |         Returns positional embeddings for index 0 up to the length of x
17 |         """
18 |         sl = x.shape[1]
19 |         return self.emb(torch.arange(0, sl, device=x.device))
20 | 
21 |     def get_fixed_embedding(self, idx: 'Union[int, Tensor]'):
22 |         """
23 |         Args:
24 |             idx: scalar int or an integer tensor of shape (T,) or (B, T)
25 |         Returns:
26 |             positional embeddings for given indices, shape (B, T, dim), ie (1, 1, dim) for int input
27 |         """
28 |         device = self.emb.weight.device
29 |         idx = idx.to(device) if torch.is_tensor(idx) else torch.tensor(idx, device=device)
30 |         idx = torch.atleast_2d(idx)
31 |         assert idx.ndim == 2
32 |         return self.emb(idx)  # (B, T, dim)
33 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/perceiver.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2025 Resemble AI
  2 | # Author: Manmay Nakhashi
  3 | # MIT License
  4 | import math
  5 | 
  6 | import torch
  7 | from torch import nn
  8 | import torch.nn.functional as F
  9 | from einops import rearrange
 10 | 
 11 | 
 12 | class RelativePositionBias(nn.Module):
 13 |     def __init__(self, scale, causal=False, num_buckets=32, max_distance=128, heads=8):
 14 |         super().__init__()
 15 |         self.scale = scale
 16 |         self.causal = causal
 17 |         self.num_buckets = num_buckets
 18 |         self.max_distance = max_distance
 19 |         self.relative_attention_bias = nn.Embedding(num_buckets, heads)
 20 | 
 21 |     @staticmethod
 22 |     def _relative_position_bucket(relative_position, causal=True, num_buckets=32, max_distance=128):
 23 |         ret = 0
 24 |         n = -relative_position
 25 |         if not causal:
 26 |             num_buckets //= 2
 27 |             ret += (n < 0).long() * num_buckets
 28 |             n = torch.abs(n)
 29 |         else:
 30 |             n = torch.max(n, torch.zeros_like(n))
 31 | 
 32 |         max_exact = num_buckets // 2
 33 |         is_small = n < max_exact
 34 | 
 35 |         val_if_large = max_exact + (
 36 |                 torch.log(n.float() / max_exact) / math.log(max_distance / max_exact) * (num_buckets - max_exact)
 37 |         ).long()
 38 |         val_if_large = torch.min(val_if_large, torch.full_like(val_if_large, num_buckets - 1))
 39 | 
 40 |         ret += torch.where(is_small, n, val_if_large)
 41 |         return ret
 42 | 
 43 |     def forward(self, qk_dots):
 44 |         i, j, device = *qk_dots.shape[-2:], qk_dots.device
 45 |         q_pos = torch.arange(i, dtype=torch.long, device=device)
 46 |         k_pos = torch.arange(j, dtype=torch.long, device=device)
 47 |         rel_pos = k_pos[None, :] - q_pos[:, None]
 48 |         rp_bucket = self._relative_position_bucket(rel_pos, causal=self.causal, num_buckets=self.num_buckets,
 49 |                                                    max_distance=self.max_distance)
 50 |         values = self.relative_attention_bias(rp_bucket)
 51 |         bias = rearrange(values, 'i j h -> () h i j')
 52 |         return qk_dots + (bias * self.scale)
 53 | 
 54 | 
 55 | class AttentionQKV(nn.Module):
 56 |     def __init__(self, n_heads, head_dim, dropout_rate=0.1, scale=None, flash=False):
 57 |         super().__init__()
 58 |         self.n_heads = n_heads
 59 |         self.head_dim = head_dim
 60 |         self.scale = scale if scale is not None else head_dim ** -0.5
 61 |         self.flash = flash
 62 |         self.dropout_rate = dropout_rate
 63 |         self.dropout = nn.Dropout(dropout_rate)
 64 |         self.flash_config = self.setup_flash_config() if flash else None
 65 | 
 66 |     def setup_flash_config(self):
 67 |         # Setup flash attention configuration
 68 |         flash_config = {
 69 |             'enable_flash': True,
 70 |             'enable_math': True,
 71 |             'enable_mem_efficient': True
 72 |         }
 73 |         return flash_config
 74 | 
 75 |     def forward(self, q, k, v, mask=None):
 76 |         q, k, v = [self.split_heads(tensor) for tensor in [q, k, v]]
 77 |         if self.flash:
 78 |             out = self.flash_attention(q, k, v, mask=mask)
 79 |         else:
 80 |             out = self.scaled_dot_product_attention(q, k, v, mask=mask)
 81 | 
 82 |         return self.combine_heads(out)
 83 | 
 84 |     def scaled_dot_product_attention(self, q, k, v, mask=None):
 85 |         sim = torch.einsum("bhlt,bhls->bhts", q, k) * self.scale
 86 |         if mask is not None:
 87 |             sim = sim.masked_fill(mask == 0, float('-inf'))
 88 |         attn = torch.softmax(sim, dim=-1)
 89 |         attn = self.dropout(attn)
 90 |         return torch.einsum("bhts,bhls->bhlt", attn, v)
 91 | 
 92 |     def flash_attention(self, q, k, v, mask=None):
 93 |         config = self.flash_config if self.flash_config else {}
 94 |         with torch.backends.cuda.sdp_kernel(**config):
 95 |             out = F.scaled_dot_product_attention(
 96 |                 q, k, v,
 97 |                 attn_mask=mask,
 98 |                 dropout_p=self.dropout_rate if self.training else 0.
 99 |             )
100 |         return out
101 | 
102 |     def split_heads(self, x):
103 |         bs, length, _ = x.shape
104 |         x = x.view(bs, length, self.n_heads, self.head_dim)
105 |         return x.permute(0, 2, 1, 3)
106 | 
107 |     def combine_heads(self, x):
108 |         bs, _, length, _ = x.shape
109 |         x = x.permute(0, 2, 1, 3).contiguous()
110 |         return x.view(bs, length, -1)
111 | 
112 | 
113 | class AttentionBlock2(nn.Module):
114 |     """
115 |     An attention block that allows spatial positions to attend to each other,
116 |     using AttentionQKV and separate linear transformations for Q, K, and V.
117 |     """
118 | 
119 |     def __init__(
120 |         self,
121 |         channels,
122 |         num_heads=1,
123 |         num_head_channels=-1,
124 |         relative_pos_embeddings=False,
125 |         flash_attention=True,
126 |         dropout_rate=0.2,
127 |         scale=None
128 |     ):
129 |         super().__init__()
130 |         self.channels = channels
131 | 
132 |         if num_head_channels == -1:
133 |             self.num_heads = num_heads
134 |         else:
135 |             assert (
136 |                 channels % num_head_channels == 0
137 |             ), f"channels {channels} is not divisible by num_head_channels {num_head_channels}"
138 |             self.num_heads = channels // num_head_channels
139 | 
140 |         self.norm = nn.LayerNorm(channels)
141 | 
142 |         # Separate linear layers for Q, K, and V
143 |         self.to_q = nn.Linear(channels, channels)
144 |         self.to_k = nn.Linear(channels, channels)
145 |         self.to_v = nn.Linear(channels, channels)
146 | 
147 |         self.attention = AttentionQKV(self.num_heads, channels // self.num_heads, dropout_rate=dropout_rate, flash=flash_attention, scale=scale)
148 | 
149 |         self.proj_out = nn.Linear(channels, channels)
150 | 
151 |         if relative_pos_embeddings:
152 |             self.relative_pos_embeddings = RelativePositionBias(scale=(channels // self.num_heads) ** .5, causal=False, heads=num_heads, num_buckets=32, max_distance=64)
153 |         else:
154 |             self.relative_pos_embeddings = None
155 | 
156 |     def forward(self, x1, x2, mask=None):
157 |         b1, c1, *spatial1 = x1.shape
158 |         b2, c2, *spatial2 = x2.shape
159 | 
160 |         x1_norm = self.norm(x1)
161 |         x2_norm = self.norm(x2)
162 | 
163 |         q = self.to_q(x1_norm)
164 |         k = self.to_k(x2_norm)
165 |         v = self.to_v(x2_norm)
166 | 
167 |         h = self.attention(q, k, v, mask=mask)
168 |         h = self.proj_out(h)
169 | 
170 |         return (x1 + h).reshape(b1, c1, *spatial1)
171 | 
172 | 
173 | class Perceiver(nn.Module):
174 |     """Inspired by https://arxiv.org/abs/2103.03206"""
175 |     def __init__(self, pre_attention_query_token=32, pre_attention_query_size=1024, embedding_dim=1024, num_attn_heads=4):
176 |         """
177 |         Initialize the perceiver module.
178 | 
179 |         :param pre_attention_query_token: Number of query tokens for pre-attention
180 |         :param pre_attention_query_size: Size of each query token
181 |         :param embedding_dim: Dimension of the embedding space
182 |         :param num_attn_heads: Number of attention heads
183 |         """
184 |         super().__init__()
185 | 
186 |         # Initialize the pre-attention query parameter
187 |         self.pre_attention_query = torch.nn.Parameter(
188 |             torch.empty(1, pre_attention_query_token, pre_attention_query_size)
189 |         )
190 | 
191 |         # Calculate the variance for uniform initialization
192 |         query_variance = math.sqrt(3.0) * math.sqrt(2.0 / (pre_attention_query_token + pre_attention_query_token))
193 | 
194 |         # Initialize the pre-attention query with uniform distribution
195 |         self.pre_attention_query.data.uniform_(-query_variance, query_variance)
196 | 
197 |         # Initialize the attention block
198 |         self.attn = AttentionBlock2(embedding_dim, num_attn_heads)
199 | 
200 |     def forward(self, h):
201 |         """
202 |         Forward pass of the perceiver module.
203 |         :param h: Input tensor
204 |         :return: Output after applying attention mechanisms
205 |         """
206 |         # Expand the pre-attention query to match the batch size of the input
207 |         query_ = self.pre_attention_query.expand(h.shape[0], -1, -1)
208 |         # Apply the first attention mechanism (cross-attention)
209 |         pre_att = self.attn(query_, h)
210 |         # Apply the second attention mechanism (self-attention)
211 |         attn = self.attn(pre_att, pre_att)
212 |         return attn
213 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/t3_config.py:
--------------------------------------------------------------------------------
 1 | from ..llama_configs import LLAMA_CONFIGS
 2 | 
 3 | 
 4 | class T3Config:
 5 |     start_text_token = 255
 6 |     stop_text_token = 0
 7 |     text_tokens_dict_size = 704
 8 |     max_text_tokens = 2048
 9 | 
10 |     start_speech_token = 6561
11 |     stop_speech_token = 6562
12 |     speech_tokens_dict_size = 8194
13 |     max_speech_tokens = 4096
14 | 
15 |     llama_config_name = "Llama_520M"
16 |     input_pos_emb = "learned"
17 |     speech_cond_prompt_len = 150
18 | 
19 |     # For T3CondEnc
20 |     encoder_type = "voice_encoder"
21 |     speaker_embed_size = 256
22 |     use_perceiver_resampler = True
23 |     emotion_adv = True
24 | 
25 |     @property
26 |     def n_channels(self):
27 |         return LLAMA_CONFIGS[self.llama_config_name]["hidden_size"]
28 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/tokenizers/__init__.py:
--------------------------------------------------------------------------------
1 | from .tokenizer import EnTokenizer
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/tokenizers/tokenizer.py:
--------------------------------------------------------------------------------
 1 | import logging
 2 | 
 3 | import torch
 4 | from tokenizers import Tokenizer
 5 | 
 6 | 
 7 | # Special tokens
 8 | SOT = "[START]"
 9 | EOT = "[STOP]"
10 | UNK = "[UNK]"
11 | SPACE = "[SPACE]"
12 | SPECIAL_TOKENS = [SOT, EOT, UNK, SPACE, "[PAD]", "[SEP]", "[CLS]", "[MASK]"]
13 | 
14 | logger = logging.getLogger(__name__)
15 | 
16 | class EnTokenizer:
17 |     def __init__(self, vocab_file_path):
18 |         self.tokenizer: Tokenizer = Tokenizer.from_file(vocab_file_path)
19 |         self.check_vocabset_sot_eot()
20 | 
21 |     def check_vocabset_sot_eot(self):
22 |         voc = self.tokenizer.get_vocab()
23 |         assert SOT in voc
24 |         assert EOT in voc
25 | 
26 |     def text_to_tokens(self, text: str):
27 |         text_tokens = self.encode(text)
28 |         text_tokens = torch.IntTensor(text_tokens).unsqueeze(0)
29 |         return text_tokens
30 | 
31 |     def encode( self, txt: str, verbose=False):
32 |         """
33 |         clean_text > (append `lang_id`) > replace SPACE > encode text using Tokenizer
34 |         """
35 |         txt = txt.replace(' ', SPACE)
36 |         code = self.tokenizer.encode(txt)
37 |         ids = code.ids
38 |         return ids
39 | 
40 |     def decode(self, seq):
41 |         if isinstance(seq, torch.Tensor):
42 |             seq = seq.cpu().numpy()
43 | 
44 |         txt: str = self.tokenizer.decode(seq,
45 |         skip_special_tokens=False)
46 |         txt = txt.replace(' ', '')
47 |         txt = txt.replace(SPACE, ' ')
48 |         txt = txt.replace(EOT, '')
49 |         txt = txt.replace(UNK, '')
50 |         return txt
51 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/utils.py:
--------------------------------------------------------------------------------
1 | class AttrDict(dict):
2 |     def __init__(self, *args, **kwargs):
3 |         super(AttrDict, self).__init__(*args, **kwargs)
4 |         self.__dict__ = self
5 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/__init__.py:
--------------------------------------------------------------------------------
1 | from .voice_encoder import VoiceEncoder, VoiceEncConfig
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/config.py:
--------------------------------------------------------------------------------
 1 | class VoiceEncConfig:
 2 |     num_mels = 40
 3 |     sample_rate = 16000
 4 |     speaker_embed_size = 256
 5 |     ve_hidden_size = 256
 6 |     flatten_lstm_params = False
 7 |     n_fft = 400
 8 |     hop_size = 160
 9 |     win_size = 400
10 |     fmax = 8000
11 |     fmin = 0
12 |     preemphasis = 0.
13 |     mel_power = 2.0
14 |     mel_type = "amp"
15 |     normalized_mels = False
16 |     ve_partial_frames = 160
17 |     ve_final_relu = True
18 |     stft_magnitude_min = 1e-4
19 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/melspec.py:
--------------------------------------------------------------------------------
 1 | from functools import lru_cache
 2 | 
 3 | from scipy import signal
 4 | import numpy as np
 5 | import librosa
 6 | 
 7 | 
 8 | @lru_cache()
 9 | def mel_basis(hp):
10 |     assert hp.fmax <= hp.sample_rate // 2
11 |     return librosa.filters.mel(
12 |         sr=hp.sample_rate,
13 |         n_fft=hp.n_fft,
14 |         n_mels=hp.num_mels,
15 |         fmin=hp.fmin,
16 |         fmax=hp.fmax)  # -> (nmel, nfreq)
17 | 
18 | 
19 | def preemphasis(wav, hp):
20 |     assert hp.preemphasis != 0
21 |     wav = signal.lfilter([1, -hp.preemphasis], [1], wav)
22 |     wav = np.clip(wav, -1, 1)
23 |     return wav
24 | 
25 | 
26 | def melspectrogram(wav, hp, pad=True):
27 |     # Run through pre-emphasis
28 |     if hp.preemphasis > 0:
29 |         wav = preemphasis(wav, hp)
30 |         assert np.abs(wav).max() - 1 < 1e-07
31 | 
32 |     # Do the stft
33 |     spec_complex = _stft(wav, hp, pad=pad)
34 | 
35 |     # Get the magnitudes
36 |     spec_magnitudes = np.abs(spec_complex)
37 | 
38 |     if hp.mel_power != 1.0:
39 |         spec_magnitudes **= hp.mel_power
40 | 
41 |     # Get the mel and convert magnitudes->db
42 |     mel = np.dot(mel_basis(hp), spec_magnitudes)
43 |     if hp.mel_type == "db":
44 |         mel = _amp_to_db(mel, hp)
45 | 
46 |     # Normalise the mel from db to 0,1
47 |     if hp.normalized_mels:
48 |         mel = _normalize(mel, hp).astype(np.float32)
49 | 
50 |     assert not pad or mel.shape[1] == 1 + len(wav) // hp.hop_size   # Sanity check
51 |     return mel   # (M, T)
52 | 
53 | 
54 | def _stft(y, hp, pad=True):
55 |     # NOTE: after 0.8, pad mode defaults to constant, setting this to reflect for
56 |     #   historical consistency and streaming-version consistency
57 |     return librosa.stft(
58 |         y,
59 |         n_fft=hp.n_fft,
60 |         hop_length=hp.hop_size,
61 |         win_length=hp.win_size,
62 |         center=pad,
63 |         pad_mode="reflect",
64 |     )
65 | 
66 | 
67 | def _amp_to_db(x, hp):
68 |     return 20 * np.log10(np.maximum(hp.stft_magnitude_min, x))
69 | 
70 | 
71 | def _db_to_amp(x):
72 |     return np.power(10.0, x * 0.05)
73 | 
74 | 
75 | def _normalize(s, hp, headroom_db=15):
76 |     min_level_db = 20 * np.log10(hp.stft_magnitude_min)
77 |     s = (s - min_level_db) / (-min_level_db + headroom_db)
78 |     return s
79 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/voice_encoder.py:
--------------------------------------------------------------------------------
  1 | # Adapted from https://github.com/CorentinJ/Real-Time-Voice-Cloning
  2 | # MIT License
  3 | from typing import List, Union, Optional
  4 | 
  5 | import numpy as np
  6 | from numpy.lib.stride_tricks import as_strided
  7 | import librosa
  8 | import torch
  9 | import torch.nn.functional as F
 10 | from torch import nn, Tensor
 11 | 
 12 | from .config import VoiceEncConfig
 13 | from .melspec import melspectrogram
 14 | 
 15 | 
 16 | def pack(arrays, seq_len: int=None, pad_value=0):
 17 |     """
 18 |     Given a list of length B of array-like objects of shapes (Ti, ...), packs them in a single tensor of
 19 |     shape (B, T, ...) by padding each individual array on the right.
 20 | 
 21 |     :param arrays: a list of array-like objects of matching shapes except for the first axis.
 22 |     :param seq_len: the value of T. It must be the maximum of the lengths Ti of the arrays at
 23 |     minimum. Will default to that value if None.
 24 |     :param pad_value: the value to pad the arrays with.
 25 |     :return: a (B, T, ...) tensor
 26 |     """
 27 |     if seq_len is None:
 28 |         seq_len = max(len(array) for array in arrays)
 29 |     else:
 30 |         assert seq_len >= max(len(array) for array in arrays)
 31 | 
 32 |     # Convert lists to np.array
 33 |     if isinstance(arrays[0], list):
 34 |         arrays = [np.array(array) for array in arrays]
 35 | 
 36 |     # Convert to tensor and handle device
 37 |     device = None
 38 |     if isinstance(arrays[0], torch.Tensor):
 39 |         tensors = arrays
 40 |         device = tensors[0].device
 41 |     else:
 42 |         tensors = [torch.as_tensor(array) for array in arrays]
 43 | 
 44 |     # Fill the packed tensor with the array data
 45 |     packed_shape = (len(tensors), seq_len, *tensors[0].shape[1:])
 46 |     packed_tensor = torch.full(packed_shape, pad_value, dtype=tensors[0].dtype, device=device)
 47 | 
 48 |     for i, tensor in enumerate(tensors):
 49 |         packed_tensor[i, :tensor.size(0)] = tensor
 50 | 
 51 |     return packed_tensor
 52 | 
 53 | 
 54 | def get_num_wins(
 55 |     n_frames: int,
 56 |     step: int,
 57 |     min_coverage: float,
 58 |     hp: VoiceEncConfig,
 59 | ):
 60 |     assert n_frames > 0
 61 |     win_size = hp.ve_partial_frames
 62 |     n_wins, remainder = divmod(max(n_frames - win_size + step, 0), step)
 63 |     if n_wins == 0 or (remainder + (win_size - step)) / win_size >= min_coverage:
 64 |         n_wins += 1
 65 |     target_n = win_size + step * (n_wins - 1)
 66 |     return n_wins, target_n
 67 | 
 68 | 
 69 | def get_frame_step(
 70 |     overlap: float,
 71 |     rate: float,
 72 |     hp: VoiceEncConfig,
 73 | ):
 74 |     # Compute how many frames separate two partial utterances
 75 |     assert 0 <= overlap < 1
 76 |     if rate is None:
 77 |         frame_step = int(np.round(hp.ve_partial_frames * (1 - overlap)))
 78 |     else:
 79 |         frame_step = int(np.round((hp.sample_rate / rate) / hp.ve_partial_frames))
 80 |     assert 0 < frame_step <= hp.ve_partial_frames
 81 |     return frame_step
 82 | 
 83 | 
 84 | def stride_as_partials(
 85 |     mel: np.ndarray,
 86 |     hp: VoiceEncConfig,
 87 |     overlap=0.5,
 88 |     rate: float=None,
 89 |     min_coverage=0.8,
 90 | ):
 91 |     """
 92 |     Takes unscaled mels in (T, M) format
 93 |     TODO: doc
 94 |     """
 95 |     assert 0 < min_coverage <= 1
 96 |     frame_step = get_frame_step(overlap, rate, hp)
 97 | 
 98 |     # Compute how many partials can fit in the mel
 99 |     n_partials, target_len = get_num_wins(len(mel), frame_step, min_coverage, hp)
100 | 
101 |     # Trim or pad the mel spectrogram to match the number of partials
102 |     if target_len > len(mel):
103 |         mel = np.concatenate((mel, np.full((target_len - len(mel), hp.num_mels), 0)))
104 |     elif target_len < len(mel):
105 |         mel = mel[:target_len]
106 | 
107 |     # Ensure the numpy array data is float32 and contiguous in memory
108 |     mel = mel.astype(np.float32, order="C")
109 | 
110 |     # Re-arrange the array in memory to be of shape (N, P, M) with partials overlapping eachother,
111 |     # where N is the number of partials, P is the number of frames of each partial and M the
112 |     # number of channels of the mel spectrograms.
113 |     shape = (n_partials, hp.ve_partial_frames, hp.num_mels)
114 |     strides = (mel.strides[0] * frame_step, mel.strides[0], mel.strides[1])
115 |     partials = as_strided(mel, shape, strides)
116 |     return partials
117 | 
118 | 
119 | class VoiceEncoder(nn.Module):
120 |     def __init__(self, hp=VoiceEncConfig()):
121 |         super().__init__()
122 | 
123 |         self.hp = hp
124 | 
125 |         # Network definition
126 |         self.lstm = nn.LSTM(self.hp.num_mels, self.hp.ve_hidden_size, num_layers=3, batch_first=True)
127 |         if hp.flatten_lstm_params:
128 |             self.lstm.flatten_parameters()
129 |         self.proj = nn.Linear(self.hp.ve_hidden_size, self.hp.speaker_embed_size)
130 | 
131 |         # Cosine similarity scaling (fixed initial parameter values)
132 |         self.similarity_weight = nn.Parameter(torch.tensor([10.]), requires_grad=True)
133 |         self.similarity_bias = nn.Parameter(torch.tensor([-5.]), requires_grad=True)
134 | 
135 |     @property
136 |     def device(self):
137 |         return next(self.parameters()).device
138 | 
139 |     def forward(self, mels: torch.FloatTensor):
140 |         """
141 |         Computes the embeddings of a batch of partial utterances.
142 | 
143 |         :param mels: a batch of unscaled mel spectrograms of same duration as a float32 tensor
144 |         of shape (B, T, M) where T is hp.ve_partial_frames
145 |         :return: the embeddings as a float32 tensor of shape (B, E) where E is
146 |         hp.speaker_embed_size. Embeddings are L2-normed and thus lay in the range [-1, 1].
147 |         """
148 |         if self.hp.normalized_mels and (mels.min() < 0 or mels.max() > 1):
149 |             raise Exception(f"Mels outside [0, 1]. Min={mels.min()}, Max={mels.max()}")
150 | 
151 |         # Pass the input through the LSTM layers
152 |         _, (hidden, _) = self.lstm(mels)
153 | 
154 |         # Project the final hidden state
155 |         raw_embeds = self.proj(hidden[-1])
156 |         if self.hp.ve_final_relu:
157 |             raw_embeds = F.relu(raw_embeds)
158 | 
159 |         # L2 normalize the embeddings.
160 |         return raw_embeds / torch.linalg.norm(raw_embeds, dim=1, keepdim=True)
161 | 
162 |     def inference(self, mels: torch.Tensor, mel_lens, overlap=0.5, rate: float=None, min_coverage=0.8, batch_size=None):
163 |         """
164 |         Computes the embeddings of a batch of full utterances with gradients.
165 | 
166 |         :param mels: (B, T, M) unscaled mels
167 |         :return: (B, E) embeddings on CPU
168 |         """
169 |         mel_lens = mel_lens.tolist() if torch.is_tensor(mel_lens) else mel_lens
170 | 
171 |         # Compute where to split the utterances into partials
172 |         frame_step = get_frame_step(overlap, rate, self.hp)
173 |         n_partials, target_lens = zip(*(get_num_wins(l, frame_step, min_coverage, self.hp) for l in mel_lens))
174 | 
175 |         # Possibly pad the mels to reach the target lengths
176 |         len_diff = max(target_lens) - mels.size(1)
177 |         if len_diff > 0:
178 |             pad = torch.full((mels.size(0), len_diff, self.hp.num_mels), 0, dtype=torch.float32)
179 |             mels = torch.cat((mels, pad.to(mels.device)), dim=1)
180 | 
181 |         # Group all partials together so that we can batch them easily
182 |         partials = [
183 |             mel[i * frame_step: i * frame_step + self.hp.ve_partial_frames]
184 |             for mel, n_partial in zip(mels, n_partials) for i in range(n_partial)
185 |         ]
186 |         assert all(partials[0].shape == partial.shape for partial in partials)
187 |         partials = torch.stack(partials)
188 | 
189 |         # Forward the partials
190 |         n_chunks = int(np.ceil(len(partials) / (batch_size or len(partials))))
191 |         partial_embeds = torch.cat([self(batch) for batch in partials.chunk(n_chunks)], dim=0).cpu()
192 | 
193 |         # Reduce the partial embeds into full embeds and L2-normalize them
194 |         slices = np.concatenate(([0], np.cumsum(n_partials)))
195 |         raw_embeds = [torch.mean(partial_embeds[start:end], dim=0) for start, end in zip(slices[:-1], slices[1:])]
196 |         raw_embeds = torch.stack(raw_embeds)
197 |         embeds = raw_embeds / torch.linalg.norm(raw_embeds, dim=1, keepdim=True)
198 | 
199 |         return embeds
200 | 
201 |     @staticmethod
202 |     def utt_to_spk_embed(utt_embeds: np.ndarray):
203 |         """
204 |         Takes an array of L2-normalized utterance embeddings, computes the mean embedding and L2-normalize it to get a
205 |         speaker embedding.
206 |         """
207 |         assert utt_embeds.ndim == 2
208 |         utt_embeds = np.mean(utt_embeds, axis=0)
209 |         return utt_embeds / np.linalg.norm(utt_embeds, 2)
210 | 
211 |     @staticmethod
212 |     def voice_similarity(embeds_x: np.ndarray, embeds_y: np.ndarray):
213 |         """
214 |         Cosine similarity for L2-normalized utterance embeddings or speaker embeddings
215 |         """
216 |         embeds_x = embeds_x if embeds_x.ndim == 1 else VoiceEncoder.utt_to_spk_embed(embeds_x)
217 |         embeds_y = embeds_y if embeds_y.ndim == 1 else VoiceEncoder.utt_to_spk_embed(embeds_y)
218 |         return embeds_x @ embeds_y
219 | 
220 |     def embeds_from_mels(
221 |         self, mels: Union[Tensor, List[np.ndarray]], mel_lens=None, as_spk=False, batch_size=32, **kwargs
222 |     ):
223 |         """
224 |         Convenience function for deriving utterance or speaker embeddings from mel spectrograms.
225 | 
226 |         :param mels: unscaled mels strictly within [0, 1] as either a (B, T, M) tensor or a list of (Ti, M) arrays.
227 |         :param mel_lens: if passing mels as a tensor, individual mel lengths
228 |         :param as_spk: whether to return utterance embeddings or a single speaker embedding
229 |         :param kwargs: args for inference()
230 | 
231 |         :returns: embeds as a (B, E) float32 numpy array if <as_spk> is False, else as a (E,) array
232 |         """
233 |         # Load mels in memory and pack them
234 |         if isinstance(mels, List):
235 |             mels = [np.asarray(mel) for mel in mels]
236 |             assert all(m.shape[1] == mels[0].shape[1] for m in mels), "Mels aren't in (B, T, M) format"
237 |             mel_lens = [mel.shape[0] for mel in mels]
238 |             mels = pack(mels)
239 | 
240 |         # Embed them
241 |         with torch.inference_mode():
242 |             utt_embeds = self.inference(mels.to(self.device), mel_lens, batch_size=batch_size, **kwargs).numpy()
243 | 
244 |         return self.utt_to_spk_embed(utt_embeds) if as_spk else utt_embeds
245 | 
246 |     def embeds_from_wavs(
247 |         self,
248 |         wavs: List[np.ndarray],
249 |         sample_rate,
250 |         as_spk=False,
251 |         batch_size=32,
252 |         trim_top_db: Optional[float]=20,
253 |         **kwargs
254 |     ):
255 |         """
256 |         Wrapper around embeds_from_mels
257 | 
258 |         :param trim_top_db: this argument was only added for the sake of compatibility with metavoice's implementation
259 |         """
260 |         if sample_rate != self.hp.sample_rate:
261 |             wavs = [
262 |                 librosa.resample(wav, orig_sr=sample_rate, target_sr=self.hp.sample_rate, res_type="kaiser_fast")
263 |                 for wav in wavs
264 |             ]
265 | 
266 |         if trim_top_db:
267 |             wavs = [librosa.effects.trim(wav, top_db=trim_top_db)[0] for wav in wavs]
268 | 
269 |         if "rate" not in kwargs:
270 |             kwargs["rate"] = 1.3  # Resemble's default value.
271 | 
272 |         mels = [melspectrogram(w, self.hp).T for w in wavs]
273 | 
274 |         return self.embeds_from_mels(mels, as_spk=as_spk, batch_size=batch_size, **kwargs)
275 | 


--------------------------------------------------------------------------------
/src/chatterbox/tts.py:
--------------------------------------------------------------------------------
  1 | from dataclasses import dataclass
  2 | from pathlib import Path
  3 | 
  4 | import librosa
  5 | import torch
  6 | import perth
  7 | import torch.nn.functional as F
  8 | from huggingface_hub import hf_hub_download
  9 | from safetensors.torch import load_file
 10 | 
 11 | from .models.t3 import T3
 12 | from .models.s3tokenizer import S3_SR, drop_invalid_tokens
 13 | from .models.s3gen import S3GEN_SR, S3Gen
 14 | from .models.tokenizers import EnTokenizer
 15 | from .models.voice_encoder import VoiceEncoder
 16 | from .models.t3.modules.cond_enc import T3Cond
 17 | 
 18 | 
 19 | REPO_ID = "ResembleAI/chatterbox"
 20 | 
 21 | 
 22 | def punc_norm(text: str) -> str:
 23 |     """
 24 |         Quick cleanup func for punctuation from LLMs or
 25 |         containing chars not seen often in the dataset
 26 |     """
 27 |     if len(text) == 0:
 28 |         return "You need to add some text for me to talk."
 29 | 
 30 |     # Capitalise first letter
 31 |     if text[0].islower():
 32 |         text = text[0].upper() + text[1:]
 33 | 
 34 |     # Remove multiple space chars
 35 |     text = " ".join(text.split())
 36 | 
 37 |     # Replace uncommon/llm punc
 38 |     punc_to_replace = [
 39 |         ("...", ", "),
 40 |         ("…", ", "),
 41 |         (":", ","),
 42 |         (" - ", ", "),
 43 |         (";", ", "),
 44 |         ("—", "-"),
 45 |         ("–", "-"),
 46 |         (" ,", ","),
 47 |         ("“", "\""),
 48 |         ("”", "\""),
 49 |         ("‘", "'"),
 50 |         ("’", "'"),
 51 |     ]
 52 |     for old_char_sequence, new_char in punc_to_replace:
 53 |         text = text.replace(old_char_sequence, new_char)
 54 | 
 55 |     # Add full stop if no ending punc
 56 |     text = text.rstrip(" ")
 57 |     sentence_enders = {".", "!", "?", "-", ","}
 58 |     if not any(text.endswith(p) for p in sentence_enders):
 59 |         text += "."
 60 | 
 61 |     return text
 62 | 
 63 | 
 64 | @dataclass
 65 | class Conditionals:
 66 |     """
 67 |     Conditionals for T3 and S3Gen
 68 |     - T3 conditionals:
 69 |         - speaker_emb
 70 |         - clap_emb
 71 |         - cond_prompt_speech_tokens
 72 |         - cond_prompt_speech_emb
 73 |         - emotion_adv
 74 |     - S3Gen conditionals:
 75 |         - prompt_token
 76 |         - prompt_token_len
 77 |         - prompt_feat
 78 |         - prompt_feat_len
 79 |         - embedding
 80 |     """
 81 |     t3: T3Cond
 82 |     gen: dict
 83 | 
 84 |     def to(self, device):
 85 |         self.t3 = self.t3.to(device=device)
 86 |         for k, v in self.gen.items():
 87 |             if torch.is_tensor(v):
 88 |                 self.gen[k] = v.to(device=device)
 89 |         return self
 90 | 
 91 |     def save(self, fpath: Path):
 92 |         arg_dict = dict(
 93 |             t3=self.t3.__dict__,
 94 |             gen=self.gen
 95 |         )
 96 |         torch.save(arg_dict, fpath)
 97 | 
 98 |     @classmethod
 99 |     def load(cls, fpath, map_location="cpu"):
100 |         if isinstance(map_location, str):
101 |             map_location = torch.device(map_location)
102 |         kwargs = torch.load(fpath, map_location=map_location, weights_only=True)
103 |         return cls(T3Cond(**kwargs['t3']), kwargs['gen'])
104 | 
105 | 
106 | class ChatterboxTTS:
107 |     ENC_COND_LEN = 6 * S3_SR
108 |     DEC_COND_LEN = 10 * S3GEN_SR
109 | 
110 |     def __init__(
111 |         self,
112 |         t3: T3,
113 |         s3gen: S3Gen,
114 |         ve: VoiceEncoder,
115 |         tokenizer: EnTokenizer,
116 |         device: str,
117 |         conds: Conditionals = None,
118 |     ):
119 |         self.sr = S3GEN_SR  # sample rate of synthesized audio
120 |         self.t3 = t3
121 |         self.s3gen = s3gen
122 |         self.ve = ve
123 |         self.tokenizer = tokenizer
124 |         self.device = device
125 |         self.conds = conds
126 |         self.watermarker = perth.PerthImplicitWatermarker()
127 | 
128 |     @classmethod
129 |     def from_local(cls, ckpt_dir, device) -> 'ChatterboxTTS':
130 |         ckpt_dir = Path(ckpt_dir)
131 | 
132 |         # Always load to CPU first for non-CUDA devices to handle CUDA-saved models
133 |         if device in ["cpu", "mps"]:
134 |             map_location = torch.device('cpu')
135 |         else:
136 |             map_location = None
137 | 
138 |         ve = VoiceEncoder()
139 |         ve.load_state_dict(
140 |             load_file(ckpt_dir / "ve.safetensors")
141 |         )
142 |         ve.to(device).eval()
143 | 
144 |         t3 = T3()
145 |         t3_state = load_file(ckpt_dir / "t3_cfg.safetensors")
146 |         if "model" in t3_state.keys():
147 |             t3_state = t3_state["model"][0]
148 |         t3.load_state_dict(t3_state)
149 |         t3.to(device).eval()
150 | 
151 |         s3gen = S3Gen()
152 |         s3gen.load_state_dict(
153 |             load_file(ckpt_dir / "s3gen.safetensors"), strict=False
154 |         )
155 |         s3gen.to(device).eval()
156 | 
157 |         tokenizer = EnTokenizer(
158 |             str(ckpt_dir / "tokenizer.json")
159 |         )
160 | 
161 |         conds = None
162 |         if (builtin_voice := ckpt_dir / "conds.pt").exists():
163 |             conds = Conditionals.load(builtin_voice, map_location=map_location).to(device)
164 | 
165 |         return cls(t3, s3gen, ve, tokenizer, device, conds=conds)
166 | 
167 |     @classmethod
168 |     def from_pretrained(cls, device) -> 'ChatterboxTTS':
169 |         # Check if MPS is available on macOS
170 |         if device == "mps" and not torch.backends.mps.is_available():
171 |             if not torch.backends.mps.is_built():
172 |                 print("MPS not available because the current PyTorch install was not built with MPS enabled.")
173 |             else:
174 |                 print("MPS not available because the current MacOS version is not 12.3+ and/or you do not have an MPS-enabled device on this machine.")
175 |             device = "cpu"
176 | 
177 |         for fpath in ["ve.safetensors", "t3_cfg.safetensors", "s3gen.safetensors", "tokenizer.json", "conds.pt"]:
178 |             local_path = hf_hub_download(repo_id=REPO_ID, filename=fpath)
179 | 
180 |         return cls.from_local(Path(local_path).parent, device)
181 | 
182 |     def prepare_conditionals(self, wav_fpath, exaggeration=0.5):
183 |         ## Load reference wav
184 |         s3gen_ref_wav, _sr = librosa.load(wav_fpath, sr=S3GEN_SR)
185 | 
186 |         ref_16k_wav = librosa.resample(s3gen_ref_wav, orig_sr=S3GEN_SR, target_sr=S3_SR)
187 | 
188 |         s3gen_ref_wav = s3gen_ref_wav[:self.DEC_COND_LEN]
189 |         s3gen_ref_dict = self.s3gen.embed_ref(s3gen_ref_wav, S3GEN_SR, device=self.device)
190 | 
191 |         # Speech cond prompt tokens
192 |         if plen := self.t3.hp.speech_cond_prompt_len:
193 |             s3_tokzr = self.s3gen.tokenizer
194 |             t3_cond_prompt_tokens, _ = s3_tokzr.forward([ref_16k_wav[:self.ENC_COND_LEN]], max_len=plen)
195 |             t3_cond_prompt_tokens = torch.atleast_2d(t3_cond_prompt_tokens).to(self.device)
196 | 
197 |         # Voice-encoder speaker embedding
198 |         ve_embed = torch.from_numpy(self.ve.embeds_from_wavs([ref_16k_wav], sample_rate=S3_SR))
199 |         ve_embed = ve_embed.mean(axis=0, keepdim=True).to(self.device)
200 | 
201 |         t3_cond = T3Cond(
202 |             speaker_emb=ve_embed,
203 |             cond_prompt_speech_tokens=t3_cond_prompt_tokens,
204 |             emotion_adv=exaggeration * torch.ones(1, 1, 1),
205 |         ).to(device=self.device)
206 |         self.conds = Conditionals(t3_cond, s3gen_ref_dict)
207 | 
208 |     def generate(
209 |         self,
210 |         text,
211 |         repetition_penalty=1.2,
212 |         min_p=0.05,
213 |         top_p=1.0,
214 |         audio_prompt_path=None,
215 |         exaggeration=0.5,
216 |         cfg_weight=0.5,
217 |         temperature=0.8,
218 |     ):
219 |         if audio_prompt_path:
220 |             self.prepare_conditionals(audio_prompt_path, exaggeration=exaggeration)
221 |         else:
222 |             assert self.conds is not None, "Please `prepare_conditionals` first or specify `audio_prompt_path`"
223 | 
224 |         # Update exaggeration if needed
225 |         if exaggeration != self.conds.t3.emotion_adv[0, 0, 0]:
226 |             _cond: T3Cond = self.conds.t3
227 |             self.conds.t3 = T3Cond(
228 |                 speaker_emb=_cond.speaker_emb,
229 |                 cond_prompt_speech_tokens=_cond.cond_prompt_speech_tokens,
230 |                 emotion_adv=exaggeration * torch.ones(1, 1, 1),
231 |             ).to(device=self.device)
232 | 
233 |         # Norm and tokenize text
234 |         text = punc_norm(text)
235 |         text_tokens = self.tokenizer.text_to_tokens(text).to(self.device)
236 | 
237 |         if cfg_weight > 0.0:
238 |             text_tokens = torch.cat([text_tokens, text_tokens], dim=0)  # Need two seqs for CFG
239 | 
240 |         sot = self.t3.hp.start_text_token
241 |         eot = self.t3.hp.stop_text_token
242 |         text_tokens = F.pad(text_tokens, (1, 0), value=sot)
243 |         text_tokens = F.pad(text_tokens, (0, 1), value=eot)
244 | 
245 |         with torch.inference_mode():
246 |             speech_tokens = self.t3.inference(
247 |                 t3_cond=self.conds.t3,
248 |                 text_tokens=text_tokens,
249 |                 max_new_tokens=1000,  # TODO: use the value in config
250 |                 temperature=temperature,
251 |                 cfg_weight=cfg_weight,
252 |                 repetition_penalty=repetition_penalty,
253 |                 min_p=min_p,
254 |                 top_p=top_p,
255 |             )
256 |             # Extract only the conditional batch.
257 |             speech_tokens = speech_tokens[0]
258 | 
259 |             # TODO: output becomes 1D
260 |             speech_tokens = drop_invalid_tokens(speech_tokens)
261 |             
262 |             speech_tokens = speech_tokens[speech_tokens < 6561]
263 | 
264 |             speech_tokens = speech_tokens.to(self.device)
265 | 
266 |             wav, _ = self.s3gen.inference(
267 |                 speech_tokens=speech_tokens,
268 |                 ref_dict=self.conds.gen,
269 |             )
270 |             wav = wav.squeeze(0).detach().cpu().numpy()
271 |             watermarked_wav = self.watermarker.apply_watermark(wav, sample_rate=self.sr)
272 |         return torch.from_numpy(watermarked_wav).unsqueeze(0)


--------------------------------------------------------------------------------
/src/chatterbox/vc.py:
--------------------------------------------------------------------------------
  1 | from pathlib import Path
  2 | 
  3 | import librosa
  4 | import torch
  5 | import perth
  6 | from huggingface_hub import hf_hub_download
  7 | from safetensors.torch import load_file
  8 | 
  9 | from .models.s3tokenizer import S3_SR
 10 | from .models.s3gen import S3GEN_SR, S3Gen
 11 | 
 12 | 
 13 | REPO_ID = "ResembleAI/chatterbox"
 14 | 
 15 | 
 16 | class ChatterboxVC:
 17 |     ENC_COND_LEN = 6 * S3_SR
 18 |     DEC_COND_LEN = 10 * S3GEN_SR
 19 | 
 20 |     def __init__(
 21 |         self,
 22 |         s3gen: S3Gen,
 23 |         device: str,
 24 |         ref_dict: dict=None,
 25 |     ):
 26 |         self.sr = S3GEN_SR
 27 |         self.s3gen = s3gen
 28 |         self.device = device
 29 |         self.watermarker = perth.PerthImplicitWatermarker()
 30 |         if ref_dict is None:
 31 |             self.ref_dict = None
 32 |         else:
 33 |             self.ref_dict = {
 34 |                 k: v.to(device) if torch.is_tensor(v) else v
 35 |                 for k, v in ref_dict.items()
 36 |             }
 37 | 
 38 |     @classmethod
 39 |     def from_local(cls, ckpt_dir, device) -> 'ChatterboxVC':
 40 |         ckpt_dir = Path(ckpt_dir)
 41 |         
 42 |         # Always load to CPU first for non-CUDA devices to handle CUDA-saved models
 43 |         if device in ["cpu", "mps"]:
 44 |             map_location = torch.device('cpu')
 45 |         else:
 46 |             map_location = None
 47 |             
 48 |         ref_dict = None
 49 |         if (builtin_voice := ckpt_dir / "conds.pt").exists():
 50 |             states = torch.load(builtin_voice, map_location=map_location)
 51 |             ref_dict = states['gen']
 52 | 
 53 |         s3gen = S3Gen()
 54 |         s3gen.load_state_dict(
 55 |             load_file(ckpt_dir / "s3gen.safetensors"), strict=False
 56 |         )
 57 |         s3gen.to(device).eval()
 58 | 
 59 |         return cls(s3gen, device, ref_dict=ref_dict)
 60 | 
 61 |     @classmethod
 62 |     def from_pretrained(cls, device) -> 'ChatterboxVC':
 63 |         # Check if MPS is available on macOS
 64 |         if device == "mps" and not torch.backends.mps.is_available():
 65 |             if not torch.backends.mps.is_built():
 66 |                 print("MPS not available because the current PyTorch install was not built with MPS enabled.")
 67 |             else:
 68 |                 print("MPS not available because the current MacOS version is not 12.3+ and/or you do not have an MPS-enabled device on this machine.")
 69 |             device = "cpu"
 70 |             
 71 |         for fpath in ["s3gen.safetensors", "conds.pt"]:
 72 |             local_path = hf_hub_download(repo_id=REPO_ID, filename=fpath)
 73 | 
 74 |         return cls.from_local(Path(local_path).parent, device)
 75 | 
 76 |     def set_target_voice(self, wav_fpath):
 77 |         ## Load reference wav
 78 |         s3gen_ref_wav, _sr = librosa.load(wav_fpath, sr=S3GEN_SR)
 79 | 
 80 |         s3gen_ref_wav = s3gen_ref_wav[:self.DEC_COND_LEN]
 81 |         self.ref_dict = self.s3gen.embed_ref(s3gen_ref_wav, S3GEN_SR, device=self.device)
 82 | 
 83 |     def generate(
 84 |         self,
 85 |         audio,
 86 |         target_voice_path=None,
 87 |     ):
 88 |         if target_voice_path:
 89 |             self.set_target_voice(target_voice_path)
 90 |         else:
 91 |             assert self.ref_dict is not None, "Please `prepare_conditionals` first or specify `target_voice_path`"
 92 | 
 93 |         with torch.inference_mode():
 94 |             audio_16, _ = librosa.load(audio, sr=S3_SR)
 95 |             audio_16 = torch.from_numpy(audio_16).float().to(self.device)[None, ]
 96 | 
 97 |             s3_tokens, _ = self.s3gen.tokenizer(audio_16)
 98 |             wav, _ = self.s3gen.inference(
 99 |                 speech_tokens=s3_tokens,
100 |                 ref_dict=self.ref_dict,
101 |             )
102 |             wav = wav.squeeze(0).detach().cpu().numpy()
103 |             watermarked_wav = self.watermarker.apply_watermark(wav, sample_rate=self.sr)
104 |         return torch.from_numpy(watermarked_wav).unsqueeze(0)


--------------------------------------------------------------------------------├── .gitignore
├── LICENSE
├── README.md
├── example_for_mac.py
├── example_tts.py
├── example_vc.py
├── gradio_tts_app.py
├── gradio_vc_app.py
├── pyproject.toml
└── src
    └── chatterbox
        ├── __init__.py
        ├── models
            ├── __init__.py
            ├── s3gen
            │   ├── __init__.py
            │   ├── configs.py
            │   ├── const.py
            │   ├── decoder.py
            │   ├── f0_predictor.py
            │   ├── flow.py
            │   ├── flow_matching.py
            │   ├── hifigan.py
            │   ├── matcha
            │   │   ├── decoder.py
            │   │   ├── flow_matching.py
            │   │   ├── text_encoder.py
            │   │   └── transformer.py
            │   ├── s3gen.py
            │   ├── transformer
            │   │   ├── __init__.py
            │   │   ├── activation.py
            │   │   ├── attention.py
            │   │   ├── convolution.py
            │   │   ├── embedding.py
            │   │   ├── encoder_layer.py
            │   │   ├── positionwise_feed_forward.py
            │   │   ├── subsampling.py
            │   │   └── upsample_encoder.py
            │   ├── utils
            │   │   ├── class_utils.py
            │   │   ├── mask.py
            │   │   └── mel.py
            │   └── xvector.py
            ├── s3tokenizer
            │   ├── __init__.py
            │   └── s3tokenizer.py
            ├── t3
            │   ├── __init__.py
            │   ├── inference
            │   │   ├── alignment_stream_analyzer.py
            │   │   └── t3_hf_backend.py
            │   ├── llama_configs.py
            │   ├── modules
            │   │   ├── cond_enc.py
            │   │   ├── learned_pos_emb.py
            │   │   ├── perceiver.py
            │   │   └── t3_config.py
            │   └── t3.py
            ├── tokenizers
            │   ├── __init__.py
            │   └── tokenizer.py
            ├── utils.py
            └── voice_encoder
            │   ├── __init__.py
            │   ├── config.py
            │   ├── melspec.py
            │   └── voice_encoder.py
        ├── tts.py
        └── vc.py


/.gitignore:
--------------------------------------------------------------------------------
 1 | .vscode
 2 | 
 3 | # Pylance
 4 | pyrightconfig.json
 5 | 
 6 | # Byte-compiled / optimized / DLL files
 7 | __pycache__/
 8 | *.py[cod]
 9 | *$py.class
10 | 
11 | # C extensions
12 | *.so
13 | 
14 | # Distribution / packaging
15 | .Python
16 | build/
17 | develop-eggs/
18 | dist/
19 | downloads/
20 | eggs/
21 | .eggs/
22 | lib/
23 | lib64/
24 | parts/
25 | sdist/
26 | var/
27 | wheels/
28 | *.egg-info/
29 | .installed.cfg
30 | *.egg
31 | MANIFEST
32 | 
33 | # PyInstaller
34 | #  Usually these files are written by a python script from a template
35 | #  before PyInstaller builds the exe, so as to inject date/other infos into it.
36 | *.manifest
37 | *.spec
38 | 
39 | # Installer logs
40 | pip-log.txt
41 | pip-delete-this-directory.txt
42 | 
43 | syn_out/
44 | checkpoints/
45 | .gradio
46 | 
47 | # Ignore generated sample .wav files
48 | **/*.wav
49 | 


--------------------------------------------------------------------------------
/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2025 Resemble AI
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
  1 | 
  2 | <img width="1200" alt="cb-big2" src="https://github.com/user-attachments/assets/bd8c5f03-e91d-4ee5-b680-57355da204d1" />
  3 | 
  4 | # Chatterbox TTS
  5 | 
  6 | [![Alt Text](https://img.shields.io/badge/listen-demo_samples-blue)](https://resemble-ai.github.io/chatterbox_demopage/)
  7 | [![Alt Text](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/ResembleAI/Chatterbox)
  8 | [![Alt Text](https://static-public.podonos.com/badges/insight-on-pdns-sm-dark.svg)](https://podonos.com/resembleai/chatterbox)
  9 | [![Discord](https://img.shields.io/discord/1377773249798344776?label=join%20discord&logo=discord&style=flat)](https://discord.gg/rJq9cRJBJ6)
 10 | 
 11 | _Made with ♥️ by <a href="https://resemble.ai" target="_blank"><img width="100" alt="resemble-logo-horizontal" src="https://github.com/user-attachments/assets/35cf756b-3506-4943-9c72-c05ddfa4e525" /></a>
 12 | 
 13 | We're excited to introduce Chatterbox, [Resemble AI's](https://resemble.ai) first production-grade open source TTS model. Licensed under MIT, Chatterbox has been benchmarked against leading closed-source systems like ElevenLabs, and is consistently preferred in side-by-side evaluations.
 14 | 
 15 | Whether you're working on memes, videos, games, or AI agents, Chatterbox brings your content to life. It's also the first open source TTS model to support **emotion exaggeration control**, a powerful feature that makes your voices stand out. Try it now on our [Hugging Face Gradio app.](https://huggingface.co/spaces/ResembleAI/Chatterbox)
 16 | 
 17 | If you like the model but need to scale or tune it for higher accuracy, check out our competitively priced TTS service (<a href="https://resemble.ai">link</a>). It delivers reliable performance with ultra-low latency of sub 200ms—ideal for production use in agents, applications, or interactive media.
 18 | 
 19 | # Key Details
 20 | - SoTA zeroshot TTS
 21 | - 0.5B Llama backbone
 22 | - Unique exaggeration/intensity control
 23 | - Ultra-stable with alignment-informed inference
 24 | - Trained on 0.5M hours of cleaned data
 25 | - Watermarked outputs
 26 | - Easy voice conversion script
 27 | - [Outperforms ElevenLabs](https://podonos.com/resembleai/chatterbox)
 28 | 
 29 | # Tips
 30 | - **General Use (TTS and Voice Agents):**
 31 |   - The default settings (`exaggeration=0.5`, `cfg_weight=0.5`) work well for most prompts.
 32 |   - If the reference speaker has a fast speaking style, lowering `cfg_weight` to around `0.3` can improve pacing.
 33 | 
 34 | - **Expressive or Dramatic Speech:**
 35 |   - Try lower `cfg_weight` values (e.g. `~0.3`) and increase `exaggeration` to around `0.7` or higher.
 36 |   - Higher `exaggeration` tends to speed up speech; reducing `cfg_weight` helps compensate with slower, more deliberate pacing.
 37 | 
 38 | 
 39 | # Installation
 40 | ```shell
 41 | pip install chatterbox-tts
 42 | ```
 43 | 
 44 | Alternatively, you can install from source:
 45 | ```shell
 46 | # conda create -yn chatterbox python=3.11
 47 | # conda activate chatterbox
 48 | 
 49 | git clone https://github.com/resemble-ai/chatterbox.git
 50 | cd chatterbox
 51 | pip install -e .
 52 | ```
 53 | We developed and tested Chatterbox on Python 3.11 on Debain 11 OS; the versions of the dependencies are pinned in `pyproject.toml` to ensure consistency. You can modify the code or dependencies in this installation mode.
 54 | 
 55 | 
 56 | # Usage
 57 | ```python
 58 | import torchaudio as ta
 59 | from chatterbox.tts import ChatterboxTTS
 60 | 
 61 | model = ChatterboxTTS.from_pretrained(device="cuda")
 62 | 
 63 | text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
 64 | wav = model.generate(text)
 65 | ta.save("test-1.wav", wav, model.sr)
 66 | 
 67 | # If you want to synthesize with a different voice, specify the audio prompt
 68 | AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
 69 | wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
 70 | ta.save("test-2.wav", wav, model.sr)
 71 | ```
 72 | See `example_tts.py` and `example_vc.py` for more examples.
 73 | 
 74 | # Supported Lanugage
 75 | Currenlty only English.
 76 | 
 77 | # Acknowledgements
 78 | - [Cosyvoice](https://github.com/FunAudioLLM/CosyVoice)
 79 | - [Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)
 80 | - [HiFT-GAN](https://github.com/yl4579/HiFTNet)
 81 | - [Llama 3](https://github.com/meta-llama/llama3)
 82 | - [S3Tokenizer](https://github.com/xingchensong/S3Tokenizer)
 83 | 
 84 | # Built-in PerTh Watermarking for Responsible AI
 85 | 
 86 | Every audio file generated by Chatterbox includes [Resemble AI's Perth (Perceptual Threshold) Watermarker](https://github.com/resemble-ai/perth) - imperceptible neural watermarks that survive MP3 compression, audio editing, and common manipulations while maintaining nearly 100% detection accuracy.
 87 | 
 88 | 
 89 | ## Watermark extraction
 90 | 
 91 | You can look for the watermark using the following script.
 92 | 
 93 | ```python
 94 | import perth
 95 | import librosa
 96 | 
 97 | AUDIO_PATH = "YOUR_FILE.wav"
 98 | 
 99 | # Load the watermarked audio
100 | watermarked_audio, sr = librosa.load(AUDIO_PATH, sr=None)
101 | 
102 | # Initialize watermarker (same as used for embedding)
103 | watermarker = perth.PerthImplicitWatermarker()
104 | 
105 | # Extract watermark
106 | watermark = watermarker.get_watermark(watermarked_audio, sample_rate=sr)
107 | print(f"Extracted watermark: {watermark}")
108 | # Output: 0.0 (no watermark) or 1.0 (watermarked)
109 | ```
110 | 
111 | 
112 | # Official Discord
113 | 
114 | 👋 Join us on [Discord](https://discord.gg/rJq9cRJBJ6) and let's build something awesome together!
115 | 
116 | # Disclaimer
117 | Don't use this model to do bad things. Prompts are sourced from freely available data on the internet.
118 | 


--------------------------------------------------------------------------------
/example_for_mac.py:
--------------------------------------------------------------------------------
 1 | import torch
 2 | import torchaudio as ta
 3 | from chatterbox.tts import ChatterboxTTS
 4 | 
 5 | # Detect device (Mac with M1/M2/M3/M4)
 6 | device = "mps" if torch.backends.mps.is_available() else "cpu"
 7 | map_location = torch.device(device)
 8 | 
 9 | torch_load_original = torch.load
10 | def patched_torch_load(*args, **kwargs):
11 |     if 'map_location' not in kwargs:
12 |         kwargs['map_location'] = map_location
13 |     return torch_load_original(*args, **kwargs)
14 | 
15 | torch.load = patched_torch_load
16 | 
17 | model = ChatterboxTTS.from_pretrained(device=device)
18 | text = "Today is the day. I want to move like a titan at dawn, sweat like a god forging lightning. No more excuses. From now on, my mornings will be temples of discipline. I am going to work out like the gods… every damn day."
19 | 
20 | # If you want to synthesize with a different voice, specify the audio prompt
21 | AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
22 | wav = model.generate(
23 |     text, 
24 |     audio_prompt_path=AUDIO_PROMPT_PATH,
25 |     exaggeration=2.0,
26 |     cfg_weight=0.5
27 |     )
28 | ta.save("test-2.wav", wav, model.sr)
29 | 


--------------------------------------------------------------------------------
/example_tts.py:
--------------------------------------------------------------------------------
 1 | import torchaudio as ta
 2 | import torch
 3 | from chatterbox.tts import ChatterboxTTS
 4 | 
 5 | # Automatically detect the best available device
 6 | if torch.cuda.is_available():
 7 |     device = "cuda"
 8 | elif torch.backends.mps.is_available():
 9 |     device = "mps"
10 | else:
11 |     device = "cpu"
12 | 
13 | print(f"Using device: {device}")
14 | 
15 | model = ChatterboxTTS.from_pretrained(device=device)
16 | 
17 | text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
18 | wav = model.generate(text)
19 | ta.save("test-1.wav", wav, model.sr)
20 | 
21 | # If you want to synthesize with a different voice, specify the audio prompt
22 | AUDIO_PROMPT_PATH = "YOUR_FILE.wav"
23 | wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
24 | ta.save("test-2.wav", wav, model.sr)
25 | 


--------------------------------------------------------------------------------
/example_vc.py:
--------------------------------------------------------------------------------
 1 | import torch
 2 | import torchaudio as ta
 3 | 
 4 | from chatterbox.vc import ChatterboxVC
 5 | 
 6 | # Automatically detect the best available device
 7 | if torch.cuda.is_available():
 8 |     device = "cuda"
 9 | elif torch.backends.mps.is_available():
10 |     device = "mps"
11 | else:
12 |     device = "cpu"
13 | 
14 | print(f"Using device: {device}")
15 | 
16 | AUDIO_PATH = "YOUR_FILE.wav"
17 | TARGET_VOICE_PATH = "YOUR_FILE.wav"
18 | 
19 | model = ChatterboxVC.from_pretrained(device)
20 | wav = model.generate(
21 |     audio=AUDIO_PATH,
22 |     target_voice_path=TARGET_VOICE_PATH,
23 | )
24 | ta.save("testvc.wav", wav, model.sr)
25 | 


--------------------------------------------------------------------------------
/gradio_tts_app.py:
--------------------------------------------------------------------------------
 1 | import random
 2 | import numpy as np
 3 | import torch
 4 | import gradio as gr
 5 | from chatterbox.tts import ChatterboxTTS
 6 | 
 7 | 
 8 | DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
 9 | 
10 | 
11 | def set_seed(seed: int):
12 |     torch.manual_seed(seed)
13 |     torch.cuda.manual_seed(seed)
14 |     torch.cuda.manual_seed_all(seed)
15 |     random.seed(seed)
16 |     np.random.seed(seed)
17 | 
18 | 
19 | def load_model():
20 |     model = ChatterboxTTS.from_pretrained(DEVICE)
21 |     return model
22 | 
23 | 
24 | def generate(model, text, audio_prompt_path, exaggeration, temperature, seed_num, cfgw, min_p, top_p, repetition_penalty):
25 |     if model is None:
26 |         model = ChatterboxTTS.from_pretrained(DEVICE)
27 | 
28 |     if seed_num != 0:
29 |         set_seed(int(seed_num))
30 | 
31 |     wav = model.generate(
32 |         text,
33 |         audio_prompt_path=audio_prompt_path,
34 |         exaggeration=exaggeration,
35 |         temperature=temperature,
36 |         cfg_weight=cfgw,
37 |         min_p=min_p,
38 |         top_p=top_p,
39 |         repetition_penalty=repetition_penalty,
40 |     )
41 |     return (model.sr, wav.squeeze(0).numpy())
42 | 
43 | 
44 | with gr.Blocks() as demo:
45 |     model_state = gr.State(None)  # Loaded once per session/user
46 | 
47 |     with gr.Row():
48 |         with gr.Column():
49 |             text = gr.Textbox(
50 |                 value="Now let's make my mum's favourite. So three mars bars into the pan. Then we add the tuna and just stir for a bit, just let the chocolate and fish infuse. A sprinkle of olive oil and some tomato ketchup. Now smell that. Oh boy this is going to be incredible.",
51 |                 label="Text to synthesize (max chars 300)",
52 |                 max_lines=5
53 |             )
54 |             ref_wav = gr.Audio(sources=["upload", "microphone"], type="filepath", label="Reference Audio File", value=None)
55 |             exaggeration = gr.Slider(0.25, 2, step=.05, label="Exaggeration (Neutral = 0.5, extreme values can be unstable)", value=.5)
56 |             cfg_weight = gr.Slider(0.0, 1, step=.05, label="CFG/Pace", value=0.5)
57 | 
58 |             with gr.Accordion("More options", open=False):
59 |                 seed_num = gr.Number(value=0, label="Random seed (0 for random)")
60 |                 temp = gr.Slider(0.05, 5, step=.05, label="temperature", value=.8)
61 |                 min_p = gr.Slider(0.00, 1.00, step=0.01, label="min_p || Newer Sampler. Recommend 0.02 > 0.1. Handles Higher Temperatures better. 0.00 Disables", value=0.05)
62 |                 top_p = gr.Slider(0.00, 1.00, step=0.01, label="top_p || Original Sampler. 1.0 Disables(recommended). Original 0.8", value=1.00)
63 |                 repetition_penalty = gr.Slider(1.00, 2.00, step=0.1, label="repetition_penalty", value=1.2)
64 | 
65 |             run_btn = gr.Button("Generate", variant="primary")
66 | 
67 |         with gr.Column():
68 |             audio_output = gr.Audio(label="Output Audio")
69 | 
70 |     demo.load(fn=load_model, inputs=[], outputs=model_state)
71 | 
72 |     run_btn.click(
73 |         fn=generate,
74 |         inputs=[
75 |             model_state,
76 |             text,
77 |             ref_wav,
78 |             exaggeration,
79 |             temp,
80 |             seed_num,
81 |             cfg_weight,
82 |             min_p,
83 |             top_p,
84 |             repetition_penalty,
85 |         ],
86 |         outputs=audio_output,
87 |     )
88 | 
89 | if __name__ == "__main__":
90 |     demo.queue(
91 |         max_size=50,
92 |         default_concurrency_limit=1,
93 |     ).launch(share=True)
94 | 


--------------------------------------------------------------------------------
/gradio_vc_app.py:
--------------------------------------------------------------------------------
 1 | import torch
 2 | import gradio as gr
 3 | from chatterbox.vc import ChatterboxVC
 4 | 
 5 | 
 6 | DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
 7 | 
 8 | 
 9 | model = ChatterboxVC.from_pretrained(DEVICE)
10 | def generate(audio, target_voice_path):
11 |     wav = model.generate(
12 |         audio, target_voice_path=target_voice_path,
13 |     )
14 |     return model.sr, wav.squeeze(0).numpy()
15 | 
16 | 
17 | demo = gr.Interface(
18 |     generate,
19 |     [
20 |         gr.Audio(sources=["upload", "microphone"], type="filepath", label="Input audio file"),
21 |         gr.Audio(sources=["upload", "microphone"], type="filepath", label="Target voice audio file (if none, the default voice is used)", value=None),
22 |     ],
23 |     "audio",
24 | )
25 | 
26 | if __name__ == "__main__":
27 |     demo.launch()
28 | 


--------------------------------------------------------------------------------
/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [project]
 2 | name = "chatterbox-tts"
 3 | version = "0.1.2"
 4 | description = "Chatterbox: Open Source TTS and Voice Conversion by Resemble AI"
 5 | readme = "README.md"
 6 | requires-python = ">=3.9"
 7 | license = {file = "LICENSE"}
 8 | authors = [
 9 |     {name = "resemble-ai", email = "engineering@resemble.ai"}
10 | ]
11 | dependencies = [
12 |     "numpy>=1.26.0",
13 |     "librosa==0.11.0",
14 |     "s3tokenizer",
15 |     "torch==2.6.0",
16 |     "torchaudio==2.6.0",
17 |     "transformers==4.46.3",
18 |     "diffusers==0.29.0",
19 |     "resemble-perth==1.0.1",
20 |     "conformer==0.3.2",
21 |     "safetensors==0.5.3"
22 | ]
23 | 
24 | [project.urls]
25 | Homepage = "https://github.com/resemble-ai/chatterbox"
26 | Repository = "https://github.com/resemble-ai/chatterbox"
27 | 
28 | [build-system]
29 | requires = ["setuptools>=61.0"]
30 | build-backend = "setuptools.build_meta"
31 | 
32 | [tool.setuptools.packages.find]
33 | where = ["src"]
34 | 


--------------------------------------------------------------------------------
/src/chatterbox/__init__.py:
--------------------------------------------------------------------------------
 1 | try:
 2 |     from importlib.metadata import version
 3 | except ImportError:
 4 |     from importlib_metadata import version  # For Python <3.8
 5 | 
 6 | __version__ = version("chatterbox-tts")
 7 | 
 8 | 
 9 | from .tts import ChatterboxTTS
10 | from .vc import ChatterboxVC
11 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/resemble-ai/chatterbox/eb90621fa748f341a5b768aed0c0c12fc561894b/src/chatterbox/models/__init__.py


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/__init__.py:
--------------------------------------------------------------------------------
1 | from .s3gen import S3Token2Wav as S3Gen
2 | from .const import S3GEN_SR
3 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/configs.py:
--------------------------------------------------------------------------------
 1 | from ..utils import AttrDict
 2 | 
 3 | CFM_PARAMS = AttrDict({
 4 |     "sigma_min": 1e-06,
 5 |     "solver": "euler",
 6 |     "t_scheduler": "cosine",
 7 |     "training_cfg_rate": 0.2,
 8 |     "inference_cfg_rate": 0.7,
 9 |     "reg_loss_type": "l1"
10 | })
11 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/const.py:
--------------------------------------------------------------------------------
1 | S3GEN_SR = 24000
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/decoder.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Zhihao Du)
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | import torch
 15 | import torch.nn as nn
 16 | import torch.nn.functional as F
 17 | from einops import pack, rearrange, repeat
 18 | 
 19 | from .utils.mask import add_optional_chunk_mask
 20 | from .matcha.decoder import SinusoidalPosEmb, Block1D, ResnetBlock1D, Downsample1D, \
 21 |     TimestepEmbedding, Upsample1D
 22 | from .matcha.transformer import BasicTransformerBlock
 23 | 
 24 | 
 25 | def mask_to_bias(mask: torch.Tensor, dtype: torch.dtype) -> torch.Tensor:
 26 |     assert mask.dtype == torch.bool
 27 |     assert dtype in [torch.float32, torch.bfloat16, torch.float16]
 28 |     mask = mask.to(dtype)
 29 |     # attention mask bias
 30 |     # NOTE(Mddct): torch.finfo jit issues
 31 |     #     chunk_masks = (1.0 - chunk_masks) * torch.finfo(dtype).min
 32 |     mask = (1.0 - mask) * -1.0e+10
 33 |     return mask
 34 | 
 35 | 
 36 | 
 37 | class Transpose(torch.nn.Module):
 38 |     def __init__(self, dim0: int, dim1: int):
 39 |         super().__init__()
 40 |         self.dim0 = dim0
 41 |         self.dim1 = dim1
 42 | 
 43 |     def forward(self, x: torch.Tensor):
 44 |         x = torch.transpose(x, self.dim0, self.dim1)
 45 |         return x
 46 | 
 47 | 
 48 | class CausalBlock1D(Block1D):
 49 |     def __init__(self, dim: int, dim_out: int):
 50 |         super(CausalBlock1D, self).__init__(dim, dim_out)
 51 |         self.block = torch.nn.Sequential(
 52 |             CausalConv1d(dim, dim_out, 3),
 53 |             Transpose(1, 2),
 54 |             nn.LayerNorm(dim_out),
 55 |             Transpose(1, 2),
 56 |             nn.Mish(),
 57 |         )
 58 | 
 59 |     def forward(self, x: torch.Tensor, mask: torch.Tensor):
 60 |         output = self.block(x * mask)
 61 |         return output * mask
 62 | 
 63 | 
 64 | class CausalResnetBlock1D(ResnetBlock1D):
 65 |     def __init__(self, dim: int, dim_out: int, time_emb_dim: int, groups: int = 8):
 66 |         super(CausalResnetBlock1D, self).__init__(dim, dim_out, time_emb_dim, groups)
 67 |         self.block1 = CausalBlock1D(dim, dim_out)
 68 |         self.block2 = CausalBlock1D(dim_out, dim_out)
 69 | 
 70 | 
 71 | class CausalConv1d(torch.nn.Conv1d):
 72 |     def __init__(
 73 |         self,
 74 |         in_channels: int,
 75 |         out_channels: int,
 76 |         kernel_size: int,
 77 |         stride: int = 1,
 78 |         dilation: int = 1,
 79 |         groups: int = 1,
 80 |         bias: bool = True,
 81 |         padding_mode: str = 'zeros',
 82 |         device=None,
 83 |         dtype=None
 84 |     ) -> None:
 85 |         super(CausalConv1d, self).__init__(in_channels, out_channels,
 86 |                                            kernel_size, stride,
 87 |                                            padding=0, dilation=dilation,
 88 |                                            groups=groups, bias=bias,
 89 |                                            padding_mode=padding_mode,
 90 |                                            device=device, dtype=dtype)
 91 |         assert stride == 1
 92 |         self.causal_padding = (kernel_size - 1, 0)
 93 | 
 94 |     def forward(self, x: torch.Tensor):
 95 |         x = F.pad(x, self.causal_padding)
 96 |         x = super(CausalConv1d, self).forward(x)
 97 |         return x
 98 | 
 99 | 
100 | class ConditionalDecoder(nn.Module):
101 |     def __init__(
102 |         self,
103 |         in_channels=320,
104 |         out_channels=80,
105 |         causal=True,
106 |         channels=[256],
107 |         dropout=0.0,
108 |         attention_head_dim=64,
109 |         n_blocks=4,
110 |         num_mid_blocks=12,
111 |         num_heads=8,
112 |         act_fn="gelu",
113 |     ):
114 |         """
115 |         This decoder requires an input with the same shape of the target. So, if your text content
116 |         is shorter or longer than the outputs, please re-sampling it before feeding to the decoder.
117 |         """
118 |         super().__init__()
119 |         channels = tuple(channels)
120 |         self.in_channels = in_channels
121 |         self.out_channels = out_channels
122 |         self.causal = causal
123 |         self.time_embeddings = SinusoidalPosEmb(in_channels)
124 |         time_embed_dim = channels[0] * 4
125 |         self.time_mlp = TimestepEmbedding(
126 |             in_channels=in_channels,
127 |             time_embed_dim=time_embed_dim,
128 |             act_fn="silu",
129 |         )
130 |         self.down_blocks = nn.ModuleList([])
131 |         self.mid_blocks = nn.ModuleList([])
132 |         self.up_blocks = nn.ModuleList([])
133 | 
134 |         # NOTE jrm: `static_chunk_size` is missing?
135 |         self.static_chunk_size = 0
136 | 
137 |         output_channel = in_channels
138 |         for i in range(len(channels)):  # pylint: disable=consider-using-enumerate
139 |             input_channel = output_channel
140 |             output_channel = channels[i]
141 |             is_last = i == len(channels) - 1
142 |             resnet = CausalResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim) if self.causal else \
143 |                 ResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim)
144 |             transformer_blocks = nn.ModuleList(
145 |                 [
146 |                     BasicTransformerBlock(
147 |                         dim=output_channel,
148 |                         num_attention_heads=num_heads,
149 |                         attention_head_dim=attention_head_dim,
150 |                         dropout=dropout,
151 |                         activation_fn=act_fn,
152 |                     )
153 |                     for _ in range(n_blocks)
154 |                 ]
155 |             )
156 |             downsample = (
157 |                 Downsample1D(output_channel) if not is_last else
158 |                 CausalConv1d(output_channel, output_channel, 3) if self.causal else nn.Conv1d(output_channel, output_channel, 3, padding=1)
159 |             )
160 |             self.down_blocks.append(nn.ModuleList([resnet, transformer_blocks, downsample]))
161 | 
162 |         for _ in range(num_mid_blocks):
163 |             input_channel = channels[-1]
164 |             out_channels = channels[-1]
165 |             resnet = CausalResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim) if self.causal else \
166 |                 ResnetBlock1D(dim=input_channel, dim_out=output_channel, time_emb_dim=time_embed_dim)
167 | 
168 |             transformer_blocks = nn.ModuleList(
169 |                 [
170 |                     BasicTransformerBlock(
171 |                         dim=output_channel,
172 |                         num_attention_heads=num_heads,
173 |                         attention_head_dim=attention_head_dim,
174 |                         dropout=dropout,
175 |                         activation_fn=act_fn,
176 |                     )
177 |                     for _ in range(n_blocks)
178 |                 ]
179 |             )
180 | 
181 |             self.mid_blocks.append(nn.ModuleList([resnet, transformer_blocks]))
182 | 
183 |         channels = channels[::-1] + (channels[0],)
184 |         for i in range(len(channels) - 1):
185 |             input_channel = channels[i] * 2
186 |             output_channel = channels[i + 1]
187 |             is_last = i == len(channels) - 2
188 |             resnet = CausalResnetBlock1D(
189 |                 dim=input_channel,
190 |                 dim_out=output_channel,
191 |                 time_emb_dim=time_embed_dim,
192 |             ) if self.causal else ResnetBlock1D(
193 |                 dim=input_channel,
194 |                 dim_out=output_channel,
195 |                 time_emb_dim=time_embed_dim,
196 |             )
197 |             transformer_blocks = nn.ModuleList(
198 |                 [
199 |                     BasicTransformerBlock(
200 |                         dim=output_channel,
201 |                         num_attention_heads=num_heads,
202 |                         attention_head_dim=attention_head_dim,
203 |                         dropout=dropout,
204 |                         activation_fn=act_fn,
205 |                     )
206 |                     for _ in range(n_blocks)
207 |                 ]
208 |             )
209 |             upsample = (
210 |                 Upsample1D(output_channel, use_conv_transpose=True)
211 |                 if not is_last
212 |                 else CausalConv1d(output_channel, output_channel, 3) if self.causal else nn.Conv1d(output_channel, output_channel, 3, padding=1)
213 |             )
214 |             self.up_blocks.append(nn.ModuleList([resnet, transformer_blocks, upsample]))
215 |         self.final_block = CausalBlock1D(channels[-1], channels[-1]) if self.causal else Block1D(channels[-1], channels[-1])
216 |         self.final_proj = nn.Conv1d(channels[-1], self.out_channels, 1)
217 |         self.initialize_weights()
218 | 
219 |     def initialize_weights(self):
220 |         for m in self.modules():
221 |             if isinstance(m, nn.Conv1d):
222 |                 nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
223 |                 if m.bias is not None:
224 |                     nn.init.constant_(m.bias, 0)
225 |             elif isinstance(m, nn.GroupNorm):
226 |                 nn.init.constant_(m.weight, 1)
227 |                 nn.init.constant_(m.bias, 0)
228 |             elif isinstance(m, nn.Linear):
229 |                 nn.init.kaiming_normal_(m.weight, nonlinearity="relu")
230 |                 if m.bias is not None:
231 |                     nn.init.constant_(m.bias, 0)
232 | 
233 |     def forward(self, x, mask, mu, t, spks=None, cond=None):
234 |         """Forward pass of the UNet1DConditional model.
235 | 
236 |         Args:
237 |             x (torch.Tensor): shape (batch_size, in_channels, time)
238 |             mask (_type_): shape (batch_size, 1, time)
239 |             t (_type_): shape (batch_size)
240 |             spks (_type_, optional): shape: (batch_size, condition_channels). Defaults to None.
241 |             cond (_type_, optional): placeholder for future use. Defaults to None.
242 | 
243 |         Raises:
244 |             ValueError: _description_
245 |             ValueError: _description_
246 | 
247 |         Returns:
248 |             _type_: _description_
249 |         """
250 | 
251 |         t = self.time_embeddings(t).to(t.dtype)
252 |         t = self.time_mlp(t)
253 | 
254 |         x = pack([x, mu], "b * t")[0]
255 | 
256 |         if spks is not None:
257 |             spks = repeat(spks, "b c -> b c t", t=x.shape[-1])
258 |             x = pack([x, spks], "b * t")[0]
259 |         if cond is not None:
260 |             x = pack([x, cond], "b * t")[0]
261 | 
262 |         hiddens = []
263 |         masks = [mask]
264 |         for resnet, transformer_blocks, downsample in self.down_blocks:
265 |             mask_down = masks[-1]
266 |             x = resnet(x, mask_down, t)
267 |             x = rearrange(x, "b c t -> b t c").contiguous()
268 |             # attn_mask = torch.matmul(mask_down.transpose(1, 2).contiguous(), mask_down)
269 |             attn_mask = add_optional_chunk_mask(x, mask_down.bool(), False, False, 0, self.static_chunk_size, -1)
270 |             attn_mask = mask_to_bias(attn_mask == 1, x.dtype)
271 |             for transformer_block in transformer_blocks:
272 |                 x = transformer_block(
273 |                     hidden_states=x,
274 |                     attention_mask=attn_mask,
275 |                     timestep=t,
276 |                 )
277 |             x = rearrange(x, "b t c -> b c t").contiguous()
278 |             hiddens.append(x)  # Save hidden states for skip connections
279 |             x = downsample(x * mask_down)
280 |             masks.append(mask_down[:, :, ::2])
281 |         masks = masks[:-1]
282 |         mask_mid = masks[-1]
283 | 
284 |         for resnet, transformer_blocks in self.mid_blocks:
285 |             x = resnet(x, mask_mid, t)
286 |             x = rearrange(x, "b c t -> b t c").contiguous()
287 |             # attn_mask = torch.matmul(mask_mid.transpose(1, 2).contiguous(), mask_mid)
288 |             attn_mask = add_optional_chunk_mask(x, mask_mid.bool(), False, False, 0, self.static_chunk_size, -1)
289 |             attn_mask = mask_to_bias(attn_mask == 1, x.dtype)
290 |             for transformer_block in transformer_blocks:
291 |                 x = transformer_block(
292 |                     hidden_states=x,
293 |                     attention_mask=attn_mask,
294 |                     timestep=t,
295 |                 )
296 |             x = rearrange(x, "b t c -> b c t").contiguous()
297 | 
298 |         for resnet, transformer_blocks, upsample in self.up_blocks:
299 |             mask_up = masks.pop()
300 |             skip = hiddens.pop()
301 |             x = pack([x[:, :, :skip.shape[-1]], skip], "b * t")[0]
302 |             x = resnet(x, mask_up, t)
303 |             x = rearrange(x, "b c t -> b t c").contiguous()
304 |             # attn_mask = torch.matmul(mask_up.transpose(1, 2).contiguous(), mask_up)
305 |             attn_mask = add_optional_chunk_mask(x, mask_up.bool(), False, False, 0, self.static_chunk_size, -1)
306 |             attn_mask = mask_to_bias(attn_mask == 1, x.dtype)
307 |             for transformer_block in transformer_blocks:
308 |                 x = transformer_block(
309 |                     hidden_states=x,
310 |                     attention_mask=attn_mask,
311 |                     timestep=t,
312 |                 )
313 |             x = rearrange(x, "b t c -> b c t").contiguous()
314 |             x = upsample(x * mask_up)
315 |         x = self.final_block(x, mask_up)
316 |         output = self.final_proj(x * mask_up)
317 |         return output * mask
318 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/f0_predictor.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Kai Hu)
 2 | #
 3 | # Licensed under the Apache License, Version 2.0 (the "License");
 4 | # you may not use this file except in compliance with the License.
 5 | # You may obtain a copy of the License at
 6 | #
 7 | #     http://www.apache.org/licenses/LICENSE-2.0
 8 | #
 9 | # Unless required by applicable law or agreed to in writing, software
10 | # distributed under the License is distributed on an "AS IS" BASIS,
11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12 | # See the License for the specific language governing permissions and
13 | # limitations under the License.
14 | import torch
15 | import torch.nn as nn
16 | from torch.nn.utils.parametrizations import weight_norm
17 | 
18 | 
19 | class ConvRNNF0Predictor(nn.Module):
20 |     def __init__(self,
21 |                  num_class: int = 1,
22 |                  in_channels: int = 80,
23 |                  cond_channels: int = 512
24 |                  ):
25 |         super().__init__()
26 | 
27 |         self.num_class = num_class
28 |         self.condnet = nn.Sequential(
29 |             weight_norm(
30 |                 nn.Conv1d(in_channels, cond_channels, kernel_size=3, padding=1)
31 |             ),
32 |             nn.ELU(),
33 |             weight_norm(
34 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
35 |             ),
36 |             nn.ELU(),
37 |             weight_norm(
38 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
39 |             ),
40 |             nn.ELU(),
41 |             weight_norm(
42 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
43 |             ),
44 |             nn.ELU(),
45 |             weight_norm(
46 |                 nn.Conv1d(cond_channels, cond_channels, kernel_size=3, padding=1)
47 |             ),
48 |             nn.ELU(),
49 |         )
50 |         self.classifier = nn.Linear(in_features=cond_channels, out_features=self.num_class)
51 | 
52 |     def forward(self, x: torch.Tensor) -> torch.Tensor:
53 |         x = self.condnet(x)
54 |         x = x.transpose(1, 2)
55 |         return torch.abs(self.classifier(x).squeeze(-1))
56 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/flow.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Zhihao Du)
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | import logging
 15 | import random
 16 | from typing import Dict, Optional
 17 | import torch
 18 | import torch.nn as nn
 19 | from torch.nn import functional as F
 20 | from .utils.mask import make_pad_mask
 21 | from .configs import CFM_PARAMS
 22 | 
 23 | 
 24 | class MaskedDiffWithXvec(torch.nn.Module):
 25 |     def __init__(
 26 |         self,
 27 |         input_size: int = 512,
 28 |         output_size: int = 80,
 29 |         spk_embed_dim: int = 192,
 30 |         output_type: str = "mel",
 31 |         vocab_size: int = 4096,
 32 |         input_frame_rate: int = 50,
 33 |         only_mask_loss: bool = True,
 34 |         encoder: torch.nn.Module = None,
 35 |         length_regulator: torch.nn.Module = None,
 36 |         decoder: torch.nn.Module = None,
 37 |         decoder_conf: Dict = {
 38 |             'in_channels': 240,
 39 |             'out_channel': 80,
 40 |             'spk_emb_dim': 80,
 41 |             'n_spks': 1,
 42 |             'cfm_params': CFM_PARAMS,
 43 |             'decoder_params': {
 44 |                 'channels': [256, 256],
 45 |                 'dropout': 0.0,
 46 |                 'attention_head_dim': 64,
 47 |                 'n_blocks': 4,
 48 |                 'num_mid_blocks': 12,
 49 |                 'num_heads': 8,
 50 |                 'act_fn': 'gelu',
 51 |             }
 52 |         },
 53 |         mel_feat_conf: Dict = {
 54 |             'n_fft': 1024,
 55 |             'num_mels': 80,
 56 |             'sampling_rate': 22050,
 57 |             'hop_size': 256,
 58 |             'win_size': 1024,
 59 |             'fmin': 0,
 60 |             'fmax': 8000
 61 |         }
 62 |     ):
 63 |         super().__init__()
 64 |         self.input_size = input_size
 65 |         self.output_size = output_size
 66 |         self.decoder_conf = decoder_conf
 67 |         self.mel_feat_conf = mel_feat_conf
 68 |         self.vocab_size = vocab_size
 69 |         self.output_type = output_type
 70 |         self.input_frame_rate = input_frame_rate
 71 |         logging.info(f"input frame rate={self.input_frame_rate}")
 72 |         self.input_embedding = nn.Embedding(vocab_size, input_size)
 73 |         self.spk_embed_affine_layer = torch.nn.Linear(spk_embed_dim, output_size)
 74 |         self.encoder = encoder
 75 |         self.encoder_proj = torch.nn.Linear(self.encoder.output_size(), output_size)
 76 |         self.decoder = decoder
 77 |         self.length_regulator = length_regulator
 78 |         self.only_mask_loss = only_mask_loss
 79 | 
 80 |     def forward(
 81 |             self,
 82 |             batch: dict,
 83 |             device: torch.device,
 84 |     ) -> Dict[str, Optional[torch.Tensor]]:
 85 |         token = batch['speech_token'].to(device)
 86 |         token_len = batch['speech_token_len'].to(device)
 87 |         feat = batch['speech_feat'].to(device)
 88 |         feat_len = batch['speech_feat_len'].to(device)
 89 |         embedding = batch['embedding'].to(device)
 90 | 
 91 |         # xvec projection
 92 |         embedding = F.normalize(embedding, dim=1)
 93 |         embedding = self.spk_embed_affine_layer(embedding)
 94 | 
 95 |         # concat text and prompt_text
 96 |         mask = (~make_pad_mask(token_len)).float().unsqueeze(-1).to(device)
 97 |         token = self.input_embedding(torch.clamp(token, min=0)) * mask
 98 | 
 99 |         # text encode
100 |         h, h_lengths = self.encoder(token, token_len)
101 |         h = self.encoder_proj(h)
102 |         h, h_lengths = self.length_regulator(h, feat_len)
103 | 
104 |         # get conditions
105 |         conds = torch.zeros(feat.shape, device=token.device)
106 |         for i, j in enumerate(feat_len):
107 |             if random.random() < 0.5:
108 |                 continue
109 |             index = random.randint(0, int(0.3 * j))
110 |             conds[i, :index] = feat[i, :index]
111 |         conds = conds.transpose(1, 2)
112 | 
113 |         mask = (~make_pad_mask(feat_len)).to(h)
114 |         feat = F.interpolate(feat.unsqueeze(dim=1), size=h.shape[1:], mode="nearest").squeeze(dim=1)
115 |         loss, _ = self.decoder.compute_loss(
116 |             feat.transpose(1, 2).contiguous(),
117 |             mask.unsqueeze(1),
118 |             h.transpose(1, 2).contiguous(),
119 |             embedding,
120 |             cond=conds
121 |         )
122 |         return {'loss': loss}
123 | 
124 |     @torch.inference_mode()
125 |     def inference(self,
126 |                   token,
127 |                   token_len,
128 |                   prompt_token,
129 |                   prompt_token_len,
130 |                   prompt_feat,
131 |                   prompt_feat_len,
132 |                   embedding,
133 |                   flow_cache):
134 |         if self.fp16 is True:
135 |             prompt_feat = prompt_feat.half()
136 |             embedding = embedding.half()
137 | 
138 |         assert token.shape[0] == 1
139 |         # xvec projection
140 |         embedding = F.normalize(embedding, dim=1)
141 |         embedding = self.spk_embed_affine_layer(embedding)
142 | 
143 |         # concat text and prompt_text
144 |         token_len1, token_len2 = prompt_token.shape[1], token.shape[1]
145 |         token, token_len = torch.concat([prompt_token, token], dim=1), prompt_token_len + token_len
146 |         mask = (~make_pad_mask(token_len)).unsqueeze(-1).to(embedding)
147 |         token = self.input_embedding(torch.clamp(token, min=0)) * mask
148 | 
149 |         # text encode
150 |         h, h_lengths = self.encoder(token, token_len)
151 |         h = self.encoder_proj(h)
152 |         mel_len1, mel_len2 = prompt_feat.shape[1], int(token_len2 / self.input_frame_rate * 22050 / 256)
153 |         h, h_lengths = self.length_regulator.inference(h[:, :token_len1], h[:, token_len1:], mel_len1, mel_len2, self.input_frame_rate)
154 | 
155 |         # get conditions
156 |         conds = torch.zeros([1, mel_len1 + mel_len2, self.output_size], device=token.device).to(h.dtype)
157 |         conds[:, :mel_len1] = prompt_feat
158 |         conds = conds.transpose(1, 2)
159 | 
160 |         mask = (~make_pad_mask(torch.tensor([mel_len1 + mel_len2]))).to(h)
161 |         feat, flow_cache = self.decoder(
162 |             mu=h.transpose(1, 2).contiguous(),
163 |             mask=mask.unsqueeze(1),
164 |             spks=embedding,
165 |             cond=conds,
166 |             n_timesteps=10,
167 |             prompt_len=mel_len1,
168 |             flow_cache=flow_cache
169 |         )
170 |         feat = feat[:, :, mel_len1:]
171 |         assert feat.shape[2] == mel_len2
172 |         return feat.float(), flow_cache
173 | 
174 | 
175 | class CausalMaskedDiffWithXvec(torch.nn.Module):
176 |     def __init__(
177 |         self,
178 |         input_size: int = 512,
179 |         output_size: int = 80,
180 |         spk_embed_dim: int = 192,
181 |         output_type: str = "mel",
182 |         vocab_size: int = 6561,
183 |         input_frame_rate: int = 25,
184 |         only_mask_loss: bool = True,
185 |         token_mel_ratio: int = 2,
186 |         pre_lookahead_len: int = 3,
187 |         encoder: torch.nn.Module = None,
188 |         decoder: torch.nn.Module = None,
189 |         decoder_conf: Dict = {
190 |             'in_channels': 240,
191 |             'out_channel': 80,
192 |             'spk_emb_dim': 80,
193 |             'n_spks': 1,
194 |             'cfm_params': CFM_PARAMS,
195 |             'decoder_params': {
196 |                 'channels': [256, 256],
197 |                 'dropout': 0.0,
198 |                 'attention_head_dim': 64,
199 |                 'n_blocks': 4,
200 |                 'num_mid_blocks': 12,
201 |                 'num_heads': 8,
202 |                 'act_fn': 'gelu',
203 |             }
204 |         },
205 |         mel_feat_conf: Dict = {
206 |             'n_fft': 1024,
207 |             'num_mels': 80,
208 |             'sampling_rate': 22050,
209 |             'hop_size': 256,
210 |             'win_size': 1024,
211 |             'fmin': 0,
212 |             'fmax': 8000
213 |         }
214 |     ):
215 |         super().__init__()
216 |         self.input_size = input_size
217 |         self.output_size = output_size
218 |         self.decoder_conf = decoder_conf
219 |         self.mel_feat_conf = mel_feat_conf
220 |         self.vocab_size = vocab_size
221 |         self.output_type = output_type
222 |         self.input_frame_rate = input_frame_rate
223 |         logging.info(f"input frame rate={self.input_frame_rate}")
224 |         self.input_embedding = nn.Embedding(vocab_size, input_size)
225 |         self.spk_embed_affine_layer = torch.nn.Linear(spk_embed_dim, output_size)
226 |         self.encoder = encoder
227 |         self.encoder_proj = torch.nn.Linear(self.encoder.output_size(), output_size)
228 |         self.decoder = decoder
229 |         self.only_mask_loss = only_mask_loss
230 |         self.token_mel_ratio = token_mel_ratio
231 |         self.pre_lookahead_len = pre_lookahead_len
232 | 
233 |         # FIXME: this was missing - just putting it in as false
234 |         self.fp16 = False
235 | 
236 |     @torch.inference_mode()
237 |     def inference(self,
238 |                   token,
239 |                   token_len,
240 |                   prompt_token,
241 |                   prompt_token_len,
242 |                   prompt_feat,
243 |                   prompt_feat_len,
244 |                   embedding,
245 |                   finalize):
246 |         if self.fp16 is True:
247 |             prompt_feat = prompt_feat.half()
248 |             embedding = embedding.half()
249 | 
250 |         assert token.shape[0] == 1
251 |         # xvec projection
252 |         embedding = F.normalize(embedding, dim=1)
253 |         embedding = self.spk_embed_affine_layer(embedding)
254 | 
255 |         # concat text and prompt_text
256 |         token, token_len = torch.concat([prompt_token, token], dim=1), prompt_token_len + token_len
257 |         mask = (~make_pad_mask(token_len)).unsqueeze(-1).to(embedding)
258 |         token = self.input_embedding(torch.clamp(token, min=0)) * mask
259 | 
260 |         # text encode
261 |         h, h_lengths = self.encoder(token, token_len)
262 |         if finalize is False:
263 |             h = h[:, :-self.pre_lookahead_len * self.token_mel_ratio]
264 |         mel_len1, mel_len2 = prompt_feat.shape[1], h.shape[1] - prompt_feat.shape[1]
265 |         h = self.encoder_proj(h)
266 | 
267 |         # get conditions
268 |         conds = torch.zeros([1, mel_len1 + mel_len2, self.output_size], device=token.device).to(h.dtype)
269 |         conds[:, :mel_len1] = prompt_feat
270 |         conds = conds.transpose(1, 2)
271 | 
272 |         mask = (~make_pad_mask(torch.tensor([mel_len1 + mel_len2]))).to(h)
273 |         feat, _ = self.decoder(
274 |             mu=h.transpose(1, 2).contiguous(),
275 |             mask=mask.unsqueeze(1),
276 |             spks=embedding,
277 |             cond=conds,
278 |             n_timesteps=10
279 |         )
280 |         feat = feat[:, :, mel_len1:]
281 |         assert feat.shape[2] == mel_len2
282 |         return feat.float(), None  # NOTE jrm: why are they returning None here?
283 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/flow_matching.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2024 Alibaba Inc (authors: Xiang Lyu, Zhihao Du)
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | import threading
 15 | import torch
 16 | import torch.nn.functional as F
 17 | from .matcha.flow_matching import BASECFM
 18 | from .configs import CFM_PARAMS
 19 | 
 20 | 
 21 | class ConditionalCFM(BASECFM):
 22 |     def __init__(self, in_channels, cfm_params, n_spks=1, spk_emb_dim=64, estimator: torch.nn.Module = None):
 23 |         super().__init__(
 24 |             n_feats=in_channels,
 25 |             cfm_params=cfm_params,
 26 |             n_spks=n_spks,
 27 |             spk_emb_dim=spk_emb_dim,
 28 |         )
 29 |         self.t_scheduler = cfm_params.t_scheduler
 30 |         self.training_cfg_rate = cfm_params.training_cfg_rate
 31 |         self.inference_cfg_rate = cfm_params.inference_cfg_rate
 32 |         in_channels = in_channels + (spk_emb_dim if n_spks > 0 else 0)
 33 |         # Just change the architecture of the estimator here
 34 |         self.estimator = estimator
 35 |         self.lock = threading.Lock()
 36 | 
 37 |     @torch.inference_mode()
 38 |     def forward(self, mu, mask, n_timesteps, temperature=1.0, spks=None, cond=None, prompt_len=0, flow_cache=torch.zeros(1, 80, 0, 2)):
 39 |         """Forward diffusion
 40 | 
 41 |         Args:
 42 |             mu (torch.Tensor): output of encoder
 43 |                 shape: (batch_size, n_feats, mel_timesteps)
 44 |             mask (torch.Tensor): output_mask
 45 |                 shape: (batch_size, 1, mel_timesteps)
 46 |             n_timesteps (int): number of diffusion steps
 47 |             temperature (float, optional): temperature for scaling noise. Defaults to 1.0.
 48 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 49 |                 shape: (batch_size, spk_emb_dim)
 50 |             cond: Not used but kept for future purposes
 51 | 
 52 |         Returns:
 53 |             sample: generated mel-spectrogram
 54 |                 shape: (batch_size, n_feats, mel_timesteps)
 55 |         """
 56 | 
 57 |         z = torch.randn_like(mu).to(mu.device).to(mu.dtype) * temperature
 58 |         cache_size = flow_cache.shape[2]
 59 |         # fix prompt and overlap part mu and z
 60 |         if cache_size != 0:
 61 |             z[:, :, :cache_size] = flow_cache[:, :, :, 0]
 62 |             mu[:, :, :cache_size] = flow_cache[:, :, :, 1]
 63 |         z_cache = torch.concat([z[:, :, :prompt_len], z[:, :, -34:]], dim=2)
 64 |         mu_cache = torch.concat([mu[:, :, :prompt_len], mu[:, :, -34:]], dim=2)
 65 |         flow_cache = torch.stack([z_cache, mu_cache], dim=-1)
 66 | 
 67 |         t_span = torch.linspace(0, 1, n_timesteps + 1, device=mu.device, dtype=mu.dtype)
 68 |         if self.t_scheduler == 'cosine':
 69 |             t_span = 1 - torch.cos(t_span * 0.5 * torch.pi)
 70 |         return self.solve_euler(z, t_span=t_span, mu=mu, mask=mask, spks=spks, cond=cond), flow_cache
 71 | 
 72 |     def solve_euler(self, x, t_span, mu, mask, spks, cond):
 73 |         """
 74 |         Fixed euler solver for ODEs.
 75 |         Args:
 76 |             x (torch.Tensor): random noise
 77 |             t_span (torch.Tensor): n_timesteps interpolated
 78 |                 shape: (n_timesteps + 1,)
 79 |             mu (torch.Tensor): output of encoder
 80 |                 shape: (batch_size, n_feats, mel_timesteps)
 81 |             mask (torch.Tensor): output_mask
 82 |                 shape: (batch_size, 1, mel_timesteps)
 83 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 84 |                 shape: (batch_size, spk_emb_dim)
 85 |             cond: Not used but kept for future purposes
 86 |         """
 87 |         t, _, dt = t_span[0], t_span[-1], t_span[1] - t_span[0]
 88 |         t = t.unsqueeze(dim=0)
 89 | 
 90 |         # I am storing this because I can later plot it by putting a debugger here and saving it to a file
 91 |         # Or in future might add like a return_all_steps flag
 92 |         sol = []
 93 | 
 94 |         # Do not use concat, it may cause memory format changed and trt infer with wrong results!
 95 |         x_in = torch.zeros([2, 80, x.size(2)], device=x.device, dtype=x.dtype)
 96 |         mask_in = torch.zeros([2, 1, x.size(2)], device=x.device, dtype=x.dtype)
 97 |         mu_in = torch.zeros([2, 80, x.size(2)], device=x.device, dtype=x.dtype)
 98 |         t_in = torch.zeros([2], device=x.device, dtype=x.dtype)
 99 |         spks_in = torch.zeros([2, 80], device=x.device, dtype=x.dtype)
100 |         cond_in = torch.zeros([2, 80, x.size(2)], device=x.device, dtype=x.dtype)
101 |         for step in range(1, len(t_span)):
102 |             # Classifier-Free Guidance inference introduced in VoiceBox
103 |             x_in[:] = x
104 |             mask_in[:] = mask
105 |             mu_in[0] = mu
106 |             t_in[:] = t.unsqueeze(0)
107 |             spks_in[0] = spks
108 |             cond_in[0] = cond
109 |             dphi_dt = self.forward_estimator(
110 |                 x_in, mask_in,
111 |                 mu_in, t_in,
112 |                 spks_in,
113 |                 cond_in
114 |             )
115 |             dphi_dt, cfg_dphi_dt = torch.split(dphi_dt, [x.size(0), x.size(0)], dim=0)
116 |             dphi_dt = ((1.0 + self.inference_cfg_rate) * dphi_dt - self.inference_cfg_rate * cfg_dphi_dt)
117 |             x = x + dt * dphi_dt
118 |             t = t + dt
119 |             sol.append(x)
120 |             if step < len(t_span) - 1:
121 |                 dt = t_span[step + 1] - t
122 | 
123 |         return sol[-1].float()
124 | 
125 |     def forward_estimator(self, x, mask, mu, t, spks, cond):
126 |         if isinstance(self.estimator, torch.nn.Module):
127 |             return self.estimator.forward(x, mask, mu, t, spks, cond)
128 |         else:
129 |             with self.lock:
130 |                 self.estimator.set_input_shape('x', (2, 80, x.size(2)))
131 |                 self.estimator.set_input_shape('mask', (2, 1, x.size(2)))
132 |                 self.estimator.set_input_shape('mu', (2, 80, x.size(2)))
133 |                 self.estimator.set_input_shape('t', (2,))
134 |                 self.estimator.set_input_shape('spks', (2, 80))
135 |                 self.estimator.set_input_shape('cond', (2, 80, x.size(2)))
136 |                 # run trt engine
137 |                 self.estimator.execute_v2([x.contiguous().data_ptr(),
138 |                                            mask.contiguous().data_ptr(),
139 |                                            mu.contiguous().data_ptr(),
140 |                                            t.contiguous().data_ptr(),
141 |                                            spks.contiguous().data_ptr(),
142 |                                            cond.contiguous().data_ptr(),
143 |                                            x.data_ptr()])
144 |             return x
145 | 
146 |     def compute_loss(self, x1, mask, mu, spks=None, cond=None):
147 |         """Computes diffusion loss
148 | 
149 |         Args:
150 |             x1 (torch.Tensor): Target
151 |                 shape: (batch_size, n_feats, mel_timesteps)
152 |             mask (torch.Tensor): target mask
153 |                 shape: (batch_size, 1, mel_timesteps)
154 |             mu (torch.Tensor): output of encoder
155 |                 shape: (batch_size, n_feats, mel_timesteps)
156 |             spks (torch.Tensor, optional): speaker embedding. Defaults to None.
157 |                 shape: (batch_size, spk_emb_dim)
158 | 
159 |         Returns:
160 |             loss: conditional flow matching loss
161 |             y: conditional flow
162 |                 shape: (batch_size, n_feats, mel_timesteps)
163 |         """
164 |         b, _, t = mu.shape
165 | 
166 |         # random timestep
167 |         t = torch.rand([b, 1, 1], device=mu.device, dtype=mu.dtype)
168 |         if self.t_scheduler == 'cosine':
169 |             t = 1 - torch.cos(t * 0.5 * torch.pi)
170 |         # sample noise p(x_0)
171 |         z = torch.randn_like(x1)
172 | 
173 |         y = (1 - (1 - self.sigma_min) * t) * z + t * x1
174 |         u = x1 - (1 - self.sigma_min) * z
175 | 
176 |         # during training, we randomly drop condition to trade off mode coverage and sample fidelity
177 |         if self.training_cfg_rate > 0:
178 |             cfg_mask = torch.rand(b, device=x1.device) > self.training_cfg_rate
179 |             mu = mu * cfg_mask.view(-1, 1, 1)
180 |             spks = spks * cfg_mask.view(-1, 1)
181 |             cond = cond * cfg_mask.view(-1, 1, 1)
182 | 
183 |         pred = self.estimator(y, mask, mu, t.squeeze(), spks, cond)
184 |         loss = F.mse_loss(pred * mask, u * mask, reduction="sum") / (torch.sum(mask) * u.shape[1])
185 |         return loss, y
186 | 
187 | 
188 | class CausalConditionalCFM(ConditionalCFM):
189 |     def __init__(self, in_channels=240, cfm_params=CFM_PARAMS, n_spks=1, spk_emb_dim=80, estimator=None):
190 |         super().__init__(in_channels, cfm_params, n_spks, spk_emb_dim, estimator)
191 |         self.rand_noise = torch.randn([1, 80, 50 * 300])
192 | 
193 |     @torch.inference_mode()
194 |     def forward(self, mu, mask, n_timesteps, temperature=1.0, spks=None, cond=None):
195 |         """Forward diffusion
196 | 
197 |         Args:
198 |             mu (torch.Tensor): output of encoder
199 |                 shape: (batch_size, n_feats, mel_timesteps)
200 |             mask (torch.Tensor): output_mask
201 |                 shape: (batch_size, 1, mel_timesteps)
202 |             n_timesteps (int): number of diffusion steps
203 |             temperature (float, optional): temperature for scaling noise. Defaults to 1.0.
204 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
205 |                 shape: (batch_size, spk_emb_dim)
206 |             cond: Not used but kept for future purposes
207 | 
208 |         Returns:
209 |             sample: generated mel-spectrogram
210 |                 shape: (batch_size, n_feats, mel_timesteps)
211 |         """
212 | 
213 |         z = self.rand_noise[:, :, :mu.size(2)].to(mu.device).to(mu.dtype) * temperature
214 |         # fix prompt and overlap part mu and z
215 |         t_span = torch.linspace(0, 1, n_timesteps + 1, device=mu.device, dtype=mu.dtype)
216 |         if self.t_scheduler == 'cosine':
217 |             t_span = 1 - torch.cos(t_span * 0.5 * torch.pi)
218 |         return self.solve_euler(z, t_span=t_span, mu=mu, mask=mask, spks=spks, cond=cond), None
219 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/matcha/flow_matching.py:
--------------------------------------------------------------------------------
  1 | from abc import ABC
  2 | 
  3 | import torch
  4 | import torch.nn.functional as F
  5 | 
  6 | from .decoder import Decoder
  7 | 
  8 | 
  9 | class BASECFM(torch.nn.Module, ABC):
 10 |     def __init__(
 11 |         self,
 12 |         n_feats,
 13 |         cfm_params,
 14 |         n_spks=1,
 15 |         spk_emb_dim=128,
 16 |     ):
 17 |         super().__init__()
 18 |         self.n_feats = n_feats
 19 |         self.n_spks = n_spks
 20 |         self.spk_emb_dim = spk_emb_dim
 21 |         self.solver = cfm_params.solver
 22 |         if hasattr(cfm_params, "sigma_min"):
 23 |             self.sigma_min = cfm_params.sigma_min
 24 |         else:
 25 |             self.sigma_min = 1e-4
 26 | 
 27 |         self.estimator = None
 28 | 
 29 |     @torch.inference_mode()
 30 |     def forward(self, mu, mask, n_timesteps, temperature=1.0, spks=None, cond=None):
 31 |         """Forward diffusion
 32 | 
 33 |         Args:
 34 |             mu (torch.Tensor): output of encoder
 35 |                 shape: (batch_size, n_feats, mel_timesteps)
 36 |             mask (torch.Tensor): output_mask
 37 |                 shape: (batch_size, 1, mel_timesteps)
 38 |             n_timesteps (int): number of diffusion steps
 39 |             temperature (float, optional): temperature for scaling noise. Defaults to 1.0.
 40 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 41 |                 shape: (batch_size, spk_emb_dim)
 42 |             cond: Not used but kept for future purposes
 43 | 
 44 |         Returns:
 45 |             sample: generated mel-spectrogram
 46 |                 shape: (batch_size, n_feats, mel_timesteps)
 47 |         """
 48 |         z = torch.randn_like(mu) * temperature
 49 |         t_span = torch.linspace(0, 1, n_timesteps + 1, device=mu.device)
 50 |         return self.solve_euler(z, t_span=t_span, mu=mu, mask=mask, spks=spks, cond=cond)
 51 | 
 52 |     def solve_euler(self, x, t_span, mu, mask, spks, cond):
 53 |         """
 54 |         Fixed euler solver for ODEs.
 55 |         Args:
 56 |             x (torch.Tensor): random noise
 57 |             t_span (torch.Tensor): n_timesteps interpolated
 58 |                 shape: (n_timesteps + 1,)
 59 |             mu (torch.Tensor): output of encoder
 60 |                 shape: (batch_size, n_feats, mel_timesteps)
 61 |             mask (torch.Tensor): output_mask
 62 |                 shape: (batch_size, 1, mel_timesteps)
 63 |             spks (torch.Tensor, optional): speaker ids. Defaults to None.
 64 |                 shape: (batch_size, spk_emb_dim)
 65 |             cond: Not used but kept for future purposes
 66 |         """
 67 |         t, _, dt = t_span[0], t_span[-1], t_span[1] - t_span[0]
 68 | 
 69 |         # I am storing this because I can later plot it by putting a debugger here and saving it to a file
 70 |         # Or in future might add like a return_all_steps flag
 71 |         sol = []
 72 | 
 73 |         for step in range(1, len(t_span)):
 74 |             dphi_dt = self.estimator(x, mask, mu, t, spks, cond)
 75 | 
 76 |             x = x + dt * dphi_dt
 77 |             t = t + dt
 78 |             sol.append(x)
 79 |             if step < len(t_span) - 1:
 80 |                 dt = t_span[step + 1] - t
 81 | 
 82 |         return sol[-1]
 83 | 
 84 |     def compute_loss(self, x1, mask, mu, spks=None, cond=None):
 85 |         """Computes diffusion loss
 86 | 
 87 |         Args:
 88 |             x1 (torch.Tensor): Target
 89 |                 shape: (batch_size, n_feats, mel_timesteps)
 90 |             mask (torch.Tensor): target mask
 91 |                 shape: (batch_size, 1, mel_timesteps)
 92 |             mu (torch.Tensor): output of encoder
 93 |                 shape: (batch_size, n_feats, mel_timesteps)
 94 |             spks (torch.Tensor, optional): speaker embedding. Defaults to None.
 95 |                 shape: (batch_size, spk_emb_dim)
 96 | 
 97 |         Returns:
 98 |             loss: conditional flow matching loss
 99 |             y: conditional flow
100 |                 shape: (batch_size, n_feats, mel_timesteps)
101 |         """
102 |         b, _, t = mu.shape
103 | 
104 |         # random timestep
105 |         t = torch.rand([b, 1, 1], device=mu.device, dtype=mu.dtype)
106 |         # sample noise p(x_0)
107 |         z = torch.randn_like(x1)
108 | 
109 |         y = (1 - (1 - self.sigma_min) * t) * z + t * x1
110 |         u = x1 - (1 - self.sigma_min) * z
111 | 
112 |         loss = F.mse_loss(self.estimator(y, mask, mu, t.squeeze(), spks), u, reduction="sum") / (
113 |             torch.sum(mask) * u.shape[1]
114 |         )
115 |         return loss, y
116 | 
117 | 
118 | class CFM(BASECFM):
119 |     def __init__(self, in_channels, out_channel, cfm_params, decoder_params, n_spks=1, spk_emb_dim=64):
120 |         super().__init__(
121 |             n_feats=in_channels,
122 |             cfm_params=cfm_params,
123 |             n_spks=n_spks,
124 |             spk_emb_dim=spk_emb_dim,
125 |         )
126 | 
127 |         in_channels = in_channels + (spk_emb_dim if n_spks > 1 else 0)
128 |         # Just change the architecture of the estimator here
129 |         self.estimator = Decoder(in_channels=in_channels, out_channels=out_channel, **decoder_params)
130 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/matcha/transformer.py:
--------------------------------------------------------------------------------
  1 | from typing import Any, Dict, Optional
  2 | 
  3 | import torch
  4 | import torch.nn as nn
  5 | from diffusers.models.attention import (
  6 |     GEGLU,
  7 |     GELU,
  8 |     AdaLayerNorm,
  9 |     AdaLayerNormZero,
 10 |     ApproximateGELU,
 11 | )
 12 | from diffusers.models.attention_processor import Attention
 13 | from diffusers.models.lora import LoRACompatibleLinear
 14 | from diffusers.utils.torch_utils import maybe_allow_in_graph
 15 | 
 16 | 
 17 | class SnakeBeta(nn.Module):
 18 |     """
 19 |     A modified Snake function which uses separate parameters for the magnitude of the periodic components
 20 |     Shape:
 21 |         - Input: (B, C, T)
 22 |         - Output: (B, C, T), same shape as the input
 23 |     Parameters:
 24 |         - alpha - trainable parameter that controls frequency
 25 |         - beta - trainable parameter that controls magnitude
 26 |     References:
 27 |         - This activation function is a modified version based on this paper by Liu Ziyin, Tilman Hartwig, Masahito Ueda:
 28 |         https://arxiv.org/abs/2006.08195
 29 |     Examples:
 30 |         >>> a1 = snakebeta(256)
 31 |         >>> x = torch.randn(256)
 32 |         >>> x = a1(x)
 33 |     """
 34 | 
 35 |     def __init__(self, in_features, out_features, alpha=1.0, alpha_trainable=True, alpha_logscale=True):
 36 |         """
 37 |         Initialization.
 38 |         INPUT:
 39 |             - in_features: shape of the input
 40 |             - alpha - trainable parameter that controls frequency
 41 |             - beta - trainable parameter that controls magnitude
 42 |             alpha is initialized to 1 by default, higher values = higher-frequency.
 43 |             beta is initialized to 1 by default, higher values = higher-magnitude.
 44 |             alpha will be trained along with the rest of your model.
 45 |         """
 46 |         super().__init__()
 47 |         self.in_features = out_features if isinstance(out_features, list) else [out_features]
 48 |         self.proj = LoRACompatibleLinear(in_features, out_features)
 49 | 
 50 |         # initialize alpha
 51 |         self.alpha_logscale = alpha_logscale
 52 |         if self.alpha_logscale:  # log scale alphas initialized to zeros
 53 |             self.alpha = nn.Parameter(torch.zeros(self.in_features) * alpha)
 54 |             self.beta = nn.Parameter(torch.zeros(self.in_features) * alpha)
 55 |         else:  # linear scale alphas initialized to ones
 56 |             self.alpha = nn.Parameter(torch.ones(self.in_features) * alpha)
 57 |             self.beta = nn.Parameter(torch.ones(self.in_features) * alpha)
 58 | 
 59 |         self.alpha.requires_grad = alpha_trainable
 60 |         self.beta.requires_grad = alpha_trainable
 61 | 
 62 |         self.no_div_by_zero = 0.000000001
 63 | 
 64 |     def forward(self, x):
 65 |         """
 66 |         Forward pass of the function.
 67 |         Applies the function to the input elementwise.
 68 |         SnakeBeta ∶= x + 1/b * sin^2 (xa)
 69 |         """
 70 |         x = self.proj(x)
 71 |         if self.alpha_logscale:
 72 |             alpha = torch.exp(self.alpha)
 73 |             beta = torch.exp(self.beta)
 74 |         else:
 75 |             alpha = self.alpha
 76 |             beta = self.beta
 77 | 
 78 |         x = x + (1.0 / (beta + self.no_div_by_zero)) * torch.pow(torch.sin(x * alpha), 2)
 79 | 
 80 |         return x
 81 | 
 82 | 
 83 | class FeedForward(nn.Module):
 84 |     r"""
 85 |     A feed-forward layer.
 86 | 
 87 |     Parameters:
 88 |         dim (`int`): The number of channels in the input.
 89 |         dim_out (`int`, *optional*): The number of channels in the output. If not given, defaults to `dim`.
 90 |         mult (`int`, *optional*, defaults to 4): The multiplier to use for the hidden dimension.
 91 |         dropout (`float`, *optional*, defaults to 0.0): The dropout probability to use.
 92 |         activation_fn (`str`, *optional*, defaults to `"geglu"`): Activation function to be used in feed-forward.
 93 |         final_dropout (`bool` *optional*, defaults to False): Apply a final dropout.
 94 |     """
 95 | 
 96 |     def __init__(
 97 |         self,
 98 |         dim: int,
 99 |         dim_out: Optional[int] = None,
100 |         mult: int = 4,
101 |         dropout: float = 0.0,
102 |         activation_fn: str = "geglu",
103 |         final_dropout: bool = False,
104 |     ):
105 |         super().__init__()
106 |         inner_dim = int(dim * mult)
107 |         dim_out = dim_out if dim_out is not None else dim
108 | 
109 |         if activation_fn == "gelu":
110 |             act_fn = GELU(dim, inner_dim)
111 |         if activation_fn == "gelu-approximate":
112 |             act_fn = GELU(dim, inner_dim, approximate="tanh")
113 |         elif activation_fn == "geglu":
114 |             act_fn = GEGLU(dim, inner_dim)
115 |         elif activation_fn == "geglu-approximate":
116 |             act_fn = ApproximateGELU(dim, inner_dim)
117 |         elif activation_fn == "snakebeta":
118 |             act_fn = SnakeBeta(dim, inner_dim)
119 | 
120 |         self.net = nn.ModuleList([])
121 |         # project in
122 |         self.net.append(act_fn)
123 |         # project dropout
124 |         self.net.append(nn.Dropout(dropout))
125 |         # project out
126 |         self.net.append(LoRACompatibleLinear(inner_dim, dim_out))
127 |         # FF as used in Vision Transformer, MLP-Mixer, etc. have a final dropout
128 |         if final_dropout:
129 |             self.net.append(nn.Dropout(dropout))
130 | 
131 |     def forward(self, hidden_states):
132 |         for module in self.net:
133 |             hidden_states = module(hidden_states)
134 |         return hidden_states
135 | 
136 | 
137 | @maybe_allow_in_graph
138 | class BasicTransformerBlock(nn.Module):
139 |     r"""
140 |     A basic Transformer block.
141 | 
142 |     Parameters:
143 |         dim (`int`): The number of channels in the input and output.
144 |         num_attention_heads (`int`): The number of heads to use for multi-head attention.
145 |         attention_head_dim (`int`): The number of channels in each head.
146 |         dropout (`float`, *optional*, defaults to 0.0): The dropout probability to use.
147 |         cross_attention_dim (`int`, *optional*): The size of the encoder_hidden_states vector for cross attention.
148 |         only_cross_attention (`bool`, *optional*):
149 |             Whether to use only cross-attention layers. In this case two cross attention layers are used.
150 |         double_self_attention (`bool`, *optional*):
151 |             Whether to use two self-attention layers. In this case no cross attention layers are used.
152 |         activation_fn (`str`, *optional*, defaults to `"geglu"`): Activation function to be used in feed-forward.
153 |         num_embeds_ada_norm (:
154 |             obj: `int`, *optional*): The number of diffusion steps used during training. See `Transformer2DModel`.
155 |         attention_bias (:
156 |             obj: `bool`, *optional*, defaults to `False`): Configure if the attentions should contain a bias parameter.
157 |     """
158 | 
159 |     def __init__(
160 |         self,
161 |         dim: int,
162 |         num_attention_heads: int,
163 |         attention_head_dim: int,
164 |         dropout=0.0,
165 |         cross_attention_dim: Optional[int] = None,
166 |         activation_fn: str = "geglu",
167 |         num_embeds_ada_norm: Optional[int] = None,
168 |         attention_bias: bool = False,
169 |         only_cross_attention: bool = False,
170 |         double_self_attention: bool = False,
171 |         upcast_attention: bool = False,
172 |         norm_elementwise_affine: bool = True,
173 |         norm_type: str = "layer_norm",
174 |         final_dropout: bool = False,
175 |     ):
176 |         super().__init__()
177 |         self.only_cross_attention = only_cross_attention
178 | 
179 |         self.use_ada_layer_norm_zero = (num_embeds_ada_norm is not None) and norm_type == "ada_norm_zero"
180 |         self.use_ada_layer_norm = (num_embeds_ada_norm is not None) and norm_type == "ada_norm"
181 | 
182 |         if norm_type in ("ada_norm", "ada_norm_zero") and num_embeds_ada_norm is None:
183 |             raise ValueError(
184 |                 f"`norm_type` is set to {norm_type}, but `num_embeds_ada_norm` is not defined. Please make sure to"
185 |                 f" define `num_embeds_ada_norm` if setting `norm_type` to {norm_type}."
186 |             )
187 | 
188 |         # Define 3 blocks. Each block has its own normalization layer.
189 |         # 1. Self-Attn
190 |         if self.use_ada_layer_norm:
191 |             self.norm1 = AdaLayerNorm(dim, num_embeds_ada_norm)
192 |         elif self.use_ada_layer_norm_zero:
193 |             self.norm1 = AdaLayerNormZero(dim, num_embeds_ada_norm)
194 |         else:
195 |             self.norm1 = nn.LayerNorm(dim, elementwise_affine=norm_elementwise_affine)
196 |         self.attn1 = Attention(
197 |             query_dim=dim,
198 |             heads=num_attention_heads,
199 |             dim_head=attention_head_dim,
200 |             dropout=dropout,
201 |             bias=attention_bias,
202 |             cross_attention_dim=cross_attention_dim if only_cross_attention else None,
203 |             upcast_attention=upcast_attention,
204 |         )
205 | 
206 |         # 2. Cross-Attn
207 |         if cross_attention_dim is not None or double_self_attention:
208 |             # We currently only use AdaLayerNormZero for self attention where there will only be one attention block.
209 |             # I.e. the number of returned modulation chunks from AdaLayerZero would not make sense if returned during
210 |             # the second cross attention block.
211 |             self.norm2 = (
212 |                 AdaLayerNorm(dim, num_embeds_ada_norm)
213 |                 if self.use_ada_layer_norm
214 |                 else nn.LayerNorm(dim, elementwise_affine=norm_elementwise_affine)
215 |             )
216 |             self.attn2 = Attention(
217 |                 query_dim=dim,
218 |                 cross_attention_dim=cross_attention_dim if not double_self_attention else None,
219 |                 heads=num_attention_heads,
220 |                 dim_head=attention_head_dim,
221 |                 dropout=dropout,
222 |                 bias=attention_bias,
223 |                 upcast_attention=upcast_attention,
224 |                 # scale_qk=False, # uncomment this to not to use flash attention
225 |             )  # is self-attn if encoder_hidden_states is none
226 |         else:
227 |             self.norm2 = None
228 |             self.attn2 = None
229 | 
230 |         # 3. Feed-forward
231 |         self.norm3 = nn.LayerNorm(dim, elementwise_affine=norm_elementwise_affine)
232 |         self.ff = FeedForward(dim, dropout=dropout, activation_fn=activation_fn, final_dropout=final_dropout)
233 | 
234 |         # let chunk size default to None
235 |         self._chunk_size = None
236 |         self._chunk_dim = 0
237 | 
238 |     def set_chunk_feed_forward(self, chunk_size: Optional[int], dim: int):
239 |         # Sets chunk feed-forward
240 |         self._chunk_size = chunk_size
241 |         self._chunk_dim = dim
242 | 
243 |     def forward(
244 |         self,
245 |         hidden_states: torch.FloatTensor,
246 |         attention_mask: Optional[torch.FloatTensor] = None,
247 |         encoder_hidden_states: Optional[torch.FloatTensor] = None,
248 |         encoder_attention_mask: Optional[torch.FloatTensor] = None,
249 |         timestep: Optional[torch.LongTensor] = None,
250 |         cross_attention_kwargs: Dict[str, Any] = None,
251 |         class_labels: Optional[torch.LongTensor] = None,
252 |     ):
253 |         # Notice that normalization is always applied before the real computation in the following blocks.
254 |         # 1. Self-Attention
255 |         if self.use_ada_layer_norm:
256 |             norm_hidden_states = self.norm1(hidden_states, timestep)
257 |         elif self.use_ada_layer_norm_zero:
258 |             norm_hidden_states, gate_msa, shift_mlp, scale_mlp, gate_mlp = self.norm1(
259 |                 hidden_states, timestep, class_labels, hidden_dtype=hidden_states.dtype
260 |             )
261 |         else:
262 |             norm_hidden_states = self.norm1(hidden_states)
263 | 
264 |         cross_attention_kwargs = cross_attention_kwargs if cross_attention_kwargs is not None else {}
265 | 
266 |         attn_output = self.attn1(
267 |             norm_hidden_states,
268 |             encoder_hidden_states=encoder_hidden_states if self.only_cross_attention else None,
269 |             attention_mask=encoder_attention_mask if self.only_cross_attention else attention_mask,
270 |             **cross_attention_kwargs,
271 |         )
272 |         if self.use_ada_layer_norm_zero:
273 |             attn_output = gate_msa.unsqueeze(1) * attn_output
274 |         hidden_states = attn_output + hidden_states
275 | 
276 |         # 2. Cross-Attention
277 |         if self.attn2 is not None:
278 |             norm_hidden_states = (
279 |                 self.norm2(hidden_states, timestep) if self.use_ada_layer_norm else self.norm2(hidden_states)
280 |             )
281 | 
282 |             attn_output = self.attn2(
283 |                 norm_hidden_states,
284 |                 encoder_hidden_states=encoder_hidden_states,
285 |                 attention_mask=encoder_attention_mask,
286 |                 **cross_attention_kwargs,
287 |             )
288 |             hidden_states = attn_output + hidden_states
289 | 
290 |         # 3. Feed-forward
291 |         norm_hidden_states = self.norm3(hidden_states)
292 | 
293 |         if self.use_ada_layer_norm_zero:
294 |             norm_hidden_states = norm_hidden_states * (1 + scale_mlp[:, None]) + shift_mlp[:, None]
295 | 
296 |         if self._chunk_size is not None:
297 |             # "feed_forward_chunk_size" can be used to save memory
298 |             if norm_hidden_states.shape[self._chunk_dim] % self._chunk_size != 0:
299 |                 raise ValueError(
300 |                     f"`hidden_states` dimension to be chunked: {norm_hidden_states.shape[self._chunk_dim]} has to be divisible by chunk size: {self._chunk_size}. Make sure to set an appropriate `chunk_size` when calling `unet.enable_forward_chunking`."
301 |                 )
302 | 
303 |             num_chunks = norm_hidden_states.shape[self._chunk_dim] // self._chunk_size
304 |             ff_output = torch.cat(
305 |                 [self.ff(hid_slice) for hid_slice in norm_hidden_states.chunk(num_chunks, dim=self._chunk_dim)],
306 |                 dim=self._chunk_dim,
307 |             )
308 |         else:
309 |             ff_output = self.ff(norm_hidden_states)
310 | 
311 |         if self.use_ada_layer_norm_zero:
312 |             ff_output = gate_mlp.unsqueeze(1) * ff_output
313 | 
314 |         hidden_states = ff_output + hidden_states
315 | 
316 |         return hidden_states
317 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/s3gen.py:
--------------------------------------------------------------------------------
  1 | # Modified from CosyVoice https://github.com/FunAudioLLM/CosyVoice
  2 | #
  3 | # Licensed under the Apache License, Version 2.0 (the "License");
  4 | # you may not use this file except in compliance with the License.
  5 | # You may obtain a copy of the License at
  6 | #
  7 | #     http://www.apache.org/licenses/LICENSE-2.0
  8 | #
  9 | # Unless required by applicable law or agreed to in writing, software
 10 | # distributed under the License is distributed on an "AS IS" BASIS,
 11 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 12 | # See the License for the specific language governing permissions and
 13 | # limitations under the License.
 14 | 
 15 | import logging
 16 | 
 17 | import numpy as np
 18 | import torch
 19 | import torchaudio as ta
 20 | from functools import lru_cache
 21 | from typing import Optional
 22 | 
 23 | from ..s3tokenizer import S3_SR, SPEECH_VOCAB_SIZE, S3Tokenizer
 24 | from .const import S3GEN_SR
 25 | from .flow import CausalMaskedDiffWithXvec
 26 | from .xvector import CAMPPlus
 27 | from .utils.mel import mel_spectrogram
 28 | from .f0_predictor import ConvRNNF0Predictor
 29 | from .hifigan import HiFTGenerator
 30 | from .transformer.upsample_encoder import UpsampleConformerEncoder
 31 | from .flow_matching import CausalConditionalCFM
 32 | from .decoder import ConditionalDecoder
 33 | from .configs import CFM_PARAMS
 34 | 
 35 | 
 36 | def drop_invalid_tokens(x):
 37 |     assert len(x.shape) <= 2 and x.shape[0] == 1, "only batch size of one allowed for now"
 38 |     return x[x < SPEECH_VOCAB_SIZE]
 39 | 
 40 | 
 41 | # TODO: global resampler cache
 42 | @lru_cache(100)
 43 | def get_resampler(src_sr, dst_sr, device):
 44 |     return ta.transforms.Resample(src_sr, dst_sr).to(device)
 45 | 
 46 | 
 47 | class S3Token2Mel(torch.nn.Module):
 48 |     """
 49 |     CosyVoice2's CFM decoder maps S3 speech tokens to mel-spectrograms.
 50 | 
 51 |     TODO: make these modules configurable?
 52 |     """
 53 |     def __init__(self):
 54 |         super().__init__()
 55 |         self.tokenizer = S3Tokenizer("speech_tokenizer_v2_25hz")
 56 |         self.mel_extractor = mel_spectrogram # TODO: make it a torch module?
 57 |         self.speaker_encoder = CAMPPlus()  # use default args
 58 | 
 59 |         encoder = UpsampleConformerEncoder(
 60 |             output_size=512,
 61 |             attention_heads=8,
 62 |             linear_units=2048,
 63 |             num_blocks=6,
 64 |             dropout_rate=0.1,
 65 |             positional_dropout_rate=0.1,
 66 |             attention_dropout_rate=0.1,
 67 |             normalize_before=True,
 68 |             input_layer='linear',
 69 |             pos_enc_layer_type='rel_pos_espnet',
 70 |             selfattention_layer_type='rel_selfattn',
 71 |             input_size=512,
 72 |             use_cnn_module=False,
 73 |             macaron_style=False,
 74 |         )
 75 | 
 76 |         estimator = ConditionalDecoder(
 77 |             in_channels=320,
 78 |             out_channels=80,
 79 |             causal=True,
 80 |             channels=[256],
 81 |             dropout=0.0,
 82 |             attention_head_dim=64,
 83 |             n_blocks=4,
 84 |             num_mid_blocks=12,
 85 |             num_heads=8,
 86 |             act_fn='gelu',
 87 |         )
 88 |         cfm_params = CFM_PARAMS
 89 |         decoder = CausalConditionalCFM(
 90 |             spk_emb_dim=80,
 91 |             cfm_params=cfm_params,
 92 |             estimator=estimator,
 93 |         )
 94 | 
 95 |         self.flow = CausalMaskedDiffWithXvec(
 96 |             encoder=encoder,
 97 |             decoder=decoder
 98 |         )
 99 | 
100 |         self.resamplers = {}
101 | 
102 |     @property
103 |     def device(self):
104 |         params = self.tokenizer.parameters()
105 |         return next(params).device
106 | 
107 |     def embed_ref(
108 |         self,
109 |         ref_wav: torch.Tensor,
110 |         ref_sr: int,
111 |         device="auto",
112 |         ref_fade_out=True,
113 |     ):
114 |         device = self.device if device == "auto" else device
115 |         if isinstance(ref_wav, np.ndarray):
116 |             ref_wav = torch.from_numpy(ref_wav).float()
117 | 
118 |         if ref_wav.device != device:
119 |             ref_wav = ref_wav.to(device)
120 | 
121 |         if len(ref_wav.shape) == 1:
122 |             ref_wav = ref_wav.unsqueeze(0)  # (B, L)
123 | 
124 |         if ref_wav.size(1) > 10 * ref_sr:
125 |             print("WARNING: cosydec received ref longer than 10s")
126 | 
127 |         ref_wav_24 = ref_wav
128 |         if ref_sr != S3GEN_SR:
129 |             ref_wav_24 = get_resampler(ref_sr, S3GEN_SR, device)(ref_wav)
130 | 
131 |         ref_mels_24 = self.mel_extractor(ref_wav_24).transpose(1, 2).to(device)
132 |         ref_mels_24_len = None
133 | 
134 |         # Resample to 16kHz
135 |         ref_wav_16 = get_resampler(ref_sr, S3_SR, device)(ref_wav).to(device)
136 | 
137 |         # Speaker embedding
138 |         ref_x_vector = self.speaker_encoder.inference(ref_wav_16)
139 | 
140 |         # Tokenize 16khz reference
141 |         ref_speech_tokens, ref_speech_token_lens = self.tokenizer(ref_wav_16)
142 | 
143 |         # Make sure mel_len = 2 * stoken_len (happens when the input is not padded to multiple of 40ms)
144 |         if ref_mels_24.shape[1] != 2 * ref_speech_tokens.shape[1]:
145 |             logging.warning(
146 |                 "Reference mel length is not equal to 2 * reference token length.\n"
147 |             )
148 |             ref_speech_tokens = ref_speech_tokens[:, :ref_mels_24.shape[1] // 2]
149 |             ref_speech_token_lens[0] = ref_speech_tokens.shape[1]
150 | 
151 |         return dict(
152 |             prompt_token=ref_speech_tokens.to(device),
153 |             prompt_token_len=ref_speech_token_lens,
154 |             prompt_feat=ref_mels_24,
155 |             prompt_feat_len=ref_mels_24_len,
156 |             embedding=ref_x_vector,
157 |         )
158 | 
159 |     def forward(
160 |         self,
161 |         speech_tokens: torch.LongTensor,
162 |         # locally-computed ref embedding (mutex with ref_dict)
163 |         ref_wav: Optional[torch.Tensor],
164 |         ref_sr: Optional[int],
165 |         # pre-computed ref embedding (prod API)
166 |         ref_dict: Optional[dict] = None,
167 |         finalize: bool = False,
168 |     ):
169 |         """
170 |         Generate waveforms from S3 speech tokens and a reference waveform, which the speaker timbre is inferred from.
171 | 
172 |         NOTE:
173 |         - The speaker encoder accepts 16 kHz waveform.
174 |         - S3TokenizerV2 accepts 16 kHz waveform.
175 |         - The mel-spectrogram for the reference assumes 24 kHz input signal.
176 |         - This function is designed for batch_size=1 only.
177 | 
178 |         Args
179 |         ----
180 |         - `speech_tokens`: S3 speech tokens [B=1, T]
181 |         - `ref_wav`: reference waveform (`torch.Tensor` with shape=[B=1, T])
182 |         - `ref_sr`: reference sample rate
183 |         - `finalize`: whether streaming is finished or not. Note that if False, the last 3 tokens will be ignored.
184 |         """
185 |         assert (ref_wav is None) ^ (ref_dict is None), f"Must provide exactly one of ref_wav or ref_dict (got {ref_wav} and {ref_dict})"
186 | 
187 |         if ref_dict is None:
188 |             ref_dict = self.embed_ref(ref_wav, ref_sr)
189 |         else:
190 |             # type/device casting (all values will be numpy if it's from a prod API call)
191 |             for rk in list(ref_dict):
192 |                 if isinstance(ref_dict[rk], np.ndarray):
193 |                     ref_dict[rk] = torch.from_numpy(ref_dict[rk])
194 |                 if torch.is_tensor(ref_dict[rk]):
195 |                     ref_dict[rk] = ref_dict[rk].to(self.device)
196 | 
197 |         if len(speech_tokens.shape) == 1:
198 |             speech_tokens = speech_tokens.unsqueeze(0)
199 | 
200 |         # assert speech_tokens.shape[0] == 1, "only batch size of one allowed for now"
201 |         speech_token_lens = torch.LongTensor([speech_tokens.size(1)]).to(self.device)
202 | 
203 |         output_mels, _ = self.flow.inference(
204 |             token=speech_tokens,
205 |             token_len=speech_token_lens,
206 |             finalize=finalize,
207 |             **ref_dict,
208 |         )
209 |         return output_mels
210 | 
211 | 
212 | class S3Token2Wav(S3Token2Mel):
213 |     """
214 |     The decoder of CosyVoice2 is a concat of token-to-mel (CFM) and a mel-to-waveform (HiFiGAN) modules.
215 | 
216 |     TODO: make these modules configurable?
217 |     """
218 | 
219 |     def __init__(self):
220 |         super().__init__()
221 | 
222 |         f0_predictor = ConvRNNF0Predictor()
223 |         self.mel2wav = HiFTGenerator(
224 |             sampling_rate=S3GEN_SR,
225 |             upsample_rates=[8, 5, 3],
226 |             upsample_kernel_sizes=[16, 11, 7],
227 |             source_resblock_kernel_sizes=[7, 7, 11],
228 |             source_resblock_dilation_sizes=[[1, 3, 5], [1, 3, 5], [1, 3, 5]],
229 |             f0_predictor=f0_predictor,
230 |         )
231 | 
232 |         # silence out a few ms and fade audio in to reduce artifacts
233 |         n_trim = S3GEN_SR // 50  # 20ms = half of a frame
234 |         trim_fade = torch.zeros(2 * n_trim)
235 |         trim_fade[n_trim:] = (torch.cos(torch.linspace(torch.pi, 0, n_trim)) + 1) / 2
236 |         self.register_buffer("trim_fade", trim_fade, persistent=False) # (buffers get automatic device casting)
237 | 
238 |     def forward(
239 |         self,
240 |         speech_tokens,
241 |         # locally-computed ref embedding (mutex with ref_dict)
242 |         ref_wav: Optional[torch.Tensor],
243 |         ref_sr: Optional[int],
244 |         # pre-computed ref embedding (prod API)
245 |         ref_dict: Optional[dict] = None,
246 |         finalize: bool = False
247 |     ):
248 |         output_mels = super().forward(speech_tokens, ref_wav=ref_wav, ref_sr=ref_sr, ref_dict=ref_dict, finalize=finalize)
249 | 
250 |         # TODO jrm: ignoring the speed control (mel interpolation) and the HiFTGAN caching mechanisms for now.
251 |         hift_cache_source = torch.zeros(1, 1, 0).to(self.device)
252 | 
253 |         output_wavs, *_ = self.mel2wav.inference(speech_feat=output_mels, cache_source=hift_cache_source)
254 | 
255 |         if not self.training:
256 |             # NOTE: ad-hoc method to reduce "spillover" from the reference clip.
257 |             output_wavs[:, :len(self.trim_fade)] *= self.trim_fade
258 | 
259 |         return output_wavs
260 | 
261 |     @torch.inference_mode()
262 |     def flow_inference(
263 |         self,
264 |         speech_tokens,
265 |         # locally-computed ref embedding (mutex with ref_dict)
266 |         ref_wav: Optional[torch.Tensor] = None,
267 |         ref_sr: Optional[int] = None,
268 |         # pre-computed ref embedding (prod API)
269 |         ref_dict: Optional[dict] = None,
270 |         finalize: bool = False,
271 |     ):
272 |         return super().forward(speech_tokens, ref_wav=ref_wav, ref_sr=ref_sr, ref_dict=ref_dict, finalize=finalize)
273 | 
274 |     @torch.inference_mode()
275 |     def hift_inference(self, speech_feat, cache_source: torch.Tensor = None):
276 |         if cache_source is None:
277 |             cache_source = torch.zeros(1, 1, 0).to(self.device)
278 |         return self.mel2wav.inference(speech_feat=speech_feat, cache_source=cache_source)
279 | 
280 |     @torch.inference_mode()
281 |     def inference(
282 |         self,
283 |         speech_tokens,
284 |         # locally-computed ref embedding (mutex with ref_dict)
285 |         ref_wav: Optional[torch.Tensor] = None,
286 |         ref_sr: Optional[int] = None,
287 |         # pre-computed ref embedding (prod API)
288 |         ref_dict: Optional[dict] = None,
289 |         cache_source: torch.Tensor = None, # NOTE: this arg is for streaming, it can probably be removed here
290 |         finalize: bool = True,
291 |     ):
292 |         output_mels = self.flow_inference(speech_tokens, ref_wav=ref_wav, ref_sr=ref_sr, ref_dict=ref_dict, finalize=finalize)
293 |         output_wavs, output_sources = self.hift_inference(output_mels, cache_source)
294 | 
295 |         # NOTE: ad-hoc method to reduce "spillover" from the reference clip.
296 |         output_wavs[:, :len(self.trim_fade)] *= self.trim_fade
297 | 
298 |         return output_wavs, output_sources
299 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/resemble-ai/chatterbox/eb90621fa748f341a5b768aed0c0c12fc561894b/src/chatterbox/models/s3gen/transformer/__init__.py


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/activation.py:
--------------------------------------------------------------------------------
 1 | # Copyright (c) 2020 Johns Hopkins University (Shinji Watanabe)
 2 | #               2020 Northwestern Polytechnical University (Pengcheng Guo)
 3 | #               2020 Mobvoi Inc (Binbin Zhang)
 4 | #               2024 Alibaba Inc (Xiang Lyu)
 5 | #
 6 | # Licensed under the Apache License, Version 2.0 (the "License");
 7 | # you may not use this file except in compliance with the License.
 8 | # You may obtain a copy of the License at
 9 | #
10 | #   http://www.apache.org/licenses/LICENSE-2.0
11 | #
12 | # Unless required by applicable law or agreed to in writing, software
13 | # distributed under the License is distributed on an "AS IS" BASIS,
14 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
15 | # See the License for the specific language governing permissions and
16 | # limitations under the License.
17 | """Swish() activation function for Conformer."""
18 | 
19 | import torch
20 | from torch import nn, sin, pow
21 | from torch.nn import Parameter
22 | 
23 | 
24 | class Swish(torch.nn.Module):
25 |     """Construct an Swish object."""
26 | 
27 |     def forward(self, x: torch.Tensor) -> torch.Tensor:
28 |         """Return Swish activation function."""
29 |         return x * torch.sigmoid(x)
30 | 
31 | 
32 | # Implementation adapted from https://github.com/EdwardDixon/snake under the MIT license.
33 | #   LICENSE is in incl_licenses directory.
34 | class Snake(nn.Module):
35 |     '''
36 |     Implementation of a sine-based periodic activation function
37 |     Shape:
38 |         - Input: (B, C, T)
39 |         - Output: (B, C, T), same shape as the input
40 |     Parameters:
41 |         - alpha - trainable parameter
42 |     References:
43 |         - This activation function is from this paper by Liu Ziyin, Tilman Hartwig, Masahito Ueda:
44 |         https://arxiv.org/abs/2006.08195
45 |     Examples:
46 |         >>> a1 = snake(256)
47 |         >>> x = torch.randn(256)
48 |         >>> x = a1(x)
49 |     '''
50 |     def __init__(self, in_features, alpha=1.0, alpha_trainable=True, alpha_logscale=False):
51 |         '''
52 |         Initialization.
53 |         INPUT:
54 |             - in_features: shape of the input
55 |             - alpha: trainable parameter
56 |             alpha is initialized to 1 by default, higher values = higher-frequency.
57 |             alpha will be trained along with the rest of your model.
58 |         '''
59 |         super(Snake, self).__init__()
60 |         self.in_features = in_features
61 | 
62 |         # initialize alpha
63 |         self.alpha_logscale = alpha_logscale
64 |         if self.alpha_logscale:  # log scale alphas initialized to zeros
65 |             self.alpha = Parameter(torch.zeros(in_features) * alpha)
66 |         else:  # linear scale alphas initialized to ones
67 |             self.alpha = Parameter(torch.ones(in_features) * alpha)
68 | 
69 |         self.alpha.requires_grad = alpha_trainable
70 | 
71 |         self.no_div_by_zero = 0.000000001
72 | 
73 |     def forward(self, x):
74 |         '''
75 |         Forward pass of the function.
76 |         Applies the function to the input elementwise.
77 |         Snake ∶= x + 1/a * sin^2 (xa)
78 |         '''
79 |         alpha = self.alpha.unsqueeze(0).unsqueeze(-1)  # line up with x to [B, C, T]
80 |         if self.alpha_logscale:
81 |             alpha = torch.exp(alpha)
82 |         x = x + (1.0 / (alpha + self.no_div_by_zero)) * pow(sin(x * alpha), 2)
83 | 
84 |         return x
85 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/convolution.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2020 Mobvoi Inc. (authors: Binbin Zhang, Di Wu)
  2 | #               2024 Alibaba Inc (Xiang Lyu)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #     http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """ConvolutionModule definition."""
 17 | 
 18 | from typing import Tuple
 19 | 
 20 | import torch
 21 | from torch import nn
 22 | 
 23 | 
 24 | class ConvolutionModule(nn.Module):
 25 |     """ConvolutionModule in Conformer model."""
 26 | 
 27 |     def __init__(self,
 28 |                  channels: int,
 29 |                  kernel_size: int = 15,
 30 |                  activation: nn.Module = nn.ReLU(),
 31 |                  norm: str = "batch_norm",
 32 |                  causal: bool = False,
 33 |                  bias: bool = True):
 34 |         """Construct an ConvolutionModule object.
 35 |         Args:
 36 |             channels (int): The number of channels of conv layers.
 37 |             kernel_size (int): Kernel size of conv layers.
 38 |             causal (int): Whether use causal convolution or not
 39 |         """
 40 |         super().__init__()
 41 | 
 42 |         self.pointwise_conv1 = nn.Conv1d(
 43 |             channels,
 44 |             2 * channels,
 45 |             kernel_size=1,
 46 |             stride=1,
 47 |             padding=0,
 48 |             bias=bias,
 49 |         )
 50 |         # self.lorder is used to distinguish if it's a causal convolution,
 51 |         # if self.lorder > 0: it's a causal convolution, the input will be
 52 |         #    padded with self.lorder frames on the left in forward.
 53 |         # else: it's a symmetrical convolution
 54 |         if causal:
 55 |             padding = 0
 56 |             self.lorder = kernel_size - 1
 57 |         else:
 58 |             # kernel_size should be an odd number for none causal convolution
 59 |             assert (kernel_size - 1) % 2 == 0
 60 |             padding = (kernel_size - 1) // 2
 61 |             self.lorder = 0
 62 |         self.depthwise_conv = nn.Conv1d(
 63 |             channels,
 64 |             channels,
 65 |             kernel_size,
 66 |             stride=1,
 67 |             padding=padding,
 68 |             groups=channels,
 69 |             bias=bias,
 70 |         )
 71 | 
 72 |         assert norm in ['batch_norm', 'layer_norm']
 73 |         if norm == "batch_norm":
 74 |             self.use_layer_norm = False
 75 |             self.norm = nn.BatchNorm1d(channels)
 76 |         else:
 77 |             self.use_layer_norm = True
 78 |             self.norm = nn.LayerNorm(channels)
 79 | 
 80 |         self.pointwise_conv2 = nn.Conv1d(
 81 |             channels,
 82 |             channels,
 83 |             kernel_size=1,
 84 |             stride=1,
 85 |             padding=0,
 86 |             bias=bias,
 87 |         )
 88 |         self.activation = activation
 89 | 
 90 |     def forward(
 91 |         self,
 92 |         x: torch.Tensor,
 93 |         mask_pad: torch.Tensor = torch.ones((0, 0, 0), dtype=torch.bool),
 94 |         cache: torch.Tensor = torch.zeros((0, 0, 0)),
 95 |     ) -> Tuple[torch.Tensor, torch.Tensor]:
 96 |         """Compute convolution module.
 97 |         Args:
 98 |             x (torch.Tensor): Input tensor (#batch, time, channels).
 99 |             mask_pad (torch.Tensor): used for batch padding (#batch, 1, time),
100 |                 (0, 0, 0) means fake mask.
101 |             cache (torch.Tensor): left context cache, it is only
102 |                 used in causal convolution (#batch, channels, cache_t),
103 |                 (0, 0, 0) meas fake cache.
104 |         Returns:
105 |             torch.Tensor: Output tensor (#batch, time, channels).
106 |         """
107 |         # exchange the temporal dimension and the feature dimension
108 |         x = x.transpose(1, 2)  # (#batch, channels, time)
109 | 
110 |         # mask batch padding
111 |         if mask_pad.size(2) > 0:  # time > 0
112 |             x.masked_fill_(~mask_pad, 0.0)
113 | 
114 |         if self.lorder > 0:
115 |             if cache.size(2) == 0:  # cache_t == 0
116 |                 x = nn.functional.pad(x, (self.lorder, 0), 'constant', 0.0)
117 |             else:
118 |                 assert cache.size(0) == x.size(0)  # equal batch
119 |                 assert cache.size(1) == x.size(1)  # equal channel
120 |                 x = torch.cat((cache, x), dim=2)
121 |             assert (x.size(2) > self.lorder)
122 |             new_cache = x[:, :, -self.lorder:]
123 |         else:
124 |             # It's better we just return None if no cache is required,
125 |             # However, for JIT export, here we just fake one tensor instead of
126 |             # None.
127 |             new_cache = torch.zeros((0, 0, 0), dtype=x.dtype, device=x.device)
128 | 
129 |         # GLU mechanism
130 |         x = self.pointwise_conv1(x)  # (batch, 2*channel, dim)
131 |         x = nn.functional.glu(x, dim=1)  # (batch, channel, dim)
132 | 
133 |         # 1D Depthwise Conv
134 |         x = self.depthwise_conv(x)
135 |         if self.use_layer_norm:
136 |             x = x.transpose(1, 2)
137 |         x = self.activation(self.norm(x))
138 |         if self.use_layer_norm:
139 |             x = x.transpose(1, 2)
140 |         x = self.pointwise_conv2(x)
141 |         # mask batch padding
142 |         if mask_pad.size(2) > 0:  # time > 0
143 |             x.masked_fill_(~mask_pad, 0.0)
144 | 
145 |         return x.transpose(1, 2), new_cache
146 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/embedding.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2020 Mobvoi Inc. (authors: Binbin Zhang, Di Wu)
  2 | #               2024 Alibaba Inc (Xiang Lyu)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #     http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """Positonal Encoding Module."""
 17 | 
 18 | import math
 19 | from typing import Tuple, Union
 20 | 
 21 | import torch
 22 | import torch.nn.functional as F
 23 | import numpy as np
 24 | 
 25 | 
 26 | class PositionalEncoding(torch.nn.Module):
 27 |     """Positional encoding.
 28 | 
 29 |     :param int d_model: embedding dim
 30 |     :param float dropout_rate: dropout rate
 31 |     :param int max_len: maximum input length
 32 | 
 33 |     PE(pos, 2i)   = sin(pos/(10000^(2i/dmodel)))
 34 |     PE(pos, 2i+1) = cos(pos/(10000^(2i/dmodel)))
 35 |     """
 36 | 
 37 |     def __init__(self,
 38 |                  d_model: int,
 39 |                  dropout_rate: float,
 40 |                  max_len: int = 5000,
 41 |                  reverse: bool = False):
 42 |         """Construct an PositionalEncoding object."""
 43 |         super().__init__()
 44 |         self.d_model = d_model
 45 |         self.xscale = math.sqrt(self.d_model)
 46 |         self.dropout = torch.nn.Dropout(p=dropout_rate)
 47 |         self.max_len = max_len
 48 | 
 49 |         self.pe = torch.zeros(self.max_len, self.d_model)
 50 |         position = torch.arange(0, self.max_len,
 51 |                                 dtype=torch.float32).unsqueeze(1)
 52 |         div_term = torch.exp(
 53 |             torch.arange(0, self.d_model, 2, dtype=torch.float32) *
 54 |             -(math.log(10000.0) / self.d_model))
 55 |         self.pe[:, 0::2] = torch.sin(position * div_term)
 56 |         self.pe[:, 1::2] = torch.cos(position * div_term)
 57 |         self.pe = self.pe.unsqueeze(0)
 58 | 
 59 |     def forward(self,
 60 |                 x: torch.Tensor,
 61 |                 offset: Union[int, torch.Tensor] = 0) \
 62 |             -> Tuple[torch.Tensor, torch.Tensor]:
 63 |         """Add positional encoding.
 64 | 
 65 |         Args:
 66 |             x (torch.Tensor): Input. Its shape is (batch, time, ...)
 67 |             offset (int, torch.tensor): position offset
 68 | 
 69 |         Returns:
 70 |             torch.Tensor: Encoded tensor. Its shape is (batch, time, ...)
 71 |             torch.Tensor: for compatibility to RelPositionalEncoding
 72 |         """
 73 | 
 74 |         self.pe = self.pe.to(x.device)
 75 |         pos_emb = self.position_encoding(offset, x.size(1), False)
 76 |         x = x * self.xscale + pos_emb
 77 |         return self.dropout(x), self.dropout(pos_emb)
 78 | 
 79 |     def position_encoding(self,
 80 |                           offset: Union[int, torch.Tensor],
 81 |                           size: int,
 82 |                           apply_dropout: bool = True) -> torch.Tensor:
 83 |         """ For getting encoding in a streaming fashion
 84 | 
 85 |         Attention!!!!!
 86 |         we apply dropout only once at the whole utterance level in a none
 87 |         streaming way, but will call this function several times with
 88 |         increasing input size in a streaming scenario, so the dropout will
 89 |         be applied several times.
 90 | 
 91 |         Args:
 92 |             offset (int or torch.tensor): start offset
 93 |             size (int): required size of position encoding
 94 | 
 95 |         Returns:
 96 |             torch.Tensor: Corresponding encoding
 97 |         """
 98 |         # How to subscript a Union type:
 99 |         #   https://github.com/pytorch/pytorch/issues/69434
100 |         if isinstance(offset, int):
101 |             assert offset + size <= self.max_len
102 |             pos_emb = self.pe[:, offset:offset + size]
103 |         elif isinstance(offset, torch.Tensor) and offset.dim() == 0:  # scalar
104 |             assert offset + size <= self.max_len
105 |             pos_emb = self.pe[:, offset:offset + size]
106 |         else:  # for batched streaming decoding on GPU
107 |             assert torch.max(offset) + size <= self.max_len
108 |             index = offset.unsqueeze(1) + \
109 |                 torch.arange(0, size).to(offset.device)  # B X T
110 |             flag = index > 0
111 |             # remove negative offset
112 |             index = index * flag
113 |             pos_emb = F.embedding(index, self.pe[0])  # B X T X d_model
114 | 
115 |         if apply_dropout:
116 |             pos_emb = self.dropout(pos_emb)
117 |         return pos_emb
118 | 
119 | 
120 | class RelPositionalEncoding(PositionalEncoding):
121 |     """Relative positional encoding module.
122 |     See : Appendix B in https://arxiv.org/abs/1901.02860
123 |     Args:
124 |         d_model (int): Embedding dimension.
125 |         dropout_rate (float): Dropout rate.
126 |         max_len (int): Maximum input length.
127 |     """
128 | 
129 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 5000):
130 |         """Initialize class."""
131 |         super().__init__(d_model, dropout_rate, max_len, reverse=True)
132 | 
133 |     def forward(self,
134 |                 x: torch.Tensor,
135 |                 offset: Union[int, torch.Tensor] = 0) \
136 |             -> Tuple[torch.Tensor, torch.Tensor]:
137 |         """Compute positional encoding.
138 |         Args:
139 |             x (torch.Tensor): Input tensor (batch, time, `*`).
140 |         Returns:
141 |             torch.Tensor: Encoded tensor (batch, time, `*`).
142 |             torch.Tensor: Positional embedding tensor (1, time, `*`).
143 |         """
144 |         self.pe = self.pe.to(x.device)
145 |         x = x * self.xscale
146 |         pos_emb = self.position_encoding(offset, x.size(1), False)
147 |         return self.dropout(x), self.dropout(pos_emb)
148 | 
149 | 
150 | class WhisperPositionalEncoding(PositionalEncoding):
151 |     """ Sinusoids position encoding used in openai-whisper.encoder
152 |     """
153 | 
154 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 1500):
155 |         super().__init__(d_model, dropout_rate, max_len)
156 |         self.xscale = 1.0
157 |         log_timescale_increment = np.log(10000) / (d_model // 2 - 1)
158 |         inv_timescales = torch.exp(-log_timescale_increment *
159 |                                    torch.arange(d_model // 2))
160 |         scaled_time = torch.arange(max_len)[:, np.newaxis] * \
161 |             inv_timescales[np.newaxis, :]
162 |         pe = torch.cat([torch.sin(scaled_time), torch.cos(scaled_time)], dim=1)
163 |         delattr(self, "pe")
164 |         self.register_buffer("pe", pe.unsqueeze(0))
165 | 
166 | 
167 | class LearnablePositionalEncoding(PositionalEncoding):
168 |     """ Learnable position encoding used in openai-whisper.decoder
169 |     """
170 | 
171 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 448):
172 |         super().__init__(d_model, dropout_rate, max_len)
173 |         # NOTE(xcsong): overwrite self.pe & self.xscale
174 |         self.pe = torch.nn.Parameter(torch.empty(1, max_len, d_model))
175 |         self.xscale = 1.0
176 | 
177 | 
178 | class NoPositionalEncoding(torch.nn.Module):
179 |     """ No position encoding
180 |     """
181 | 
182 |     def __init__(self, d_model: int, dropout_rate: float):
183 |         super().__init__()
184 |         self.d_model = d_model
185 |         self.dropout = torch.nn.Dropout(p=dropout_rate)
186 | 
187 |     def forward(self,
188 |                 x: torch.Tensor,
189 |                 offset: Union[int, torch.Tensor] = 0) \
190 |             -> Tuple[torch.Tensor, torch.Tensor]:
191 |         """ Just return zero vector for interface compatibility
192 |         """
193 |         pos_emb = torch.zeros(1, x.size(1), self.d_model).to(x.device)
194 |         return self.dropout(x), pos_emb
195 | 
196 |     def position_encoding(self, offset: Union[int, torch.Tensor],
197 |                           size: int) -> torch.Tensor:
198 |         return torch.zeros(1, size, self.d_model)
199 | 
200 | 
201 | class EspnetRelPositionalEncoding(torch.nn.Module):
202 |     """Relative positional encoding module (new implementation).
203 | 
204 |     Details can be found in https://github.com/espnet/espnet/pull/2816.
205 | 
206 |     See : Appendix B in https://arxiv.org/abs/1901.02860
207 | 
208 |     Args:
209 |         d_model (int): Embedding dimension.
210 |         dropout_rate (float): Dropout rate.
211 |         max_len (int): Maximum input length.
212 | 
213 |     """
214 | 
215 |     def __init__(self, d_model: int, dropout_rate: float, max_len: int = 5000):
216 |         """Construct an PositionalEncoding object."""
217 |         super(EspnetRelPositionalEncoding, self).__init__()
218 |         self.d_model = d_model
219 |         self.xscale = math.sqrt(self.d_model)
220 |         self.dropout = torch.nn.Dropout(p=dropout_rate)
221 |         self.pe = None
222 |         self.extend_pe(torch.tensor(0.0).expand(1, max_len))
223 | 
224 |     def extend_pe(self, x: torch.Tensor):
225 |         """Reset the positional encodings."""
226 |         if self.pe is not None:
227 |             # self.pe contains both positive and negative parts
228 |             # the length of self.pe is 2 * input_len - 1
229 |             if self.pe.size(1) >= x.size(1) * 2 - 1:
230 |                 if self.pe.dtype != x.dtype or self.pe.device != x.device:
231 |                     self.pe = self.pe.to(dtype=x.dtype, device=x.device)
232 |                 return
233 |         # Suppose `i` means to the position of query vecotr and `j` means the
234 |         # position of key vector. We use position relative positions when keys
235 |         # are to the left (i>j) and negative relative positions otherwise (i<j).
236 |         pe_positive = torch.zeros(x.size(1), self.d_model)
237 |         pe_negative = torch.zeros(x.size(1), self.d_model)
238 |         position = torch.arange(0, x.size(1), dtype=torch.float32).unsqueeze(1)
239 |         div_term = torch.exp(
240 |             torch.arange(0, self.d_model, 2, dtype=torch.float32)
241 |             * -(math.log(10000.0) / self.d_model)
242 |         )
243 |         pe_positive[:, 0::2] = torch.sin(position * div_term)
244 |         pe_positive[:, 1::2] = torch.cos(position * div_term)
245 |         pe_negative[:, 0::2] = torch.sin(-1 * position * div_term)
246 |         pe_negative[:, 1::2] = torch.cos(-1 * position * div_term)
247 | 
248 |         # Reserve the order of positive indices and concat both positive and
249 |         # negative indices. This is used to support the shifting trick
250 |         # as in https://arxiv.org/abs/1901.02860
251 |         pe_positive = torch.flip(pe_positive, [0]).unsqueeze(0)
252 |         pe_negative = pe_negative[1:].unsqueeze(0)
253 |         pe = torch.cat([pe_positive, pe_negative], dim=1)
254 |         self.pe = pe.to(device=x.device, dtype=x.dtype)
255 | 
256 |     def forward(self, x: torch.Tensor, offset: Union[int, torch.Tensor] = 0) \
257 |             -> Tuple[torch.Tensor, torch.Tensor]:
258 |         """Add positional encoding.
259 | 
260 |         Args:
261 |             x (torch.Tensor): Input tensor (batch, time, `*`).
262 | 
263 |         Returns:
264 |             torch.Tensor: Encoded tensor (batch, time, `*`).
265 | 
266 |         """
267 |         self.extend_pe(x)
268 |         x = x * self.xscale
269 |         pos_emb = self.position_encoding(size=x.size(1), offset=offset)
270 |         return self.dropout(x), self.dropout(pos_emb)
271 | 
272 |     def position_encoding(self,
273 |                           offset: Union[int, torch.Tensor],
274 |                           size: int) -> torch.Tensor:
275 |         """ For getting encoding in a streaming fashion
276 | 
277 |         Attention!!!!!
278 |         we apply dropout only once at the whole utterance level in a none
279 |         streaming way, but will call this function several times with
280 |         increasing input size in a streaming scenario, so the dropout will
281 |         be applied several times.
282 | 
283 |         Args:
284 |             offset (int or torch.tensor): start offset
285 |             size (int): required size of position encoding
286 | 
287 |         Returns:
288 |             torch.Tensor: Corresponding encoding
289 |         """
290 |         pos_emb = self.pe[
291 |             :,
292 |             self.pe.size(1) // 2 - size + 1: self.pe.size(1) // 2 + size,
293 |         ]
294 |         return pos_emb
295 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/encoder_layer.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2021 Mobvoi Inc (Binbin Zhang, Di Wu)
  2 | #               2022 Xingchen Song (sxc19@mails.tsinghua.edu.cn)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #   http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """Encoder self-attention layer definition."""
 17 | 
 18 | from typing import Optional, Tuple
 19 | 
 20 | import torch
 21 | from torch import nn
 22 | 
 23 | 
 24 | class TransformerEncoderLayer(nn.Module):
 25 |     """Encoder layer module.
 26 | 
 27 |     Args:
 28 |         size (int): Input dimension.
 29 |         self_attn (torch.nn.Module): Self-attention module instance.
 30 |             `MultiHeadedAttention` or `RelPositionMultiHeadedAttention`
 31 |             instance can be used as the argument.
 32 |         feed_forward (torch.nn.Module): Feed-forward module instance.
 33 |             `PositionwiseFeedForward`, instance can be used as the argument.
 34 |         dropout_rate (float): Dropout rate.
 35 |         normalize_before (bool):
 36 |             True: use layer_norm before each sub-block.
 37 |             False: to use layer_norm after each sub-block.
 38 |     """
 39 | 
 40 |     def __init__(
 41 |         self,
 42 |         size: int,
 43 |         self_attn: torch.nn.Module,
 44 |         feed_forward: torch.nn.Module,
 45 |         dropout_rate: float,
 46 |         normalize_before: bool = True,
 47 |     ):
 48 |         """Construct an EncoderLayer object."""
 49 |         super().__init__()
 50 |         self.self_attn = self_attn
 51 |         self.feed_forward = feed_forward
 52 |         self.norm1 = nn.LayerNorm(size, eps=1e-12)
 53 |         self.norm2 = nn.LayerNorm(size, eps=1e-12)
 54 |         self.dropout = nn.Dropout(dropout_rate)
 55 |         self.size = size
 56 |         self.normalize_before = normalize_before
 57 | 
 58 |     def forward(
 59 |         self,
 60 |         x: torch.Tensor,
 61 |         mask: torch.Tensor,
 62 |         pos_emb: torch.Tensor,
 63 |         mask_pad: torch.Tensor = torch.ones((0, 0, 0), dtype=torch.bool),
 64 |         att_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
 65 |         cnn_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
 66 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
 67 |         """Compute encoded features.
 68 | 
 69 |         Args:
 70 |             x (torch.Tensor): (#batch, time, size)
 71 |             mask (torch.Tensor): Mask tensor for the input (#batch, time，time),
 72 |                 (0, 0, 0) means fake mask.
 73 |             pos_emb (torch.Tensor): just for interface compatibility
 74 |                 to ConformerEncoderLayer
 75 |             mask_pad (torch.Tensor): does not used in transformer layer,
 76 |                 just for unified api with conformer.
 77 |             att_cache (torch.Tensor): Cache tensor of the KEY & VALUE
 78 |                 (#batch=1, head, cache_t1, d_k * 2), head * d_k == size.
 79 |             cnn_cache (torch.Tensor): Convolution cache in conformer layer
 80 |                 (#batch=1, size, cache_t2), not used here, it's for interface
 81 |                 compatibility to ConformerEncoderLayer.
 82 |         Returns:
 83 |             torch.Tensor: Output tensor (#batch, time, size).
 84 |             torch.Tensor: Mask tensor (#batch, time, time).
 85 |             torch.Tensor: att_cache tensor,
 86 |                 (#batch=1, head, cache_t1 + time, d_k * 2).
 87 |             torch.Tensor: cnn_cahce tensor (#batch=1, size, cache_t2).
 88 | 
 89 |         """
 90 |         residual = x
 91 |         if self.normalize_before:
 92 |             x = self.norm1(x)
 93 |         x_att, new_att_cache = self.self_attn(x, x, x, mask, pos_emb=pos_emb, cache=att_cache)
 94 |         x = residual + self.dropout(x_att)
 95 |         if not self.normalize_before:
 96 |             x = self.norm1(x)
 97 | 
 98 |         residual = x
 99 |         if self.normalize_before:
100 |             x = self.norm2(x)
101 |         x = residual + self.dropout(self.feed_forward(x))
102 |         if not self.normalize_before:
103 |             x = self.norm2(x)
104 | 
105 |         fake_cnn_cache = torch.zeros((0, 0, 0), dtype=x.dtype, device=x.device)
106 |         return x, mask, new_att_cache, fake_cnn_cache
107 | 
108 | 
109 | class ConformerEncoderLayer(nn.Module):
110 |     """Encoder layer module.
111 |     Args:
112 |         size (int): Input dimension.
113 |         self_attn (torch.nn.Module): Self-attention module instance.
114 |             `MultiHeadedAttention` or `RelPositionMultiHeadedAttention`
115 |             instance can be used as the argument.
116 |         feed_forward (torch.nn.Module): Feed-forward module instance.
117 |             `PositionwiseFeedForward` instance can be used as the argument.
118 |         feed_forward_macaron (torch.nn.Module): Additional feed-forward module
119 |              instance.
120 |             `PositionwiseFeedForward` instance can be used as the argument.
121 |         conv_module (torch.nn.Module): Convolution module instance.
122 |             `ConvlutionModule` instance can be used as the argument.
123 |         dropout_rate (float): Dropout rate.
124 |         normalize_before (bool):
125 |             True: use layer_norm before each sub-block.
126 |             False: use layer_norm after each sub-block.
127 |     """
128 | 
129 |     def __init__(
130 |         self,
131 |         size: int,
132 |         self_attn: torch.nn.Module,
133 |         feed_forward: Optional[nn.Module] = None,
134 |         feed_forward_macaron: Optional[nn.Module] = None,
135 |         conv_module: Optional[nn.Module] = None,
136 |         dropout_rate: float = 0.1,
137 |         normalize_before: bool = True,
138 |     ):
139 |         """Construct an EncoderLayer object."""
140 |         super().__init__()
141 |         self.self_attn = self_attn
142 |         self.feed_forward = feed_forward
143 |         self.feed_forward_macaron = feed_forward_macaron
144 |         self.conv_module = conv_module
145 |         self.norm_ff = nn.LayerNorm(size, eps=1e-12)  # for the FNN module
146 |         self.norm_mha = nn.LayerNorm(size, eps=1e-12)  # for the MHA module
147 |         if feed_forward_macaron is not None:
148 |             self.norm_ff_macaron = nn.LayerNorm(size, eps=1e-12)
149 |             self.ff_scale = 0.5
150 |         else:
151 |             self.ff_scale = 1.0
152 |         if self.conv_module is not None:
153 |             self.norm_conv = nn.LayerNorm(size, eps=1e-12)  # for the CNN module
154 |             self.norm_final = nn.LayerNorm(
155 |                 size, eps=1e-12)  # for the final output of the block
156 |         self.dropout = nn.Dropout(dropout_rate)
157 |         self.size = size
158 |         self.normalize_before = normalize_before
159 | 
160 |     def forward(
161 |         self,
162 |         x: torch.Tensor,
163 |         mask: torch.Tensor,
164 |         pos_emb: torch.Tensor,
165 |         mask_pad: torch.Tensor = torch.ones((0, 0, 0), dtype=torch.bool),
166 |         att_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
167 |         cnn_cache: torch.Tensor = torch.zeros((0, 0, 0, 0)),
168 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
169 |         """Compute encoded features.
170 | 
171 |         Args:
172 |             x (torch.Tensor): (#batch, time, size)
173 |             mask (torch.Tensor): Mask tensor for the input (#batch, time，time),
174 |                 (0, 0, 0) means fake mask.
175 |             pos_emb (torch.Tensor): positional encoding, must not be None
176 |                 for ConformerEncoderLayer.
177 |             mask_pad (torch.Tensor): batch padding mask used for conv module.
178 |                 (#batch, 1，time), (0, 0, 0) means fake mask.
179 |             att_cache (torch.Tensor): Cache tensor of the KEY & VALUE
180 |                 (#batch=1, head, cache_t1, d_k * 2), head * d_k == size.
181 |             cnn_cache (torch.Tensor): Convolution cache in conformer layer
182 |                 (#batch=1, size, cache_t2)
183 |         Returns:
184 |             torch.Tensor: Output tensor (#batch, time, size).
185 |             torch.Tensor: Mask tensor (#batch, time, time).
186 |             torch.Tensor: att_cache tensor,
187 |                 (#batch=1, head, cache_t1 + time, d_k * 2).
188 |             torch.Tensor: cnn_cahce tensor (#batch, size, cache_t2).
189 |         """
190 | 
191 |         # whether to use macaron style
192 |         if self.feed_forward_macaron is not None:
193 |             residual = x
194 |             if self.normalize_before:
195 |                 x = self.norm_ff_macaron(x)
196 |             x = residual + self.ff_scale * self.dropout(
197 |                 self.feed_forward_macaron(x))
198 |             if not self.normalize_before:
199 |                 x = self.norm_ff_macaron(x)
200 | 
201 |         # multi-headed self-attention module
202 |         residual = x
203 |         if self.normalize_before:
204 |             x = self.norm_mha(x)
205 |         x_att, new_att_cache = self.self_attn(x, x, x, mask, pos_emb,
206 |                                               att_cache)
207 |         x = residual + self.dropout(x_att)
208 |         if not self.normalize_before:
209 |             x = self.norm_mha(x)
210 | 
211 |         # convolution module
212 |         # Fake new cnn cache here, and then change it in conv_module
213 |         new_cnn_cache = torch.zeros((0, 0, 0), dtype=x.dtype, device=x.device)
214 |         if self.conv_module is not None:
215 |             residual = x
216 |             if self.normalize_before:
217 |                 x = self.norm_conv(x)
218 |             x, new_cnn_cache = self.conv_module(x, mask_pad, cnn_cache)
219 |             x = residual + self.dropout(x)
220 | 
221 |             if not self.normalize_before:
222 |                 x = self.norm_conv(x)
223 | 
224 |         # feed forward module
225 |         residual = x
226 |         if self.normalize_before:
227 |             x = self.norm_ff(x)
228 | 
229 |         x = residual + self.ff_scale * self.dropout(self.feed_forward(x))
230 |         if not self.normalize_before:
231 |             x = self.norm_ff(x)
232 | 
233 |         if self.conv_module is not None:
234 |             x = self.norm_final(x)
235 | 
236 |         return x, mask, new_att_cache, new_cnn_cache
237 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/positionwise_feed_forward.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2019 Shigeki Karita
  2 | #               2020 Mobvoi Inc (Binbin Zhang)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #   http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | """Positionwise feed forward layer definition."""
 16 | 
 17 | import torch
 18 | 
 19 | 
 20 | class PositionwiseFeedForward(torch.nn.Module):
 21 |     """Positionwise feed forward layer.
 22 | 
 23 |     FeedForward are appied on each position of the sequence.
 24 |     The output dim is same with the input dim.
 25 | 
 26 |     Args:
 27 |         idim (int): Input dimenstion.
 28 |         hidden_units (int): The number of hidden units.
 29 |         dropout_rate (float): Dropout rate.
 30 |         activation (torch.nn.Module): Activation function
 31 |     """
 32 | 
 33 |     def __init__(
 34 |             self,
 35 |             idim: int,
 36 |             hidden_units: int,
 37 |             dropout_rate: float,
 38 |             activation: torch.nn.Module = torch.nn.ReLU(),
 39 |     ):
 40 |         """Construct a PositionwiseFeedForward object."""
 41 |         super(PositionwiseFeedForward, self).__init__()
 42 |         self.w_1 = torch.nn.Linear(idim, hidden_units)
 43 |         self.activation = activation
 44 |         self.dropout = torch.nn.Dropout(dropout_rate)
 45 |         self.w_2 = torch.nn.Linear(hidden_units, idim)
 46 | 
 47 |     def forward(self, xs: torch.Tensor) -> torch.Tensor:
 48 |         """Forward function.
 49 | 
 50 |         Args:
 51 |             xs: input tensor (B, L, D)
 52 |         Returns:
 53 |             output tensor, (B, L, D)
 54 |         """
 55 |         return self.w_2(self.dropout(self.activation(self.w_1(xs))))
 56 | 
 57 | 
 58 | class MoEFFNLayer(torch.nn.Module):
 59 |     """
 60 |     Mixture of expert with Positionwise feed forward layer
 61 |     See also figure 1 in https://arxiv.org/pdf/2305.15663.pdf
 62 |     The output dim is same with the input dim.
 63 | 
 64 |     Modified from https://github.com/Lightning-AI/lit-gpt/pull/823
 65 |                   https://github.com/mistralai/mistral-src/blob/b46d6/moe_one_file_ref.py#L203-L219
 66 |     Args:
 67 |         n_expert: number of expert.
 68 |         n_expert_per_token: The actual number of experts used for each frame
 69 |         idim (int): Input dimenstion.
 70 |         hidden_units (int): The number of hidden units.
 71 |         dropout_rate (float): Dropout rate.
 72 |         activation (torch.nn.Module): Activation function
 73 |     """
 74 | 
 75 |     def __init__(
 76 |             self,
 77 |             n_expert: int,
 78 |             n_expert_per_token: int,
 79 |             idim: int,
 80 |             hidden_units: int,
 81 |             dropout_rate: float,
 82 |             activation: torch.nn.Module = torch.nn.ReLU(),
 83 |     ):
 84 |         super(MoEFFNLayer, self).__init__()
 85 |         self.gate = torch.nn.Linear(idim, n_expert, bias=False)
 86 |         self.experts = torch.nn.ModuleList(
 87 |             PositionwiseFeedForward(idim, hidden_units, dropout_rate,
 88 |                                     activation) for _ in range(n_expert))
 89 |         self.n_expert_per_token = n_expert_per_token
 90 | 
 91 |     def forward(self, xs: torch.Tensor) -> torch.Tensor:
 92 |         """Foward function.
 93 |         Args:
 94 |             xs: input tensor (B, L, D)
 95 |         Returns:
 96 |             output tensor, (B, L, D)
 97 | 
 98 |         """
 99 |         B, L, D = xs.size(
100 |         )  # batch size, sequence length, embedding dimension (idim)
101 |         xs = xs.view(-1, D)  # (B*L, D)
102 |         router = self.gate(xs)  # (B*L, n_expert)
103 |         logits, indices = torch.topk(
104 |             router, self.n_expert_per_token
105 |         )  # probs:(B*L, n_expert), indices: (B*L, n_expert)
106 |         weights = torch.nn.functional.softmax(
107 |             logits, dim=1,
108 |             dtype=torch.float).to(dtype=xs.dtype)  # (B*L, n_expert_per_token)
109 |         output = torch.zeros_like(xs)  # (B*L, D)
110 |         for i, expert in enumerate(self.experts):
111 |             mask = indices == i
112 |             batch_idx, ith_expert = torch.where(mask)
113 |             output[batch_idx] += weights[batch_idx, ith_expert, None] * expert(
114 |                 xs[batch_idx])
115 |         return output.view(B, L, D)
116 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/transformer/subsampling.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2021 Mobvoi Inc (Binbin Zhang, Di Wu)
  2 | #               2024 Alibaba Inc (Xiang Lyu)
  3 | #
  4 | # Licensed under the Apache License, Version 2.0 (the "License");
  5 | # you may not use this file except in compliance with the License.
  6 | # You may obtain a copy of the License at
  7 | #
  8 | #   http://www.apache.org/licenses/LICENSE-2.0
  9 | #
 10 | # Unless required by applicable law or agreed to in writing, software
 11 | # distributed under the License is distributed on an "AS IS" BASIS,
 12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 13 | # See the License for the specific language governing permissions and
 14 | # limitations under the License.
 15 | # Modified from ESPnet(https://github.com/espnet/espnet)
 16 | """Subsampling layer definition."""
 17 | 
 18 | from typing import Tuple, Union
 19 | 
 20 | import torch
 21 | 
 22 | 
 23 | class BaseSubsampling(torch.nn.Module):
 24 | 
 25 |     def __init__(self):
 26 |         super().__init__()
 27 |         self.right_context = 0
 28 |         self.subsampling_rate = 1
 29 | 
 30 |     def position_encoding(self, offset: Union[int, torch.Tensor],
 31 |                           size: int) -> torch.Tensor:
 32 |         return self.pos_enc.position_encoding(offset, size)
 33 | 
 34 | 
 35 | class EmbedinigNoSubsampling(BaseSubsampling):
 36 |     """Embedding input without subsampling
 37 |     """
 38 | 
 39 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
 40 |                  pos_enc_class: torch.nn.Module):
 41 |         super().__init__()
 42 |         self.embed = torch.nn.Embedding(idim, odim)
 43 |         self.pos_enc = pos_enc_class
 44 | 
 45 |     def forward(
 46 |         self,
 47 |         x: torch.Tensor,
 48 |         x_mask: torch.Tensor,
 49 |         offset: Union[int, torch.Tensor] = 0
 50 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
 51 |         """Input x.
 52 | 
 53 |         Args:
 54 |             x (torch.Tensor): Input tensor (#batch, time, idim).
 55 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
 56 | 
 57 |         Returns:
 58 |             torch.Tensor: linear input tensor (#batch, time', odim),
 59 |                 where time' = time .
 60 |             torch.Tensor: linear input mask (#batch, 1, time'),
 61 |                 where time' = time .
 62 | 
 63 |         """
 64 |         x = self.embed(x)
 65 |         x, pos_emb = self.pos_enc(x, offset)
 66 |         return x, pos_emb, x_mask
 67 | 
 68 | 
 69 | class LinearNoSubsampling(BaseSubsampling):
 70 |     """Linear transform the input without subsampling
 71 | 
 72 |     Args:
 73 |         idim (int): Input dimension.
 74 |         odim (int): Output dimension.
 75 |         dropout_rate (float): Dropout rate.
 76 | 
 77 |     """
 78 | 
 79 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
 80 |                  pos_enc_class: torch.nn.Module):
 81 |         """Construct an linear object."""
 82 |         super().__init__()
 83 |         self.out = torch.nn.Sequential(
 84 |             torch.nn.Linear(idim, odim),
 85 |             torch.nn.LayerNorm(odim, eps=1e-5),
 86 |             torch.nn.Dropout(dropout_rate),
 87 |         )
 88 |         self.pos_enc = pos_enc_class
 89 |         self.right_context = 0
 90 |         self.subsampling_rate = 1
 91 | 
 92 |     def forward(
 93 |         self,
 94 |         x: torch.Tensor,
 95 |         x_mask: torch.Tensor,
 96 |         offset: Union[int, torch.Tensor] = 0
 97 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
 98 |         """Input x.
 99 | 
100 |         Args:
101 |             x (torch.Tensor): Input tensor (#batch, time, idim).
102 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
103 | 
104 |         Returns:
105 |             torch.Tensor: linear input tensor (#batch, time', odim),
106 |                 where time' = time .
107 |             torch.Tensor: linear input mask (#batch, 1, time'),
108 |                 where time' = time .
109 | 
110 |         """
111 |         x = self.out(x)
112 |         x, pos_emb = self.pos_enc(x, offset)
113 |         return x, pos_emb, x_mask
114 | 
115 | 
116 | class Conv1dSubsampling2(BaseSubsampling):
117 |     """Convolutional 1D subsampling (to 1/2 length).
118 |        It is designed for Whisper, ref:
119 |        https://github.com/openai/whisper/blob/main/whisper/model.py
120 | 
121 |     Args:
122 |         idim (int): Input dimension.
123 |         odim (int): Output dimension.
124 |         dropout_rate (float): Dropout rate.
125 | 
126 |     """
127 | 
128 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
129 |                  pos_enc_class: torch.nn.Module):
130 |         """Construct an Conv1dSubsampling2 object."""
131 |         super().__init__()
132 |         self.conv = torch.nn.Sequential(
133 |             torch.nn.Conv1d(idim, odim, kernel_size=3, padding=1),
134 |             torch.nn.GELU(),
135 |             torch.nn.Conv1d(odim, odim, kernel_size=3, stride=2, padding=1),
136 |             torch.nn.GELU(),
137 |         )
138 |         self.pos_enc = pos_enc_class
139 |         # The right context for every conv layer is computed by:
140 |         # (kernel_size - 1) * frame_rate_of_this_layer
141 |         self.subsampling_rate = 2
142 |         # 4 = (3 - 1) * 1 + (3 - 1) * 1
143 |         self.right_context = 4
144 | 
145 |     def forward(
146 |         self,
147 |         x: torch.Tensor,
148 |         x_mask: torch.Tensor,
149 |         offset: Union[int, torch.Tensor] = 0
150 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
151 |         """Subsample x.
152 | 
153 |         Args:
154 |             x (torch.Tensor): Input tensor (#batch, time, idim).
155 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
156 | 
157 |         Returns:
158 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
159 |                 where time' = time // 2.
160 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
161 |                 where time' = time // 2.
162 |             torch.Tensor: positional encoding
163 | 
164 |         """
165 |         time = x.size(1)
166 |         x = x.transpose(1, 2)  # (b, f, t)
167 |         x = self.conv(x)
168 |         x = x.transpose(1, 2)  # (b, t, f)
169 |         x, pos_emb = self.pos_enc(x, offset)
170 |         return x, pos_emb, x_mask[:, :, (time + 1) % 2::2]
171 | 
172 | 
173 | class Conv2dSubsampling4(BaseSubsampling):
174 |     """Convolutional 2D subsampling (to 1/4 length).
175 | 
176 |     Args:
177 |         idim (int): Input dimension.
178 |         odim (int): Output dimension.
179 |         dropout_rate (float): Dropout rate.
180 | 
181 |     """
182 | 
183 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
184 |                  pos_enc_class: torch.nn.Module):
185 |         """Construct an Conv2dSubsampling4 object."""
186 |         super().__init__()
187 |         self.conv = torch.nn.Sequential(
188 |             torch.nn.Conv2d(1, odim, 3, 2),
189 |             torch.nn.ReLU(),
190 |             torch.nn.Conv2d(odim, odim, 3, 2),
191 |             torch.nn.ReLU(),
192 |         )
193 |         self.out = torch.nn.Sequential(
194 |             torch.nn.Linear(odim * (((idim - 1) // 2 - 1) // 2), odim))
195 |         self.pos_enc = pos_enc_class
196 |         # The right context for every conv layer is computed by:
197 |         # (kernel_size - 1) * frame_rate_of_this_layer
198 |         self.subsampling_rate = 4
199 |         # 6 = (3 - 1) * 1 + (3 - 1) * 2
200 |         self.right_context = 6
201 | 
202 |     def forward(
203 |         self,
204 |         x: torch.Tensor,
205 |         x_mask: torch.Tensor,
206 |         offset: Union[int, torch.Tensor] = 0
207 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
208 |         """Subsample x.
209 | 
210 |         Args:
211 |             x (torch.Tensor): Input tensor (#batch, time, idim).
212 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
213 | 
214 |         Returns:
215 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
216 |                 where time' = time // 4.
217 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
218 |                 where time' = time // 4.
219 |             torch.Tensor: positional encoding
220 | 
221 |         """
222 |         x = x.unsqueeze(1)  # (b, c=1, t, f)
223 |         x = self.conv(x)
224 |         b, c, t, f = x.size()
225 |         x = self.out(x.transpose(1, 2).contiguous().view(b, t, c * f))
226 |         x, pos_emb = self.pos_enc(x, offset)
227 |         return x, pos_emb, x_mask[:, :, 2::2][:, :, 2::2]
228 | 
229 | 
230 | class Conv2dSubsampling6(BaseSubsampling):
231 |     """Convolutional 2D subsampling (to 1/6 length).
232 |     Args:
233 |         idim (int): Input dimension.
234 |         odim (int): Output dimension.
235 |         dropout_rate (float): Dropout rate.
236 |         pos_enc (torch.nn.Module): Custom position encoding layer.
237 |     """
238 | 
239 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
240 |                  pos_enc_class: torch.nn.Module):
241 |         """Construct an Conv2dSubsampling6 object."""
242 |         super().__init__()
243 |         self.conv = torch.nn.Sequential(
244 |             torch.nn.Conv2d(1, odim, 3, 2),
245 |             torch.nn.ReLU(),
246 |             torch.nn.Conv2d(odim, odim, 5, 3),
247 |             torch.nn.ReLU(),
248 |         )
249 |         self.linear = torch.nn.Linear(odim * (((idim - 1) // 2 - 2) // 3),
250 |                                       odim)
251 |         self.pos_enc = pos_enc_class
252 |         # 10 = (3 - 1) * 1 + (5 - 1) * 2
253 |         self.subsampling_rate = 6
254 |         self.right_context = 10
255 | 
256 |     def forward(
257 |         self,
258 |         x: torch.Tensor,
259 |         x_mask: torch.Tensor,
260 |         offset: Union[int, torch.Tensor] = 0
261 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
262 |         """Subsample x.
263 |         Args:
264 |             x (torch.Tensor): Input tensor (#batch, time, idim).
265 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
266 | 
267 |         Returns:
268 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
269 |                 where time' = time // 6.
270 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
271 |                 where time' = time // 6.
272 |             torch.Tensor: positional encoding
273 |         """
274 |         x = x.unsqueeze(1)  # (b, c, t, f)
275 |         x = self.conv(x)
276 |         b, c, t, f = x.size()
277 |         x = self.linear(x.transpose(1, 2).contiguous().view(b, t, c * f))
278 |         x, pos_emb = self.pos_enc(x, offset)
279 |         return x, pos_emb, x_mask[:, :, 2::2][:, :, 4::3]
280 | 
281 | 
282 | class Conv2dSubsampling8(BaseSubsampling):
283 |     """Convolutional 2D subsampling (to 1/8 length).
284 | 
285 |     Args:
286 |         idim (int): Input dimension.
287 |         odim (int): Output dimension.
288 |         dropout_rate (float): Dropout rate.
289 | 
290 |     """
291 | 
292 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
293 |                  pos_enc_class: torch.nn.Module):
294 |         """Construct an Conv2dSubsampling8 object."""
295 |         super().__init__()
296 |         self.conv = torch.nn.Sequential(
297 |             torch.nn.Conv2d(1, odim, 3, 2),
298 |             torch.nn.ReLU(),
299 |             torch.nn.Conv2d(odim, odim, 3, 2),
300 |             torch.nn.ReLU(),
301 |             torch.nn.Conv2d(odim, odim, 3, 2),
302 |             torch.nn.ReLU(),
303 |         )
304 |         self.linear = torch.nn.Linear(
305 |             odim * ((((idim - 1) // 2 - 1) // 2 - 1) // 2), odim)
306 |         self.pos_enc = pos_enc_class
307 |         self.subsampling_rate = 8
308 |         # 14 = (3 - 1) * 1 + (3 - 1) * 2 + (3 - 1) * 4
309 |         self.right_context = 14
310 | 
311 |     def forward(
312 |         self,
313 |         x: torch.Tensor,
314 |         x_mask: torch.Tensor,
315 |         offset: Union[int, torch.Tensor] = 0
316 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
317 |         """Subsample x.
318 | 
319 |         Args:
320 |             x (torch.Tensor): Input tensor (#batch, time, idim).
321 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
322 | 
323 |         Returns:
324 |             torch.Tensor: Subsampled tensor (#batch, time', odim),
325 |                 where time' = time // 8.
326 |             torch.Tensor: Subsampled mask (#batch, 1, time'),
327 |                 where time' = time // 8.
328 |             torch.Tensor: positional encoding
329 |         """
330 |         x = x.unsqueeze(1)  # (b, c, t, f)
331 |         x = self.conv(x)
332 |         b, c, t, f = x.size()
333 |         x = self.linear(x.transpose(1, 2).contiguous().view(b, t, c * f))
334 |         x, pos_emb = self.pos_enc(x, offset)
335 |         return x, pos_emb, x_mask[:, :, 2::2][:, :, 2::2][:, :, 2::2]
336 | 
337 | 
338 | class LegacyLinearNoSubsampling(BaseSubsampling):
339 |     """Linear transform the input without subsampling
340 | 
341 |     Args:
342 |         idim (int): Input dimension.
343 |         odim (int): Output dimension.
344 |         dropout_rate (float): Dropout rate.
345 | 
346 |     """
347 | 
348 |     def __init__(self, idim: int, odim: int, dropout_rate: float,
349 |                  pos_enc_class: torch.nn.Module):
350 |         """Construct an linear object."""
351 |         super().__init__()
352 |         self.out = torch.nn.Sequential(
353 |             torch.nn.Linear(idim, odim),
354 |             torch.nn.LayerNorm(odim, eps=1e-5),
355 |             torch.nn.Dropout(dropout_rate),
356 |             torch.nn.ReLU(),
357 |         )
358 |         self.pos_enc = pos_enc_class
359 |         self.right_context = 0
360 |         self.subsampling_rate = 1
361 | 
362 |     def forward(
363 |         self,
364 |         x: torch.Tensor,
365 |         x_mask: torch.Tensor,
366 |         offset: Union[int, torch.Tensor] = 0
367 |     ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
368 |         """Input x.
369 | 
370 |         Args:
371 |             x (torch.Tensor): Input tensor (#batch, time, idim).
372 |             x_mask (torch.Tensor): Input mask (#batch, 1, time).
373 | 
374 |         Returns:
375 |             torch.Tensor: linear input tensor (#batch, time', odim),
376 |                 where time' = time .
377 |             torch.Tensor: linear input mask (#batch, 1, time'),
378 |                 where time' = time .
379 | 
380 |         """
381 |         x = self.out(x)
382 |         x, pos_emb = self.pos_enc(x, offset)
383 |         return x, pos_emb, x_mask
384 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/utils/class_utils.py:
--------------------------------------------------------------------------------
 1 | # Copyright [2023-11-28] <sxc19@mails.tsinghua.edu.cn, Xingchen Song>
 2 | #            2024 Alibaba Inc (authors: Xiang Lyu)
 3 | #
 4 | # Licensed under the Apache License, Version 2.0 (the "License");
 5 | # you may not use this file except in compliance with the License.
 6 | # You may obtain a copy of the License at
 7 | #
 8 | #     http://www.apache.org/licenses/LICENSE-2.0
 9 | #
10 | # Unless required by applicable law or agreed to in writing, software
11 | # distributed under the License is distributed on an "AS IS" BASIS,
12 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
13 | # See the License for the specific language governing permissions and
14 | # limitations under the License.
15 | import torch
16 | 
17 | from ..transformer.activation import Swish
18 | from ..transformer.subsampling import (
19 |     LinearNoSubsampling,
20 |     EmbedinigNoSubsampling,
21 |     Conv1dSubsampling2,
22 |     Conv2dSubsampling4,
23 |     Conv2dSubsampling6,
24 |     Conv2dSubsampling8,
25 | )
26 | from ..transformer.embedding import (
27 |     PositionalEncoding,
28 |     RelPositionalEncoding,
29 |     WhisperPositionalEncoding,
30 |     LearnablePositionalEncoding,
31 |     NoPositionalEncoding)
32 | from ..transformer.attention import (MultiHeadedAttention,
33 |     RelPositionMultiHeadedAttention)
34 | from ..transformer.embedding import EspnetRelPositionalEncoding
35 | from ..transformer.subsampling import LegacyLinearNoSubsampling
36 | 
37 | 
38 | COSYVOICE_ACTIVATION_CLASSES = {
39 |     "hardtanh": torch.nn.Hardtanh,
40 |     "tanh": torch.nn.Tanh,
41 |     "relu": torch.nn.ReLU,
42 |     "selu": torch.nn.SELU,
43 |     "swish": getattr(torch.nn, "SiLU", Swish),
44 |     "gelu": torch.nn.GELU,
45 | }
46 | 
47 | COSYVOICE_SUBSAMPLE_CLASSES = {
48 |     "linear": LinearNoSubsampling,
49 |     "linear_legacy": LegacyLinearNoSubsampling,
50 |     "embed": EmbedinigNoSubsampling,
51 |     "conv1d2": Conv1dSubsampling2,
52 |     "conv2d": Conv2dSubsampling4,
53 |     "conv2d6": Conv2dSubsampling6,
54 |     "conv2d8": Conv2dSubsampling8,
55 |     'paraformer_dummy': torch.nn.Identity
56 | }
57 | 
58 | COSYVOICE_EMB_CLASSES = {
59 |     "embed": PositionalEncoding,
60 |     "abs_pos": PositionalEncoding,
61 |     "rel_pos": RelPositionalEncoding,
62 |     "rel_pos_espnet": EspnetRelPositionalEncoding,
63 |     "no_pos": NoPositionalEncoding,
64 |     "abs_pos_whisper": WhisperPositionalEncoding,
65 |     "embed_learnable_pe": LearnablePositionalEncoding,
66 | }
67 | 
68 | COSYVOICE_ATTENTION_CLASSES = {
69 |     "selfattn": MultiHeadedAttention,
70 |     "rel_selfattn": RelPositionMultiHeadedAttention,
71 | }
72 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/utils/mask.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2019 Shigeki Karita
  2 | #               2020 Mobvoi Inc (Binbin Zhang)
  3 | #               2024 Alibaba Inc (authors: Xiang Lyu)
  4 | #
  5 | # Licensed under the Apache License, Version 2.0 (the "License");
  6 | # you may not use this file except in compliance with the License.
  7 | # You may obtain a copy of the License at
  8 | #
  9 | #   http://www.apache.org/licenses/LICENSE-2.0
 10 | #
 11 | # Unless required by applicable law or agreed to in writing, software
 12 | # distributed under the License is distributed on an "AS IS" BASIS,
 13 | # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 14 | # See the License for the specific language governing permissions and
 15 | # limitations under the License.
 16 | 
 17 | import torch
 18 | 
 19 | '''
 20 | def subsequent_mask(
 21 |         size: int,
 22 |         device: torch.device = torch.device("cpu"),
 23 | ) -> torch.Tensor:
 24 |     """Create mask for subsequent steps (size, size).
 25 | 
 26 |     This mask is used only in decoder which works in an auto-regressive mode.
 27 |     This means the current step could only do attention with its left steps.
 28 | 
 29 |     In encoder, fully attention is used when streaming is not necessary and
 30 |     the sequence is not long. In this  case, no attention mask is needed.
 31 | 
 32 |     When streaming is need, chunk-based attention is used in encoder. See
 33 |     subsequent_chunk_mask for the chunk-based attention mask.
 34 | 
 35 |     Args:
 36 |         size (int): size of mask
 37 |         str device (str): "cpu" or "cuda" or torch.Tensor.device
 38 |         dtype (torch.device): result dtype
 39 | 
 40 |     Returns:
 41 |         torch.Tensor: mask
 42 | 
 43 |     Examples:
 44 |         >>> subsequent_mask(3)
 45 |         [[1, 0, 0],
 46 |          [1, 1, 0],
 47 |          [1, 1, 1]]
 48 |     """
 49 |     ret = torch.ones(size, size, device=device, dtype=torch.bool)
 50 |     return torch.tril(ret)
 51 | '''
 52 | 
 53 | 
 54 | def subsequent_chunk_mask(
 55 |         size: int,
 56 |         chunk_size: int,
 57 |         num_left_chunks: int = -1,
 58 |         device: torch.device = torch.device("cpu"),
 59 | ) -> torch.Tensor:
 60 |     """Create mask for subsequent steps (size, size) with chunk size,
 61 |        this is for streaming encoder
 62 | 
 63 |     Args:
 64 |         size (int): size of mask
 65 |         chunk_size (int): size of chunk
 66 |         num_left_chunks (int): number of left chunks
 67 |             <0: use full chunk
 68 |             >=0: use num_left_chunks
 69 |         device (torch.device): "cpu" or "cuda" or torch.Tensor.device
 70 | 
 71 |     Returns:
 72 |         torch.Tensor: mask
 73 | 
 74 |     Examples:
 75 |         >>> subsequent_chunk_mask(4, 2)
 76 |         [[1, 1, 0, 0],
 77 |          [1, 1, 0, 0],
 78 |          [1, 1, 1, 1],
 79 |          [1, 1, 1, 1]]
 80 |     """
 81 |     # NOTE this modified implementation meets onnx export requirements, but it doesn't support num_left_chunks
 82 |     # actually this is not needed after we have inference cache implemented, will remove it later
 83 |     pos_idx = torch.arange(size, device=device)
 84 |     block_value = (torch.div(pos_idx, chunk_size, rounding_mode='trunc') + 1) * chunk_size
 85 |     ret = pos_idx.unsqueeze(0) < block_value.unsqueeze(1)
 86 |     return ret
 87 | 
 88 | 
 89 | def add_optional_chunk_mask(xs: torch.Tensor,
 90 |                             masks: torch.Tensor,
 91 |                             use_dynamic_chunk: bool,
 92 |                             use_dynamic_left_chunk: bool,
 93 |                             decoding_chunk_size: int,
 94 |                             static_chunk_size: int,
 95 |                             num_decoding_left_chunks: int,
 96 |                             enable_full_context: bool = True):
 97 |     """ Apply optional mask for encoder.
 98 | 
 99 |     Args:
100 |         xs (torch.Tensor): padded input, (B, L, D), L for max length
101 |         mask (torch.Tensor): mask for xs, (B, 1, L)
102 |         use_dynamic_chunk (bool): whether to use dynamic chunk or not
103 |         use_dynamic_left_chunk (bool): whether to use dynamic left chunk for
104 |             training.
105 |         decoding_chunk_size (int): decoding chunk size for dynamic chunk, it's
106 |             0: default for training, use random dynamic chunk.
107 |             <0: for decoding, use full chunk.
108 |             >0: for decoding, use fixed chunk size as set.
109 |         static_chunk_size (int): chunk size for static chunk training/decoding
110 |             if it's greater than 0, if use_dynamic_chunk is true,
111 |             this parameter will be ignored
112 |         num_decoding_left_chunks: number of left chunks, this is for decoding,
113 |             the chunk size is decoding_chunk_size.
114 |             >=0: use num_decoding_left_chunks
115 |             <0: use all left chunks
116 |         enable_full_context (bool):
117 |             True: chunk size is either [1, 25] or full context(max_len)
118 |             False: chunk size ~ U[1, 25]
119 | 
120 |     Returns:
121 |         torch.Tensor: chunk mask of the input xs.
122 |     """
123 |     # Whether to use chunk mask or not
124 |     if use_dynamic_chunk:
125 |         max_len = xs.size(1)
126 |         if decoding_chunk_size < 0:
127 |             chunk_size = max_len
128 |             num_left_chunks = -1
129 |         elif decoding_chunk_size > 0:
130 |             chunk_size = decoding_chunk_size
131 |             num_left_chunks = num_decoding_left_chunks
132 |         else:
133 |             # chunk size is either [1, 25] or full context(max_len).
134 |             # Since we use 4 times subsampling and allow up to 1s(100 frames)
135 |             # delay, the maximum frame is 100 / 4 = 25.
136 |             chunk_size = torch.randint(1, max_len, (1, )).item()
137 |             num_left_chunks = -1
138 |             if chunk_size > max_len // 2 and enable_full_context:
139 |                 chunk_size = max_len
140 |             else:
141 |                 chunk_size = chunk_size % 25 + 1
142 |                 if use_dynamic_left_chunk:
143 |                     max_left_chunks = (max_len - 1) // chunk_size
144 |                     num_left_chunks = torch.randint(0, max_left_chunks,
145 |                                                     (1, )).item()
146 |         chunk_masks = subsequent_chunk_mask(xs.size(1), chunk_size,
147 |                                             num_left_chunks,
148 |                                             xs.device)  # (L, L)
149 |         chunk_masks = chunk_masks.unsqueeze(0)  # (1, L, L)
150 |         chunk_masks = masks & chunk_masks  # (B, L, L)
151 |     elif static_chunk_size > 0:
152 |         num_left_chunks = num_decoding_left_chunks
153 |         chunk_masks = subsequent_chunk_mask(xs.size(1), static_chunk_size,
154 |                                             num_left_chunks,
155 |                                             xs.device)  # (L, L)
156 |         chunk_masks = chunk_masks.unsqueeze(0)  # (1, L, L)
157 |         chunk_masks = masks & chunk_masks  # (B, L, L)
158 |     else:
159 |         chunk_masks = masks
160 |     assert chunk_masks.dtype == torch.bool
161 |     if (chunk_masks.sum(dim=-1) == 0).sum().item() != 0:
162 |         logging.warning('get chunk_masks all false at some timestep, force set to true, make sure they are masked in futuer computation!')
163 |         chunk_masks[chunk_masks.sum(dim=-1)==0] = True
164 |     return chunk_masks
165 | 
166 | 
167 | def make_pad_mask(lengths: torch.Tensor, max_len: int = 0) -> torch.Tensor:
168 |     """Make mask tensor containing indices of padded part.
169 | 
170 |     See description of make_non_pad_mask.
171 | 
172 |     Args:
173 |         lengths (torch.Tensor): Batch of lengths (B,).
174 |     Returns:
175 |         torch.Tensor: Mask tensor containing indices of padded part.
176 | 
177 |     Examples:
178 |         >>> lengths = [5, 3, 2]
179 |         >>> make_pad_mask(lengths)
180 |         masks = [[0, 0, 0, 0 ,0],
181 |                  [0, 0, 0, 1, 1],
182 |                  [0, 0, 1, 1, 1]]
183 |     """
184 |     batch_size = lengths.size(0)
185 |     max_len = max_len if max_len > 0 else lengths.max().item()
186 |     seq_range = torch.arange(0,
187 |                              max_len,
188 |                              dtype=torch.int64,
189 |                              device=lengths.device)
190 |     seq_range_expand = seq_range.unsqueeze(0).expand(batch_size, max_len)
191 |     seq_length_expand = lengths.unsqueeze(-1)
192 |     mask = seq_range_expand >= seq_length_expand
193 |     return mask
194 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3gen/utils/mel.py:
--------------------------------------------------------------------------------
 1 | """mel-spectrogram extraction in Matcha-TTS"""
 2 | from librosa.filters import mel as librosa_mel_fn
 3 | import torch
 4 | import numpy as np
 5 | 
 6 | 
 7 | # NOTE: they decalred these global vars
 8 | mel_basis = {}
 9 | hann_window = {}
10 | 
11 | 
12 | def dynamic_range_compression_torch(x, C=1, clip_val=1e-5):
13 |     return torch.log(torch.clamp(x, min=clip_val) * C)
14 | 
15 | 
16 | def spectral_normalize_torch(magnitudes):
17 |     output = dynamic_range_compression_torch(magnitudes)
18 |     return output
19 | 
20 | """
21 | feat_extractor: !name:matcha.utils.audio.mel_spectrogram
22 |     n_fft: 1920
23 |     num_mels: 80
24 |     sampling_rate: 24000
25 |     hop_size: 480
26 |     win_size: 1920
27 |     fmin: 0
28 |     fmax: 8000
29 |     center: False
30 | 
31 | """
32 | 
33 | def mel_spectrogram(y, n_fft=1920, num_mels=80, sampling_rate=24000, hop_size=480, win_size=1920,
34 |                     fmin=0, fmax=8000, center=False):
35 |     """Copied from https://github.com/shivammehta25/Matcha-TTS/blob/main/matcha/utils/audio.py
36 |     Set default values according to Cosyvoice's config.
37 |     """
38 | 
39 |     if isinstance(y, np.ndarray):
40 |         y = torch.tensor(y).float()
41 | 
42 |     if len(y.shape) == 1:
43 |         y = y[None, ]
44 | 
45 |     if torch.min(y) < -1.0:
46 |         print("min value is ", torch.min(y))
47 |     if torch.max(y) > 1.0:
48 |         print("max value is ", torch.max(y))
49 | 
50 |     global mel_basis, hann_window  # pylint: disable=global-statement,global-variable-not-assigned
51 |     if f"{str(fmax)}_{str(y.device)}" not in mel_basis:
52 |         mel = librosa_mel_fn(sr=sampling_rate, n_fft=n_fft, n_mels=num_mels, fmin=fmin, fmax=fmax)
53 |         mel_basis[str(fmax) + "_" + str(y.device)] = torch.from_numpy(mel).float().to(y.device)
54 |         hann_window[str(y.device)] = torch.hann_window(win_size).to(y.device)
55 | 
56 |     y = torch.nn.functional.pad(
57 |         y.unsqueeze(1), (int((n_fft - hop_size) / 2), int((n_fft - hop_size) / 2)), mode="reflect"
58 |     )
59 |     y = y.squeeze(1)
60 | 
61 |     spec = torch.view_as_real(
62 |         torch.stft(
63 |             y,
64 |             n_fft,
65 |             hop_length=hop_size,
66 |             win_length=win_size,
67 |             window=hann_window[str(y.device)],
68 |             center=center,
69 |             pad_mode="reflect",
70 |             normalized=False,
71 |             onesided=True,
72 |             return_complex=True,
73 |         )
74 |     )
75 | 
76 |     spec = torch.sqrt(spec.pow(2).sum(-1) + (1e-9))
77 | 
78 |     spec = torch.matmul(mel_basis[str(fmax) + "_" + str(y.device)], spec)
79 |     spec = spectral_normalize_torch(spec)
80 | 
81 |     return spec
82 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3tokenizer/__init__.py:
--------------------------------------------------------------------------------
 1 | from .s3tokenizer import (
 2 |     S3_SR,
 3 |     S3_HOP,
 4 |     S3_TOKEN_HOP,
 5 |     S3_TOKEN_RATE,
 6 |     SPEECH_VOCAB_SIZE,
 7 |     S3Tokenizer,
 8 | )
 9 | 
10 | 
11 | SOS = SPEECH_VOCAB_SIZE
12 | EOS = SPEECH_VOCAB_SIZE + 1
13 | 
14 | 
15 | 
16 | def drop_invalid_tokens(x):
17 |     """Drop SoS and EoS"""
18 |     assert len(x.shape) == 1 or (len(x.shape) == 2 and x.shape[0] == 1), "only batch size of one allowed for now"
19 |     if SOS in x:
20 |         s = (x == SOS).nonzero(as_tuple=True)[0].squeeze(0) + 1
21 |     else:
22 |         s = 0
23 | 
24 |     if EOS in x:
25 |         e = (x == EOS).nonzero(as_tuple=True)[0].squeeze(0)
26 |     else:
27 |         e = None
28 | 
29 |     x = x[s: e]
30 |     return x
31 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/s3tokenizer/s3tokenizer.py:
--------------------------------------------------------------------------------
  1 | from typing import List, Tuple
  2 | 
  3 | import numpy as np
  4 | import librosa
  5 | import torch
  6 | import torch.nn.functional as F
  7 | from s3tokenizer.utils import padding
  8 | from s3tokenizer.model_v2 import (
  9 |     S3TokenizerV2,
 10 |     ModelConfig,
 11 | )
 12 | 
 13 | 
 14 | # Sampling rate of the inputs to S3TokenizerV2
 15 | S3_SR = 16_000
 16 | S3_HOP = 160  # 100 frames/sec
 17 | S3_TOKEN_HOP = 640  # 25 tokens/sec
 18 | S3_TOKEN_RATE = 25
 19 | SPEECH_VOCAB_SIZE = 6561
 20 | 
 21 | 
 22 | class S3Tokenizer(S3TokenizerV2):
 23 |     """
 24 |     s3tokenizer.S3TokenizerV2 with the following changes:
 25 |     - a more integrated `forward`
 26 |     - compute `log_mel_spectrogram` using `_mel_filters` and `window` in `register_buffers`
 27 |     """
 28 | 
 29 |     ignore_state_dict_missing = ("_mel_filters", "window")
 30 | 
 31 |     def __init__(
 32 |         self,
 33 |         name: str="speech_tokenizer_v2_25hz",
 34 |         config: ModelConfig = ModelConfig()
 35 |     ):
 36 |         super().__init__(name)
 37 | 
 38 |         self.n_fft = 400
 39 |         _mel_filters = librosa.filters.mel(
 40 |             sr=S3_SR,
 41 |             n_fft=self.n_fft,
 42 |             n_mels=config.n_mels
 43 |         )
 44 |         self.register_buffer(
 45 |             "_mel_filters",
 46 |             torch.FloatTensor(_mel_filters),
 47 |         )
 48 | 
 49 |         self.register_buffer(
 50 |             "window",
 51 |             torch.hann_window(self.n_fft),
 52 |         )
 53 | 
 54 |     def pad(self, wavs, sr) -> List[torch.Tensor]:
 55 |         """
 56 |         Given a list of wavs with the same `sample_rate`, pad them so that the length is multiple of 40ms (S3 runs at 25 token/sec).
 57 |         """
 58 |         processed_wavs = []
 59 |         for wav in wavs:
 60 |             if isinstance(wav, np.ndarray):
 61 |                 wav = torch.from_numpy(wav)
 62 |             if wav.dim() == 1:
 63 |                 wav = wav.unsqueeze(0)
 64 | 
 65 |             n_tokens = (wav.shape[1] / sr) * S3_TOKEN_RATE
 66 |             n_tokens = np.ceil(n_tokens)
 67 |             intended_wav_len = n_tokens * (sr / S3_TOKEN_RATE)
 68 |             intended_wav_len = int(intended_wav_len)
 69 |             wav = torch.nn.functional.pad(
 70 |                 wav,
 71 |                 (0, intended_wav_len - wav.shape[-1]),
 72 |                 mode="constant",
 73 |                 value=0
 74 |             )
 75 |             processed_wavs.append(wav)
 76 |         return processed_wavs
 77 | 
 78 |     def _prepare_audio(self, wavs):
 79 |         """Prepare a list of audios for s3tokenizer processing."""
 80 |         processed_wavs = []
 81 |         for wav in wavs:
 82 |             if isinstance(wav, np.ndarray):
 83 |                 wav = torch.from_numpy(wav)
 84 |             if wav.dim() == 1:
 85 |                 wav = wav.unsqueeze(0)
 86 | 
 87 |             processed_wavs.append(wav)
 88 |         return processed_wavs
 89 | 
 90 |     @torch.no_grad()
 91 |     def forward(
 92 |         self,
 93 |         wavs: torch.Tensor,
 94 |         accelerator: 'Accelerator'=None,
 95 |         max_len: int=None,
 96 |     ) -> Tuple[torch.Tensor, torch.LongTensor]:
 97 |         """
 98 |         NOTE: mel-spec has a hop size of 160 points (100 frame/sec).
 99 |         FIXME: this class inherits `nn.Module` but doesn't accept `torch.Tensor` and handles a list of wavs one by one, which is unexpected.
100 | 
101 |         Args
102 |         ----
103 |         - `wavs`: 16 kHz speech audio
104 |         - `max_len` max length to truncate the output sequence to (25 token/sec).
105 |         NOTE: please pad the waveform if longer sequence is needed.
106 |         """
107 |         processed_wavs = self._prepare_audio(wavs)
108 |         mels, mel_lens = [], []
109 |         for wav in processed_wavs:
110 |             wav = wav.to(self.device)
111 |             mel = self.log_mel_spectrogram(wav)  # [B=1, F, T]
112 |             if max_len is not None:
113 |                 mel = mel[..., :max_len * 4]  # num_mel_frames = 4 * num_tokens
114 |             mels.append(mel.squeeze(0))
115 | 
116 |         mels, mel_lens = padding(mels)
117 |         if accelerator is None:
118 |             tokenizer = self
119 |         else:
120 |             tokenizer = accelerator.unwrap_model(self)
121 | 
122 |         speech_tokens, speech_token_lens = tokenizer.quantize(mels, mel_lens.to(self.device))
123 |         return (
124 |             speech_tokens.long().detach(),
125 |             speech_token_lens.long().detach(),
126 |         )
127 | 
128 |     def log_mel_spectrogram(
129 |         self,
130 |         audio: torch.Tensor,
131 |         padding: int = 0,
132 |     ):
133 |         """
134 |         Compute the log-Mel spectrogram of
135 | 
136 |         Parameters
137 |         ----------
138 |         audio: torch.Tensor, shape = (*)
139 |             The path to audio or either a NumPy array or Tensor containing the
140 |             audio waveform in 16 kHz
141 | 
142 |         padding: int
143 |             Number of zero samples to pad to the right
144 | 
145 |         Returns
146 |         -------
147 |         torch.Tensor, shape = (128, n_frames)
148 |             A Tensor that contains the Mel spectrogram
149 |         """
150 |         if not torch.is_tensor(audio):
151 |             audio = torch.from_numpy(audio)
152 | 
153 |         audio = audio.to(self.device)
154 |         if padding > 0:
155 |             audio = F.pad(audio, (0, padding))
156 |         stft = torch.stft(
157 |             audio, self.n_fft, S3_HOP,
158 |             window=self.window.to(self.device),
159 |             return_complex=True
160 |         )
161 |         magnitudes = stft[..., :-1].abs()**2
162 | 
163 |         mel_spec = self._mel_filters.to(self.device) @ magnitudes
164 | 
165 |         log_spec = torch.clamp(mel_spec, min=1e-10).log10()
166 |         log_spec = torch.maximum(log_spec, log_spec.max() - 8.0)
167 |         log_spec = (log_spec + 4.0) / 4.0
168 |         return log_spec
169 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/__init__.py:
--------------------------------------------------------------------------------
1 | from .t3 import T3
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/inference/alignment_stream_analyzer.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2025 Resemble AI
  2 | # Author: John Meade, Jeremy Hsu
  3 | # MIT License
  4 | import logging
  5 | import torch
  6 | from dataclasses import dataclass
  7 | from types import MethodType
  8 | 
  9 | 
 10 | logger = logging.getLogger(__name__)
 11 | 
 12 | 
 13 | @dataclass
 14 | class AlignmentAnalysisResult:
 15 |     # was this frame detected as being part of a noisy beginning chunk with potential hallucinations?
 16 |     false_start: bool
 17 |     # was this frame detected as being part of a long tail with potential hallucinations?
 18 |     long_tail: bool
 19 |     # was this frame detected as repeating existing text content?
 20 |     repetition: bool
 21 |     # was the alignment position of this frame too far from the previous frame?
 22 |     discontinuity: bool
 23 |     # has inference reached the end of the text tokens? eg, this remains false if inference stops early
 24 |     complete: bool
 25 |     # approximate position in the text token sequence. Can be used for generating online timestamps.
 26 |     position: int
 27 | 
 28 | 
 29 | class AlignmentStreamAnalyzer:
 30 |     def __init__(self, tfmr, queue, text_tokens_slice, alignment_layer_idx=9, eos_idx=0):
 31 |         """
 32 |         Some transformer TTS models implicitly solve text-speech alignment in one or more of their self-attention
 33 |         activation maps. This module exploits this to perform online integrity checks which streaming.
 34 |         A hook is injected into the specified attention layer, and heuristics are used to determine alignment
 35 |         position, repetition, etc.
 36 | 
 37 |         NOTE: currently requires no queues.
 38 |         """
 39 |         # self.queue = queue
 40 |         self.text_tokens_slice = (i, j) = text_tokens_slice
 41 |         self.eos_idx = eos_idx
 42 |         self.alignment = torch.zeros(0, j-i)
 43 |         # self.alignment_bin = torch.zeros(0, j-i)
 44 |         self.curr_frame_pos = 0
 45 |         self.text_position = 0
 46 | 
 47 |         self.started = False
 48 |         self.started_at = None
 49 | 
 50 |         self.complete = False
 51 |         self.completed_at = None
 52 | 
 53 |         # Using `output_attentions=True` is incompatible with optimized attention kernels, so
 54 |         # using it for all layers slows things down too much. We can apply it to just one layer
 55 |         # by intercepting the kwargs and adding a forward hook (credit: jrm)
 56 |         self.last_aligned_attn = None
 57 |         self._add_attention_spy(tfmr, alignment_layer_idx)
 58 | 
 59 |     def _add_attention_spy(self, tfmr, alignment_layer_idx):
 60 |         """
 61 |         Adds a forward hook to a specific attention layer to collect outputs.
 62 |         Using `output_attentions=True` is incompatible with optimized attention kernels, so
 63 |         using it for all layers slows things down too much.
 64 |         (credit: jrm)
 65 |         """
 66 | 
 67 |         def attention_forward_hook(module, input, output):
 68 |             """
 69 |             See `LlamaAttention.forward`; the output is a 3-tuple: `attn_output, attn_weights, past_key_value`.
 70 |             NOTE:
 71 |             - When `output_attentions=True`, `LlamaSdpaAttention.forward` calls `LlamaAttention.forward`.
 72 |             - `attn_output` has shape [B, H, T0, T0] for the 0th entry, and [B, H, 1, T0+i] for the rest i-th.
 73 |             """
 74 |             step_attention = output[1].cpu() # (B, 16, N, N)
 75 |             self.last_aligned_attn = step_attention[0].mean(0) # (N, N)
 76 | 
 77 |         target_layer = tfmr.layers[alignment_layer_idx].self_attn
 78 |         hook_handle = target_layer.register_forward_hook(attention_forward_hook)
 79 | 
 80 |         # Backup original forward
 81 |         original_forward = target_layer.forward
 82 |         def patched_forward(self, *args, **kwargs):
 83 |             kwargs['output_attentions'] = True
 84 |             return original_forward(*args, **kwargs)
 85 | 
 86 |         # TODO: how to unpatch it?
 87 |         target_layer.forward = MethodType(patched_forward, target_layer)
 88 | 
 89 |     def step(self, logits):
 90 |         """
 91 |         Emits an AlignmentAnalysisResult into the output queue, and potentially modifies the logits to force an EOS.
 92 |         """
 93 |         # extract approximate alignment matrix chunk (1 frame at a time after the first chunk)
 94 |         aligned_attn = self.last_aligned_attn # (N, N)
 95 |         i, j = self.text_tokens_slice
 96 |         if self.curr_frame_pos == 0:
 97 |             # first chunk has conditioning info, text tokens, and BOS token
 98 |             A_chunk = aligned_attn[j:, i:j].clone().cpu() # (T, S)
 99 |         else:
100 |             # subsequent chunks have 1 frame due to KV-caching
101 |             A_chunk = aligned_attn[:, i:j].clone().cpu() # (1, S)
102 | 
103 |         # TODO: monotonic masking; could have issue b/c spaces are often skipped.
104 |         A_chunk[:, self.curr_frame_pos + 1:] = 0
105 | 
106 | 
107 |         self.alignment = torch.cat((self.alignment, A_chunk), dim=0)
108 | 
109 |         A = self.alignment
110 |         T, S = A.shape
111 | 
112 |         # update position
113 |         cur_text_posn = A_chunk[-1].argmax()
114 |         discontinuity = not(-4 < cur_text_posn - self.text_position < 7) # NOTE: very lenient!
115 |         if not discontinuity:
116 |             self.text_position = cur_text_posn
117 | 
118 |         # Hallucinations at the start of speech show up as activations at the bottom of the attention maps!
119 |         # To mitigate this, we just wait until there are no activations far off-diagonal in the last 2 tokens,
120 |         # and there are some strong activations in the first few tokens.
121 |         false_start = (not self.started) and (A[-2:, -2:].max() > 0.1 or A[:, :4].max() < 0.5)
122 |         self.started = not false_start
123 |         if self.started and self.started_at is None:
124 |             self.started_at = T
125 | 
126 |         # Is generation likely complete?
127 |         self.complete = self.complete or self.text_position >= S - 3
128 |         if self.complete and self.completed_at is None:
129 |             self.completed_at = T
130 | 
131 |         # NOTE: EOS rarely assigned activations, and second-last token is often punctuation, so use last 3 tokens.
132 |         # NOTE: due to the false-start behaviour, we need to make sure we skip activations for the first few tokens.
133 |         last_text_token_duration = A[15:, -3:].sum()
134 | 
135 |         # Activations for the final token that last too long are likely hallucinations.
136 |         long_tail = self.complete and (A[self.completed_at:, -3:].sum(dim=0).max() >= 10) # 400ms
137 | 
138 |         # If there are activations in previous tokens after generation has completed, assume this is a repetition error.
139 |         repetition = self.complete and (A[self.completed_at:, :-5].max(dim=1).values.sum() > 5)
140 | 
141 |         # If a bad ending is detected, force emit EOS by modifying logits
142 |         # NOTE: this means logits may be inconsistent with latents!
143 |         if long_tail or repetition:
144 |             logger.warn(f"forcing EOS token, {long_tail=}, {repetition=}")
145 |             # (±2**15 is safe for all dtypes >= 16bit)
146 |             logits = -(2**15) * torch.ones_like(logits)
147 |             logits[..., self.eos_idx] = 2**15
148 | 
149 |         # Suppress EoS to prevent early termination
150 |         if cur_text_posn < S - 3: # FIXME: arbitrary
151 |             logits[..., self.eos_idx] = -2**15
152 | 
153 |         self.curr_frame_pos += 1
154 |         return logits
155 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/inference/t3_hf_backend.py:
--------------------------------------------------------------------------------
  1 | from typing import Optional
  2 | 
  3 | import torch
  4 | from torch import nn as nn
  5 | from transformers import LlamaConfig, LlamaModel, LlamaPreTrainedModel, GenerationMixin
  6 | from transformers.modeling_outputs import CausalLMOutputWithCrossAttentions
  7 | 
  8 | 
  9 | class T3HuggingfaceBackend(LlamaPreTrainedModel, GenerationMixin):
 10 |     """
 11 |     Override some HuggingFace interface methods so we can use the standard `generate` method with our
 12 |     custom embedding / logit layers.
 13 | 
 14 |     NOTE: need to extend "*PreTrainedModel" to avoid re-initializing weights!
 15 |     """
 16 | 
 17 |     def __init__(
 18 |         self,
 19 |         config: LlamaConfig,
 20 |         llama: LlamaModel,
 21 |         *,
 22 |         speech_enc,
 23 |         speech_head,
 24 |         latents_queue=None,
 25 |         logits_queue=None,
 26 |         alignment_stream_analyzer: 'AlignmentStreamAnalyzer'=None,
 27 |     ):
 28 |         super().__init__(config)
 29 |         self.model = llama
 30 |         self.speech_enc = speech_enc
 31 |         self.speech_head = speech_head
 32 |         self._added_cond = False
 33 |         self.alignment_stream_analyzer = alignment_stream_analyzer
 34 | 
 35 |     @torch.inference_mode()
 36 |     def prepare_inputs_for_generation(
 37 |         self, input_ids: torch.Tensor, decoder_cond: torch.Tensor, use_cache: bool, past_key_values=None,
 38 |         # This argument was introduced in some recent version of transformers (>=4.29.1)
 39 |         cache_position=None
 40 |     ):
 41 |         """
 42 |         This is a method used by huggingface's generate() method.
 43 |         Overridden here to apply our custom speech token embedding layer.
 44 | 
 45 |         :param input_ids: (B, S) int64 tensors of input tokens.
 46 |         :param decoder_cond: (B, T, C) float32 tensor of conditioning (prefixed to <input_embeds>)
 47 |         """
 48 | 
 49 |         # Make use of the kv cache: only the last input ID is new, we trim away all the ones before
 50 |         if not use_cache:
 51 |             past_key_values = None
 52 |         if past_key_values is not None:
 53 |             input_ids = input_ids[:, -1:]
 54 | 
 55 |         # custom speech token embedding layer
 56 |         inputs_embeds = self.speech_enc(input_ids)
 57 | 
 58 |         # prefix decoder conditioning if applicable
 59 |         if not self._added_cond:
 60 |             assert past_key_values is not None # should be first step
 61 |             if decoder_cond.size(0) != inputs_embeds.size(0):
 62 |                 decoder_cond = decoder_cond.expand(inputs_embeds.size(0), -1, -1)
 63 |             inputs_embeds = torch.cat([decoder_cond, inputs_embeds], dim=1)
 64 |             self._added_cond = True
 65 | 
 66 |         return {
 67 |             "inputs_embeds": inputs_embeds,
 68 |             "past_key_values": past_key_values,
 69 |             "use_cache": use_cache,
 70 |         }
 71 | 
 72 |     @torch.inference_mode()
 73 |     def forward(
 74 |         self,
 75 |         inputs_embeds: torch.Tensor,
 76 |         past_key_values: Optional[torch.Tensor]=None,
 77 |         use_cache=True,
 78 |         output_attentions=False,
 79 |         output_hidden_states=True,
 80 |         return_dict=True,
 81 |     ):
 82 |         """
 83 |         This is a method used by huggingface's generate() method.
 84 |         Overridden here to apply our custom layer norm and speech logit projection layers.
 85 | 
 86 |         :param inputs_embeds: (B, S, C) float32 tensor of conditioning inputs. If past key values are given,
 87 |         S should be 1.
 88 |         """
 89 |         is_large_input = inputs_embeds.size(1) != 1
 90 |         has_cache = past_key_values is not None and len(past_key_values) > 0
 91 |         assert not (is_large_input and has_cache)
 92 |         assert return_dict
 93 |         assert output_hidden_states
 94 | 
 95 |         tfmr_out = self.model(
 96 |             inputs_embeds=inputs_embeds,
 97 |             past_key_values=past_key_values,
 98 |             use_cache=use_cache,
 99 |             output_attentions=output_attentions,
100 |             output_hidden_states=output_hidden_states,
101 |             return_dict=True,
102 |         )
103 |         hidden_states = tfmr_out.hidden_states[-1]  # (B, seq, dim)
104 | 
105 |         logits = self.speech_head(hidden_states)
106 |         # assert inputs_embeds.size(0) == 1 # (disabled for CFG)
107 | 
108 |         # NOTE: hallucination handler may modify logits to force emit an EOS token
109 |         # logits = self.alignment_stream_analyzer.step(logits)
110 | 
111 |         return CausalLMOutputWithCrossAttentions(
112 |             logits=logits,
113 |             past_key_values=tfmr_out.past_key_values,
114 |             hidden_states=tfmr_out.hidden_states,
115 |             attentions=tfmr_out.attentions,
116 |         )
117 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/llama_configs.py:
--------------------------------------------------------------------------------
 1 | LLAMA_520M_CONFIG_DICT = dict(
 2 |     # Arbitrary small number that won't cause problems when loading.
 3 |     # These param are unused due to custom input layers.
 4 |     vocab_size=8,
 5 |     # default params needed for loading most pretrained 1B weights
 6 |     max_position_embeddings=131072,
 7 |     hidden_size=1024,
 8 |     intermediate_size=4096,
 9 |     num_hidden_layers=30,
10 |     num_attention_heads=16,
11 |     attn_implementation="sdpa",
12 |     head_dim=64,
13 |     tie_word_embeddings=False,
14 |     hidden_act="silu",
15 |     attention_bias=False,
16 |     attention_dropout=0.0,
17 |     initializer_range=0.02,
18 |     mlp_bias=False,
19 |     model_type="llama",
20 |     num_key_value_heads=16,
21 |     pretraining_tp=1,
22 |     rms_norm_eps=1e-05,
23 |     rope_scaling=dict(
24 |         factor=8.0,
25 |         high_freq_factor=4.0,
26 |         low_freq_factor=1.0,
27 |         original_max_position_embeddings=8192,
28 |         rope_type="llama3"
29 |     ),
30 |     rope_theta=500000.0,
31 |     torch_dtype="bfloat16",
32 |     use_cache=True,
33 | )
34 | 
35 | LLAMA_CONFIGS = {
36 |     "Llama_520M": LLAMA_520M_CONFIG_DICT,
37 | }
38 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/cond_enc.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass
 2 | from typing import Optional
 3 | 
 4 | import torch
 5 | from torch import nn, Tensor
 6 | 
 7 | from .perceiver import Perceiver
 8 | from .t3_config import T3Config
 9 | 
10 | 
11 | @dataclass
12 | class T3Cond:
13 |     """
14 |     Dataclass container for most / all conditioning info.
15 |     TODO: serialization methods aren't used, keeping them around for convenience
16 |     """
17 | 
18 |     speaker_emb: Tensor
19 |     clap_emb: Optional[Tensor] = None
20 |     cond_prompt_speech_tokens: Optional[Tensor] = None
21 |     cond_prompt_speech_emb: Optional[Tensor] = None
22 |     emotion_adv: Optional[Tensor] = 0.5
23 | 
24 |     def to(self, *, device=None, dtype=None):
25 |         "Cast to a device and dtype. Dtype casting is ignored for long/int tensors."
26 |         for k, v in self.__dict__.items():
27 |             if torch.is_tensor(v):
28 |                 is_fp = type(v.view(-1)[0].item()) is not int
29 |                 setattr(self, k, v.to(device=device, dtype=dtype if is_fp else None))
30 |         return self
31 | 
32 |     def save(self, fpath):
33 |         torch.save(self.__dict__, fpath)
34 | 
35 |     @staticmethod
36 |     def load(fpath, map_location="cpu"):
37 |         kwargs = torch.load(fpath, map_location=map_location, weights_only=True)
38 |         return T3Cond(**kwargs)
39 | 
40 | 
41 | class T3CondEnc(nn.Module):
42 |     """
43 |     Handle all non-text conditioning, like speaker embeddings / prompts, CLAP, emotion, etc.
44 |     """
45 | 
46 |     def __init__(self, hp: T3Config):
47 |         super().__init__()
48 |         self.hp = hp
49 |         if hp.encoder_type == "voice_encoder":
50 |             self.spkr_enc = nn.Linear(hp.speaker_embed_size, hp.n_channels)
51 |         else:
52 |             raise NotImplementedError(str(hp.encoder_type))
53 | 
54 |         # emotion adv
55 |         self.emotion_adv_fc = None
56 |         if hp.emotion_adv:
57 |             self.emotion_adv_fc = nn.Linear(1, hp.n_channels, bias=False)
58 | 
59 |         # perceiver resampler
60 |         self.perceiver = None
61 |         if hp.use_perceiver_resampler:
62 |             self.perceiver = Perceiver()
63 | 
64 |     def forward(self, cond: T3Cond):
65 |         # Validate
66 |         assert (cond.cond_prompt_speech_tokens is None) == (cond.cond_prompt_speech_emb is None), \
67 |             "no embeddings for cond_prompt_speech_tokens"
68 | 
69 |         # Speaker embedding projection
70 |         cond_spkr = self.spkr_enc(cond.speaker_emb.view(-1, self.hp.speaker_embed_size))[:, None]  # (B, 1, dim)
71 |         empty = torch.zeros_like(cond_spkr[:, :0])  # (B, 0, dim)
72 | 
73 |         # TODO CLAP
74 |         assert cond.clap_emb is None, "clap_embed not implemented"
75 |         cond_clap = empty  # (B, 0, dim)
76 | 
77 |         # Cond prompt
78 |         cond_prompt_speech_emb = cond.cond_prompt_speech_emb
79 |         if cond_prompt_speech_emb is None:
80 |             cond_prompt_speech_emb = empty  # (B, 0, dim)
81 |         elif self.hp.use_perceiver_resampler:
82 |             cond_prompt_speech_emb = self.perceiver(cond_prompt_speech_emb)
83 | 
84 |         # Emotion Adv: must provide a value if this model uses emotion conditioning
85 |         cond_emotion_adv = empty  # (B, 0, dim)
86 |         if self.hp.emotion_adv:
87 |             assert cond.emotion_adv is not None
88 |             cond_emotion_adv = self.emotion_adv_fc(cond.emotion_adv.view(-1, 1, 1))
89 | 
90 |         # Concat and return
91 |         cond_embeds = torch.cat((
92 |             cond_spkr,
93 |             cond_clap,
94 |             cond_prompt_speech_emb,
95 |             cond_emotion_adv,
96 |         ), dim=1)
97 |         return cond_embeds
98 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/learned_pos_emb.py:
--------------------------------------------------------------------------------
 1 | from typing import Union
 2 | 
 3 | import torch
 4 | from torch import nn, Tensor
 5 | 
 6 | 
 7 | class LearnedPositionEmbeddings(nn.Module):
 8 |     def __init__(self, seq_len, model_dim, init=.02):
 9 |         super().__init__()
10 |         self.emb = nn.Embedding(seq_len, model_dim)
11 |         # Initializing this way is standard for GPT-2
12 |         self.emb.weight.data.normal_(mean=0.0, std=init)
13 | 
14 |     def forward(self, x):
15 |         """
16 |         Returns positional embeddings for index 0 up to the length of x
17 |         """
18 |         sl = x.shape[1]
19 |         return self.emb(torch.arange(0, sl, device=x.device))
20 | 
21 |     def get_fixed_embedding(self, idx: 'Union[int, Tensor]'):
22 |         """
23 |         Args:
24 |             idx: scalar int or an integer tensor of shape (T,) or (B, T)
25 |         Returns:
26 |             positional embeddings for given indices, shape (B, T, dim), ie (1, 1, dim) for int input
27 |         """
28 |         device = self.emb.weight.device
29 |         idx = idx.to(device) if torch.is_tensor(idx) else torch.tensor(idx, device=device)
30 |         idx = torch.atleast_2d(idx)
31 |         assert idx.ndim == 2
32 |         return self.emb(idx)  # (B, T, dim)
33 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/perceiver.py:
--------------------------------------------------------------------------------
  1 | # Copyright (c) 2025 Resemble AI
  2 | # Author: Manmay Nakhashi
  3 | # MIT License
  4 | import math
  5 | 
  6 | import torch
  7 | from torch import nn
  8 | import torch.nn.functional as F
  9 | from einops import rearrange
 10 | 
 11 | 
 12 | class RelativePositionBias(nn.Module):
 13 |     def __init__(self, scale, causal=False, num_buckets=32, max_distance=128, heads=8):
 14 |         super().__init__()
 15 |         self.scale = scale
 16 |         self.causal = causal
 17 |         self.num_buckets = num_buckets
 18 |         self.max_distance = max_distance
 19 |         self.relative_attention_bias = nn.Embedding(num_buckets, heads)
 20 | 
 21 |     @staticmethod
 22 |     def _relative_position_bucket(relative_position, causal=True, num_buckets=32, max_distance=128):
 23 |         ret = 0
 24 |         n = -relative_position
 25 |         if not causal:
 26 |             num_buckets //= 2
 27 |             ret += (n < 0).long() * num_buckets
 28 |             n = torch.abs(n)
 29 |         else:
 30 |             n = torch.max(n, torch.zeros_like(n))
 31 | 
 32 |         max_exact = num_buckets // 2
 33 |         is_small = n < max_exact
 34 | 
 35 |         val_if_large = max_exact + (
 36 |                 torch.log(n.float() / max_exact) / math.log(max_distance / max_exact) * (num_buckets - max_exact)
 37 |         ).long()
 38 |         val_if_large = torch.min(val_if_large, torch.full_like(val_if_large, num_buckets - 1))
 39 | 
 40 |         ret += torch.where(is_small, n, val_if_large)
 41 |         return ret
 42 | 
 43 |     def forward(self, qk_dots):
 44 |         i, j, device = *qk_dots.shape[-2:], qk_dots.device
 45 |         q_pos = torch.arange(i, dtype=torch.long, device=device)
 46 |         k_pos = torch.arange(j, dtype=torch.long, device=device)
 47 |         rel_pos = k_pos[None, :] - q_pos[:, None]
 48 |         rp_bucket = self._relative_position_bucket(rel_pos, causal=self.causal, num_buckets=self.num_buckets,
 49 |                                                    max_distance=self.max_distance)
 50 |         values = self.relative_attention_bias(rp_bucket)
 51 |         bias = rearrange(values, 'i j h -> () h i j')
 52 |         return qk_dots + (bias * self.scale)
 53 | 
 54 | 
 55 | class AttentionQKV(nn.Module):
 56 |     def __init__(self, n_heads, head_dim, dropout_rate=0.1, scale=None, flash=False):
 57 |         super().__init__()
 58 |         self.n_heads = n_heads
 59 |         self.head_dim = head_dim
 60 |         self.scale = scale if scale is not None else head_dim ** -0.5
 61 |         self.flash = flash
 62 |         self.dropout_rate = dropout_rate
 63 |         self.dropout = nn.Dropout(dropout_rate)
 64 |         self.flash_config = self.setup_flash_config() if flash else None
 65 | 
 66 |     def setup_flash_config(self):
 67 |         # Setup flash attention configuration
 68 |         flash_config = {
 69 |             'enable_flash': True,
 70 |             'enable_math': True,
 71 |             'enable_mem_efficient': True
 72 |         }
 73 |         return flash_config
 74 | 
 75 |     def forward(self, q, k, v, mask=None):
 76 |         q, k, v = [self.split_heads(tensor) for tensor in [q, k, v]]
 77 |         if self.flash:
 78 |             out = self.flash_attention(q, k, v, mask=mask)
 79 |         else:
 80 |             out = self.scaled_dot_product_attention(q, k, v, mask=mask)
 81 | 
 82 |         return self.combine_heads(out)
 83 | 
 84 |     def scaled_dot_product_attention(self, q, k, v, mask=None):
 85 |         sim = torch.einsum("bhlt,bhls->bhts", q, k) * self.scale
 86 |         if mask is not None:
 87 |             sim = sim.masked_fill(mask == 0, float('-inf'))
 88 |         attn = torch.softmax(sim, dim=-1)
 89 |         attn = self.dropout(attn)
 90 |         return torch.einsum("bhts,bhls->bhlt", attn, v)
 91 | 
 92 |     def flash_attention(self, q, k, v, mask=None):
 93 |         config = self.flash_config if self.flash_config else {}
 94 |         with torch.backends.cuda.sdp_kernel(**config):
 95 |             out = F.scaled_dot_product_attention(
 96 |                 q, k, v,
 97 |                 attn_mask=mask,
 98 |                 dropout_p=self.dropout_rate if self.training else 0.
 99 |             )
100 |         return out
101 | 
102 |     def split_heads(self, x):
103 |         bs, length, _ = x.shape
104 |         x = x.view(bs, length, self.n_heads, self.head_dim)
105 |         return x.permute(0, 2, 1, 3)
106 | 
107 |     def combine_heads(self, x):
108 |         bs, _, length, _ = x.shape
109 |         x = x.permute(0, 2, 1, 3).contiguous()
110 |         return x.view(bs, length, -1)
111 | 
112 | 
113 | class AttentionBlock2(nn.Module):
114 |     """
115 |     An attention block that allows spatial positions to attend to each other,
116 |     using AttentionQKV and separate linear transformations for Q, K, and V.
117 |     """
118 | 
119 |     def __init__(
120 |         self,
121 |         channels,
122 |         num_heads=1,
123 |         num_head_channels=-1,
124 |         relative_pos_embeddings=False,
125 |         flash_attention=True,
126 |         dropout_rate=0.2,
127 |         scale=None
128 |     ):
129 |         super().__init__()
130 |         self.channels = channels
131 | 
132 |         if num_head_channels == -1:
133 |             self.num_heads = num_heads
134 |         else:
135 |             assert (
136 |                 channels % num_head_channels == 0
137 |             ), f"channels {channels} is not divisible by num_head_channels {num_head_channels}"
138 |             self.num_heads = channels // num_head_channels
139 | 
140 |         self.norm = nn.LayerNorm(channels)
141 | 
142 |         # Separate linear layers for Q, K, and V
143 |         self.to_q = nn.Linear(channels, channels)
144 |         self.to_k = nn.Linear(channels, channels)
145 |         self.to_v = nn.Linear(channels, channels)
146 | 
147 |         self.attention = AttentionQKV(self.num_heads, channels // self.num_heads, dropout_rate=dropout_rate, flash=flash_attention, scale=scale)
148 | 
149 |         self.proj_out = nn.Linear(channels, channels)
150 | 
151 |         if relative_pos_embeddings:
152 |             self.relative_pos_embeddings = RelativePositionBias(scale=(channels // self.num_heads) ** .5, causal=False, heads=num_heads, num_buckets=32, max_distance=64)
153 |         else:
154 |             self.relative_pos_embeddings = None
155 | 
156 |     def forward(self, x1, x2, mask=None):
157 |         b1, c1, *spatial1 = x1.shape
158 |         b2, c2, *spatial2 = x2.shape
159 | 
160 |         x1_norm = self.norm(x1)
161 |         x2_norm = self.norm(x2)
162 | 
163 |         q = self.to_q(x1_norm)
164 |         k = self.to_k(x2_norm)
165 |         v = self.to_v(x2_norm)
166 | 
167 |         h = self.attention(q, k, v, mask=mask)
168 |         h = self.proj_out(h)
169 | 
170 |         return (x1 + h).reshape(b1, c1, *spatial1)
171 | 
172 | 
173 | class Perceiver(nn.Module):
174 |     """Inspired by https://arxiv.org/abs/2103.03206"""
175 |     def __init__(self, pre_attention_query_token=32, pre_attention_query_size=1024, embedding_dim=1024, num_attn_heads=4):
176 |         """
177 |         Initialize the perceiver module.
178 | 
179 |         :param pre_attention_query_token: Number of query tokens for pre-attention
180 |         :param pre_attention_query_size: Size of each query token
181 |         :param embedding_dim: Dimension of the embedding space
182 |         :param num_attn_heads: Number of attention heads
183 |         """
184 |         super().__init__()
185 | 
186 |         # Initialize the pre-attention query parameter
187 |         self.pre_attention_query = torch.nn.Parameter(
188 |             torch.empty(1, pre_attention_query_token, pre_attention_query_size)
189 |         )
190 | 
191 |         # Calculate the variance for uniform initialization
192 |         query_variance = math.sqrt(3.0) * math.sqrt(2.0 / (pre_attention_query_token + pre_attention_query_token))
193 | 
194 |         # Initialize the pre-attention query with uniform distribution
195 |         self.pre_attention_query.data.uniform_(-query_variance, query_variance)
196 | 
197 |         # Initialize the attention block
198 |         self.attn = AttentionBlock2(embedding_dim, num_attn_heads)
199 | 
200 |     def forward(self, h):
201 |         """
202 |         Forward pass of the perceiver module.
203 |         :param h: Input tensor
204 |         :return: Output after applying attention mechanisms
205 |         """
206 |         # Expand the pre-attention query to match the batch size of the input
207 |         query_ = self.pre_attention_query.expand(h.shape[0], -1, -1)
208 |         # Apply the first attention mechanism (cross-attention)
209 |         pre_att = self.attn(query_, h)
210 |         # Apply the second attention mechanism (self-attention)
211 |         attn = self.attn(pre_att, pre_att)
212 |         return attn
213 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/t3/modules/t3_config.py:
--------------------------------------------------------------------------------
 1 | from ..llama_configs import LLAMA_CONFIGS
 2 | 
 3 | 
 4 | class T3Config:
 5 |     start_text_token = 255
 6 |     stop_text_token = 0
 7 |     text_tokens_dict_size = 704
 8 |     max_text_tokens = 2048
 9 | 
10 |     start_speech_token = 6561
11 |     stop_speech_token = 6562
12 |     speech_tokens_dict_size = 8194
13 |     max_speech_tokens = 4096
14 | 
15 |     llama_config_name = "Llama_520M"
16 |     input_pos_emb = "learned"
17 |     speech_cond_prompt_len = 150
18 | 
19 |     # For T3CondEnc
20 |     encoder_type = "voice_encoder"
21 |     speaker_embed_size = 256
22 |     use_perceiver_resampler = True
23 |     emotion_adv = True
24 | 
25 |     @property
26 |     def n_channels(self):
27 |         return LLAMA_CONFIGS[self.llama_config_name]["hidden_size"]
28 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/tokenizers/__init__.py:
--------------------------------------------------------------------------------
1 | from .tokenizer import EnTokenizer
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/tokenizers/tokenizer.py:
--------------------------------------------------------------------------------
 1 | import logging
 2 | 
 3 | import torch
 4 | from tokenizers import Tokenizer
 5 | 
 6 | 
 7 | # Special tokens
 8 | SOT = "[START]"
 9 | EOT = "[STOP]"
10 | UNK = "[UNK]"
11 | SPACE = "[SPACE]"
12 | SPECIAL_TOKENS = [SOT, EOT, UNK, SPACE, "[PAD]", "[SEP]", "[CLS]", "[MASK]"]
13 | 
14 | logger = logging.getLogger(__name__)
15 | 
16 | class EnTokenizer:
17 |     def __init__(self, vocab_file_path):
18 |         self.tokenizer: Tokenizer = Tokenizer.from_file(vocab_file_path)
19 |         self.check_vocabset_sot_eot()
20 | 
21 |     def check_vocabset_sot_eot(self):
22 |         voc = self.tokenizer.get_vocab()
23 |         assert SOT in voc
24 |         assert EOT in voc
25 | 
26 |     def text_to_tokens(self, text: str):
27 |         text_tokens = self.encode(text)
28 |         text_tokens = torch.IntTensor(text_tokens).unsqueeze(0)
29 |         return text_tokens
30 | 
31 |     def encode( self, txt: str, verbose=False):
32 |         """
33 |         clean_text > (append `lang_id`) > replace SPACE > encode text using Tokenizer
34 |         """
35 |         txt = txt.replace(' ', SPACE)
36 |         code = self.tokenizer.encode(txt)
37 |         ids = code.ids
38 |         return ids
39 | 
40 |     def decode(self, seq):
41 |         if isinstance(seq, torch.Tensor):
42 |             seq = seq.cpu().numpy()
43 | 
44 |         txt: str = self.tokenizer.decode(seq,
45 |         skip_special_tokens=False)
46 |         txt = txt.replace(' ', '')
47 |         txt = txt.replace(SPACE, ' ')
48 |         txt = txt.replace(EOT, '')
49 |         txt = txt.replace(UNK, '')
50 |         return txt
51 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/utils.py:
--------------------------------------------------------------------------------
1 | class AttrDict(dict):
2 |     def __init__(self, *args, **kwargs):
3 |         super(AttrDict, self).__init__(*args, **kwargs)
4 |         self.__dict__ = self
5 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/__init__.py:
--------------------------------------------------------------------------------
1 | from .voice_encoder import VoiceEncoder, VoiceEncConfig
2 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/config.py:
--------------------------------------------------------------------------------
 1 | class VoiceEncConfig:
 2 |     num_mels = 40
 3 |     sample_rate = 16000
 4 |     speaker_embed_size = 256
 5 |     ve_hidden_size = 256
 6 |     flatten_lstm_params = False
 7 |     n_fft = 400
 8 |     hop_size = 160
 9 |     win_size = 400
10 |     fmax = 8000
11 |     fmin = 0
12 |     preemphasis = 0.
13 |     mel_power = 2.0
14 |     mel_type = "amp"
15 |     normalized_mels = False
16 |     ve_partial_frames = 160
17 |     ve_final_relu = True
18 |     stft_magnitude_min = 1e-4
19 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/melspec.py:
--------------------------------------------------------------------------------
 1 | from functools import lru_cache
 2 | 
 3 | from scipy import signal
 4 | import numpy as np
 5 | import librosa
 6 | 
 7 | 
 8 | @lru_cache()
 9 | def mel_basis(hp):
10 |     assert hp.fmax <= hp.sample_rate // 2
11 |     return librosa.filters.mel(
12 |         sr=hp.sample_rate,
13 |         n_fft=hp.n_fft,
14 |         n_mels=hp.num_mels,
15 |         fmin=hp.fmin,
16 |         fmax=hp.fmax)  # -> (nmel, nfreq)
17 | 
18 | 
19 | def preemphasis(wav, hp):
20 |     assert hp.preemphasis != 0
21 |     wav = signal.lfilter([1, -hp.preemphasis], [1], wav)
22 |     wav = np.clip(wav, -1, 1)
23 |     return wav
24 | 
25 | 
26 | def melspectrogram(wav, hp, pad=True):
27 |     # Run through pre-emphasis
28 |     if hp.preemphasis > 0:
29 |         wav = preemphasis(wav, hp)
30 |         assert np.abs(wav).max() - 1 < 1e-07
31 | 
32 |     # Do the stft
33 |     spec_complex = _stft(wav, hp, pad=pad)
34 | 
35 |     # Get the magnitudes
36 |     spec_magnitudes = np.abs(spec_complex)
37 | 
38 |     if hp.mel_power != 1.0:
39 |         spec_magnitudes **= hp.mel_power
40 | 
41 |     # Get the mel and convert magnitudes->db
42 |     mel = np.dot(mel_basis(hp), spec_magnitudes)
43 |     if hp.mel_type == "db":
44 |         mel = _amp_to_db(mel, hp)
45 | 
46 |     # Normalise the mel from db to 0,1
47 |     if hp.normalized_mels:
48 |         mel = _normalize(mel, hp).astype(np.float32)
49 | 
50 |     assert not pad or mel.shape[1] == 1 + len(wav) // hp.hop_size   # Sanity check
51 |     return mel   # (M, T)
52 | 
53 | 
54 | def _stft(y, hp, pad=True):
55 |     # NOTE: after 0.8, pad mode defaults to constant, setting this to reflect for
56 |     #   historical consistency and streaming-version consistency
57 |     return librosa.stft(
58 |         y,
59 |         n_fft=hp.n_fft,
60 |         hop_length=hp.hop_size,
61 |         win_length=hp.win_size,
62 |         center=pad,
63 |         pad_mode="reflect",
64 |     )
65 | 
66 | 
67 | def _amp_to_db(x, hp):
68 |     return 20 * np.log10(np.maximum(hp.stft_magnitude_min, x))
69 | 
70 | 
71 | def _db_to_amp(x):
72 |     return np.power(10.0, x * 0.05)
73 | 
74 | 
75 | def _normalize(s, hp, headroom_db=15):
76 |     min_level_db = 20 * np.log10(hp.stft_magnitude_min)
77 |     s = (s - min_level_db) / (-min_level_db + headroom_db)
78 |     return s
79 | 


--------------------------------------------------------------------------------
/src/chatterbox/models/voice_encoder/voice_encoder.py:
--------------------------------------------------------------------------------
  1 | # Adapted from https://github.com/CorentinJ/Real-Time-Voice-Cloning
  2 | # MIT License
  3 | from typing import List, Union, Optional
  4 | 
  5 | import numpy as np
  6 | from numpy.lib.stride_tricks import as_strided
  7 | import librosa
  8 | import torch
  9 | import torch.nn.functional as F
 10 | from torch import nn, Tensor
 11 | 
 12 | from .config import VoiceEncConfig
 13 | from .melspec import melspectrogram
 14 | 
 15 | 
 16 | def pack(arrays, seq_len: int=None, pad_value=0):
 17 |     """
 18 |     Given a list of length B of array-like objects of shapes (Ti, ...), packs them in a single tensor of
 19 |     shape (B, T, ...) by padding each individual array on the right.
 20 | 
 21 |     :param arrays: a list of array-like objects of matching shapes except for the first axis.
 22 |     :param seq_len: the value of T. It must be the maximum of the lengths Ti of the arrays at
 23 |     minimum. Will default to that value if None.
 24 |     :param pad_value: the value to pad the arrays with.
 25 |     :return: a (B, T, ...) tensor
 26 |     """
 27 |     if seq_len is None:
 28 |         seq_len = max(len(array) for array in arrays)
 29 |     else:
 30 |         assert seq_len >= max(len(array) for array in arrays)
 31 | 
 32 |     # Convert lists to np.array
 33 |     if isinstance(arrays[0], list):
 34 |         arrays = [np.array(array) for array in arrays]
 35 | 
 36 |     # Convert to tensor and handle device
 37 |     device = None
 38 |     if isinstance(arrays[0], torch.Tensor):
 39 |         tensors = arrays
 40 |         device = tensors[0].device
 41 |     else:
 42 |         tensors = [torch.as_tensor(array) for array in arrays]
 43 | 
 44 |     # Fill the packed tensor with the array data
 45 |     packed_shape = (len(tensors), seq_len, *tensors[0].shape[1:])
 46 |     packed_tensor = torch.full(packed_shape, pad_value, dtype=tensors[0].dtype, device=device)
 47 | 
 48 |     for i, tensor in enumerate(tensors):
 49 |         packed_tensor[i, :tensor.size(0)] = tensor
 50 | 
 51 |     return packed_tensor
 52 | 
 53 | 
 54 | def get_num_wins(
 55 |     n_frames: int,
 56 |     step: int,
 57 |     min_coverage: float,
 58 |     hp: VoiceEncConfig,
 59 | ):
 60 |     assert n_frames > 0
 61 |     win_size = hp.ve_partial_frames
 62 |     n_wins, remainder = divmod(max(n_frames - win_size + step, 0), step)
 63 |     if n_wins == 0 or (remainder + (win_size - step)) / win_size >= min_coverage:
 64 |         n_wins += 1
 65 |     target_n = win_size + step * (n_wins - 1)
 66 |     return n_wins, target_n
 67 | 
 68 | 
 69 | def get_frame_step(
 70 |     overlap: float,
 71 |     rate: float,
 72 |     hp: VoiceEncConfig,
 73 | ):
 74 |     # Compute how many frames separate two partial utterances
 75 |     assert 0 <= overlap < 1
 76 |     if rate is None:
 77 |         frame_step = int(np.round(hp.ve_partial_frames * (1 - overlap)))
 78 |     else:
 79 |         frame_step = int(np.round((hp.sample_rate / rate) / hp.ve_partial_frames))
 80 |     assert 0 < frame_step <= hp.ve_partial_frames
 81 |     return frame_step
 82 | 
 83 | 
 84 | def stride_as_partials(
 85 |     mel: np.ndarray,
 86 |     hp: VoiceEncConfig,
 87 |     overlap=0.5,
 88 |     rate: float=None,
 89 |     min_coverage=0.8,
 90 | ):
 91 |     """
 92 |     Takes unscaled mels in (T, M) format
 93 |     TODO: doc
 94 |     """
 95 |     assert 0 < min_coverage <= 1
 96 |     frame_step = get_frame_step(overlap, rate, hp)
 97 | 
 98 |     # Compute how many partials can fit in the mel
 99 |     n_partials, target_len = get_num_wins(len(mel), frame_step, min_coverage, hp)
100 | 
101 |     # Trim or pad the mel spectrogram to match the number of partials
102 |     if target_len > len(mel):
103 |         mel = np.concatenate((mel, np.full((target_len - len(mel), hp.num_mels), 0)))
104 |     elif target_len < len(mel):
105 |         mel = mel[:target_len]
106 | 
107 |     # Ensure the numpy array data is float32 and contiguous in memory
108 |     mel = mel.astype(np.float32, order="C")
109 | 
110 |     # Re-arrange the array in memory to be of shape (N, P, M) with partials overlapping eachother,
111 |     # where N is the number of partials, P is the number of frames of each partial and M the
112 |     # number of channels of the mel spectrograms.
113 |     shape = (n_partials, hp.ve_partial_frames, hp.num_mels)
114 |     strides = (mel.strides[0] * frame_step, mel.strides[0], mel.strides[1])
115 |     partials = as_strided(mel, shape, strides)
116 |     return partials
117 | 
118 | 
119 | class VoiceEncoder(nn.Module):
120 |     def __init__(self, hp=VoiceEncConfig()):
121 |         super().__init__()
122 | 
123 |         self.hp = hp
124 | 
125 |         # Network definition
126 |         self.lstm = nn.LSTM(self.hp.num_mels, self.hp.ve_hidden_size, num_layers=3, batch_first=True)
127 |         if hp.flatten_lstm_params:
128 |             self.lstm.flatten_parameters()
129 |         self.proj = nn.Linear(self.hp.ve_hidden_size, self.hp.speaker_embed_size)
130 | 
131 |         # Cosine similarity scaling (fixed initial parameter values)
132 |         self.similarity_weight = nn.Parameter(torch.tensor([10.]), requires_grad=True)
133 |         self.similarity_bias = nn.Parameter(torch.tensor([-5.]), requires_grad=True)
134 | 
135 |     @property
136 |     def device(self):
137 |         return next(self.parameters()).device
138 | 
139 |     def forward(self, mels: torch.FloatTensor):
140 |         """
141 |         Computes the embeddings of a batch of partial utterances.
142 | 
143 |         :param mels: a batch of unscaled mel spectrograms of same duration as a float32 tensor
144 |         of shape (B, T, M) where T is hp.ve_partial_frames
145 |         :return: the embeddings as a float32 tensor of shape (B, E) where E is
146 |         hp.speaker_embed_size. Embeddings are L2-normed and thus lay in the range [-1, 1].
147 |         """
148 |         if self.hp.normalized_mels and (mels.min() < 0 or mels.max() > 1):
149 |             raise Exception(f"Mels outside [0, 1]. Min={mels.min()}, Max={mels.max()}")
150 | 
151 |         # Pass the input through the LSTM layers
152 |         _, (hidden, _) = self.lstm(mels)
153 | 
154 |         # Project the final hidden state
155 |         raw_embeds = self.proj(hidden[-1])
156 |         if self.hp.ve_final_relu:
157 |             raw_embeds = F.relu(raw_embeds)
158 | 
159 |         # L2 normalize the embeddings.
160 |         return raw_embeds / torch.linalg.norm(raw_embeds, dim=1, keepdim=True)
161 | 
162 |     def inference(self, mels: torch.Tensor, mel_lens, overlap=0.5, rate: float=None, min_coverage=0.8, batch_size=None):
163 |         """
164 |         Computes the embeddings of a batch of full utterances with gradients.
165 | 
166 |         :param mels: (B, T, M) unscaled mels
167 |         :return: (B, E) embeddings on CPU
168 |         """
169 |         mel_lens = mel_lens.tolist() if torch.is_tensor(mel_lens) else mel_lens
170 | 
171 |         # Compute where to split the utterances into partials
172 |         frame_step = get_frame_step(overlap, rate, self.hp)
173 |         n_partials, target_lens = zip(*(get_num_wins(l, frame_step, min_coverage, self.hp) for l in mel_lens))
174 | 
175 |         # Possibly pad the mels to reach the target lengths
176 |         len_diff = max(target_lens) - mels.size(1)
177 |         if len_diff > 0:
178 |             pad = torch.full((mels.size(0), len_diff, self.hp.num_mels), 0, dtype=torch.float32)
179 |             mels = torch.cat((mels, pad.to(mels.device)), dim=1)
180 | 
181 |         # Group all partials together so that we can batch them easily
182 |         partials = [
183 |             mel[i * frame_step: i * frame_step + self.hp.ve_partial_frames]
184 |             for mel, n_partial in zip(mels, n_partials) for i in range(n_partial)
185 |         ]
186 |         assert all(partials[0].shape == partial.shape for partial in partials)
187 |         partials = torch.stack(partials)
188 | 
189 |         # Forward the partials
190 |         n_chunks = int(np.ceil(len(partials) / (batch_size or len(partials))))
191 |         partial_embeds = torch.cat([self(batch) for batch in partials.chunk(n_chunks)], dim=0).cpu()
192 | 
193 |         # Reduce the partial embeds into full embeds and L2-normalize them
194 |         slices = np.concatenate(([0], np.cumsum(n_partials)))
195 |         raw_embeds = [torch.mean(partial_embeds[start:end], dim=0) for start, end in zip(slices[:-1], slices[1:])]
196 |         raw_embeds = torch.stack(raw_embeds)
197 |         embeds = raw_embeds / torch.linalg.norm(raw_embeds, dim=1, keepdim=True)
198 | 
199 |         return embeds
200 | 
201 |     @staticmethod
202 |     def utt_to_spk_embed(utt_embeds: np.ndarray):
203 |         """
204 |         Takes an array of L2-normalized utterance embeddings, computes the mean embedding and L2-normalize it to get a
205 |         speaker embedding.
206 |         """
207 |         assert utt_embeds.ndim == 2
208 |         utt_embeds = np.mean(utt_embeds, axis=0)
209 |         return utt_embeds / np.linalg.norm(utt_embeds, 2)
210 | 
211 |     @staticmethod
212 |     def voice_similarity(embeds_x: np.ndarray, embeds_y: np.ndarray):
213 |         """
214 |         Cosine similarity for L2-normalized utterance embeddings or speaker embeddings
215 |         """
216 |         embeds_x = embeds_x if embeds_x.ndim == 1 else VoiceEncoder.utt_to_spk_embed(embeds_x)
217 |         embeds_y = embeds_y if embeds_y.ndim == 1 else VoiceEncoder.utt_to_spk_embed(embeds_y)
218 |         return embeds_x @ embeds_y
219 | 
220 |     def embeds_from_mels(
221 |         self, mels: Union[Tensor, List[np.ndarray]], mel_lens=None, as_spk=False, batch_size=32, **kwargs
222 |     ):
223 |         """
224 |         Convenience function for deriving utterance or speaker embeddings from mel spectrograms.
225 | 
226 |         :param mels: unscaled mels strictly within [0, 1] as either a (B, T, M) tensor or a list of (Ti, M) arrays.
227 |         :param mel_lens: if passing mels as a tensor, individual mel lengths
228 |         :param as_spk: whether to return utterance embeddings or a single speaker embedding
229 |         :param kwargs: args for inference()
230 | 
231 |         :returns: embeds as a (B, E) float32 numpy array if <as_spk> is False, else as a (E,) array
232 |         """
233 |         # Load mels in memory and pack them
234 |         if isinstance(mels, List):
235 |             mels = [np.asarray(mel) for mel in mels]
236 |             assert all(m.shape[1] == mels[0].shape[1] for m in mels), "Mels aren't in (B, T, M) format"
237 |             mel_lens = [mel.shape[0] for mel in mels]
238 |             mels = pack(mels)
239 | 
240 |         # Embed them
241 |         with torch.inference_mode():
242 |             utt_embeds = self.inference(mels.to(self.device), mel_lens, batch_size=batch_size, **kwargs).numpy()
243 | 
244 |         return self.utt_to_spk_embed(utt_embeds) if as_spk else utt_embeds
245 | 
246 |     def embeds_from_wavs(
247 |         self,
248 |         wavs: List[np.ndarray],
249 |         sample_rate,
250 |         as_spk=False,
251 |         batch_size=32,
252 |         trim_top_db: Optional[float]=20,
253 |         **kwargs
254 |     ):
255 |         """
256 |         Wrapper around embeds_from_mels
257 | 
258 |         :param trim_top_db: this argument was only added for the sake of compatibility with metavoice's implementation
259 |         """
260 |         if sample_rate != self.hp.sample_rate:
261 |             wavs = [
262 |                 librosa.resample(wav, orig_sr=sample_rate, target_sr=self.hp.sample_rate, res_type="kaiser_fast")
263 |                 for wav in wavs
264 |             ]
265 | 
266 |         if trim_top_db:
267 |             wavs = [librosa.effects.trim(wav, top_db=trim_top_db)[0] for wav in wavs]
268 | 
269 |         if "rate" not in kwargs:
270 |             kwargs["rate"] = 1.3  # Resemble's default value.
271 | 
272 |         mels = [melspectrogram(w, self.hp).T for w in wavs]
273 | 
274 |         return self.embeds_from_mels(mels, as_spk=as_spk, batch_size=batch_size, **kwargs)
275 | 


--------------------------------------------------------------------------------
/src/chatterbox/tts.py:
--------------------------------------------------------------------------------
  1 | from dataclasses import dataclass
  2 | from pathlib import Path
  3 | 
  4 | import librosa
  5 | import torch
  6 | import perth
  7 | import torch.nn.functional as F
  8 | from huggingface_hub import hf_hub_download
  9 | from safetensors.torch import load_file
 10 | 
 11 | from .models.t3 import T3
 12 | from .models.s3tokenizer import S3_SR, drop_invalid_tokens
 13 | from .models.s3gen import S3GEN_SR, S3Gen
 14 | from .models.tokenizers import EnTokenizer
 15 | from .models.voice_encoder import VoiceEncoder
 16 | from .models.t3.modules.cond_enc import T3Cond
 17 | 
 18 | 
 19 | REPO_ID = "ResembleAI/chatterbox"
 20 | 
 21 | 
 22 | def punc_norm(text: str) -> str:
 23 |     """
 24 |         Quick cleanup func for punctuation from LLMs or
 25 |         containing chars not seen often in the dataset
 26 |     """
 27 |     if len(text) == 0:
 28 |         return "You need to add some text for me to talk."
 29 | 
 30 |     # Capitalise first letter
 31 |     if text[0].islower():
 32 |         text = text[0].upper() + text[1:]
 33 | 
 34 |     # Remove multiple space chars
 35 |     text = " ".join(text.split())
 36 | 
 37 |     # Replace uncommon/llm punc
 38 |     punc_to_replace = [
 39 |         ("...", ", "),
 40 |         ("…", ", "),
 41 |         (":", ","),
 42 |         (" - ", ", "),
 43 |         (";", ", "),
 44 |         ("—", "-"),
 45 |         ("–", "-"),
 46 |         (" ,", ","),
 47 |         ("“", "\""),
 48 |         ("”", "\""),
 49 |         ("‘", "'"),
 50 |         ("’", "'"),
 51 |     ]
 52 |     for old_char_sequence, new_char in punc_to_replace:
 53 |         text = text.replace(old_char_sequence, new_char)
 54 | 
 55 |     # Add full stop if no ending punc
 56 |     text = text.rstrip(" ")
 57 |     sentence_enders = {".", "!", "?", "-", ","}
 58 |     if not any(text.endswith(p) for p in sentence_enders):
 59 |         text += "."
 60 | 
 61 |     return text
 62 | 
 63 | 
 64 | @dataclass
 65 | class Conditionals:
 66 |     """
 67 |     Conditionals for T3 and S3Gen
 68 |     - T3 conditionals:
 69 |         - speaker_emb
 70 |         - clap_emb
 71 |         - cond_prompt_speech_tokens
 72 |         - cond_prompt_speech_emb
 73 |         - emotion_adv
 74 |     - S3Gen conditionals:
 75 |         - prompt_token
 76 |         - prompt_token_len
 77 |         - prompt_feat
 78 |         - prompt_feat_len
 79 |         - embedding
 80 |     """
 81 |     t3: T3Cond
 82 |     gen: dict
 83 | 
 84 |     def to(self, device):
 85 |         self.t3 = self.t3.to(device=device)
 86 |         for k, v in self.gen.items():
 87 |             if torch.is_tensor(v):
 88 |                 self.gen[k] = v.to(device=device)
 89 |         return self
 90 | 
 91 |     def save(self, fpath: Path):
 92 |         arg_dict = dict(
 93 |             t3=self.t3.__dict__,
 94 |             gen=self.gen
 95 |         )
 96 |         torch.save(arg_dict, fpath)
 97 | 
 98 |     @classmethod
 99 |     def load(cls, fpath, map_location="cpu"):
100 |         if isinstance(map_location, str):
101 |             map_location = torch.device(map_location)
102 |         kwargs = torch.load(fpath, map_location=map_location, weights_only=True)
103 |         return cls(T3Cond(**kwargs['t3']), kwargs['gen'])
104 | 
105 | 
106 | class ChatterboxTTS:
107 |     ENC_COND_LEN = 6 * S3_SR
108 |     DEC_COND_LEN = 10 * S3GEN_SR
109 | 
110 |     def __init__(
111 |         self,
112 |         t3: T3,
113 |         s3gen: S3Gen,
114 |         ve: VoiceEncoder,
115 |         tokenizer: EnTokenizer,
116 |         device: str,
117 |         conds: Conditionals = None,
118 |     ):
119 |         self.sr = S3GEN_SR  # sample rate of synthesized audio
120 |         self.t3 = t3
121 |         self.s3gen = s3gen
122 |         self.ve = ve
123 |         self.tokenizer = tokenizer
124 |         self.device = device
125 |         self.conds = conds
126 |         self.watermarker = perth.PerthImplicitWatermarker()
127 | 
128 |     @classmethod
129 |     def from_local(cls, ckpt_dir, device) -> 'ChatterboxTTS':
130 |         ckpt_dir = Path(ckpt_dir)
131 | 
132 |         # Always load to CPU first for non-CUDA devices to handle CUDA-saved models
133 |         if device in ["cpu", "mps"]:
134 |             map_location = torch.device('cpu')
135 |         else:
136 |             map_location = None
137 | 
138 |         ve = VoiceEncoder()
139 |         ve.load_state_dict(
140 |             load_file(ckpt_dir / "ve.safetensors")
141 |         )
142 |         ve.to(device).eval()
143 | 
144 |         t3 = T3()
145 |         t3_state = load_file(ckpt_dir / "t3_cfg.safetensors")
146 |         if "model" in t3_state.keys():
147 |             t3_state = t3_state["model"][0]
148 |         t3.load_state_dict(t3_state)
149 |         t3.to(device).eval()
150 | 
151 |         s3gen = S3Gen()
152 |         s3gen.load_state_dict(
153 |             load_file(ckpt_dir / "s3gen.safetensors"), strict=False
154 |         )
155 |         s3gen.to(device).eval()
156 | 
157 |         tokenizer = EnTokenizer(
158 |             str(ckpt_dir / "tokenizer.json")
159 |         )
160 | 
161 |         conds = None
162 |         if (builtin_voice := ckpt_dir / "conds.pt").exists():
163 |             conds = Conditionals.load(builtin_voice, map_location=map_location).to(device)
164 | 
165 |         return cls(t3, s3gen, ve, tokenizer, device, conds=conds)
166 | 
167 |     @classmethod
168 |     def from_pretrained(cls, device) -> 'ChatterboxTTS':
169 |         # Check if MPS is available on macOS
170 |         if device == "mps" and not torch.backends.mps.is_available():
171 |             if not torch.backends.mps.is_built():
172 |                 print("MPS not available because the current PyTorch install was not built with MPS enabled.")
173 |             else:
174 |                 print("MPS not available because the current MacOS version is not 12.3+ and/or you do not have an MPS-enabled device on this machine.")
175 |             device = "cpu"
176 | 
177 |         for fpath in ["ve.safetensors", "t3_cfg.safetensors", "s3gen.safetensors", "tokenizer.json", "conds.pt"]:
178 |             local_path = hf_hub_download(repo_id=REPO_ID, filename=fpath)
179 | 
180 |         return cls.from_local(Path(local_path).parent, device)
181 | 
182 |     def prepare_conditionals(self, wav_fpath, exaggeration=0.5):
183 |         ## Load reference wav
184 |         s3gen_ref_wav, _sr = librosa.load(wav_fpath, sr=S3GEN_SR)
185 | 
186 |         ref_16k_wav = librosa.resample(s3gen_ref_wav, orig_sr=S3GEN_SR, target_sr=S3_SR)
187 | 
188 |         s3gen_ref_wav = s3gen_ref_wav[:self.DEC_COND_LEN]
189 |         s3gen_ref_dict = self.s3gen.embed_ref(s3gen_ref_wav, S3GEN_SR, device=self.device)
190 | 
191 |         # Speech cond prompt tokens
192 |         if plen := self.t3.hp.speech_cond_prompt_len:
193 |             s3_tokzr = self.s3gen.tokenizer
194 |             t3_cond_prompt_tokens, _ = s3_tokzr.forward([ref_16k_wav[:self.ENC_COND_LEN]], max_len=plen)
195 |             t3_cond_prompt_tokens = torch.atleast_2d(t3_cond_prompt_tokens).to(self.device)
196 | 
197 |         # Voice-encoder speaker embedding
198 |         ve_embed = torch.from_numpy(self.ve.embeds_from_wavs([ref_16k_wav], sample_rate=S3_SR))
199 |         ve_embed = ve_embed.mean(axis=0, keepdim=True).to(self.device)
200 | 
201 |         t3_cond = T3Cond(
202 |             speaker_emb=ve_embed,
203 |             cond_prompt_speech_tokens=t3_cond_prompt_tokens,
204 |             emotion_adv=exaggeration * torch.ones(1, 1, 1),
205 |         ).to(device=self.device)
206 |         self.conds = Conditionals(t3_cond, s3gen_ref_dict)
207 | 
208 |     def generate(
209 |         self,
210 |         text,
211 |         repetition_penalty=1.2,
212 |         min_p=0.05,
213 |         top_p=1.0,
214 |         audio_prompt_path=None,
215 |         exaggeration=0.5,
216 |         cfg_weight=0.5,
217 |         temperature=0.8,
218 |     ):
219 |         if audio_prompt_path:
220 |             self.prepare_conditionals(audio_prompt_path, exaggeration=exaggeration)
221 |         else:
222 |             assert self.conds is not None, "Please `prepare_conditionals` first or specify `audio_prompt_path`"
223 | 
224 |         # Update exaggeration if needed
225 |         if exaggeration != self.conds.t3.emotion_adv[0, 0, 0]:
226 |             _cond: T3Cond = self.conds.t3
227 |             self.conds.t3 = T3Cond(
228 |                 speaker_emb=_cond.speaker_emb,
229 |                 cond_prompt_speech_tokens=_cond.cond_prompt_speech_tokens,
230 |                 emotion_adv=exaggeration * torch.ones(1, 1, 1),
231 |             ).to(device=self.device)
232 | 
233 |         # Norm and tokenize text
234 |         text = punc_norm(text)
235 |         text_tokens = self.tokenizer.text_to_tokens(text).to(self.device)
236 | 
237 |         if cfg_weight > 0.0:
238 |             text_tokens = torch.cat([text_tokens, text_tokens], dim=0)  # Need two seqs for CFG
239 | 
240 |         sot = self.t3.hp.start_text_token
241 |         eot = self.t3.hp.stop_text_token
242 |         text_tokens = F.pad(text_tokens, (1, 0), value=sot)
243 |         text_tokens = F.pad(text_tokens, (0, 1), value=eot)
244 | 
245 |         with torch.inference_mode():
246 |             speech_tokens = self.t3.inference(
247 |                 t3_cond=self.conds.t3,
248 |                 text_tokens=text_tokens,
249 |                 max_new_tokens=1000,  # TODO: use the value in config
250 |                 temperature=temperature,
251 |                 cfg_weight=cfg_weight,
252 |                 repetition_penalty=repetition_penalty,
253 |                 min_p=min_p,
254 |                 top_p=top_p,
255 |             )
256 |             # Extract only the conditional batch.
257 |             speech_tokens = speech_tokens[0]
258 | 
259 |             # TODO: output becomes 1D
260 |             speech_tokens = drop_invalid_tokens(speech_tokens)
261 |             
262 |             speech_tokens = speech_tokens[speech_tokens < 6561]
263 | 
264 |             speech_tokens = speech_tokens.to(self.device)
265 | 
266 |             wav, _ = self.s3gen.inference(
267 |                 speech_tokens=speech_tokens,
268 |                 ref_dict=self.conds.gen,
269 |             )
270 |             wav = wav.squeeze(0).detach().cpu().numpy()
271 |             watermarked_wav = self.watermarker.apply_watermark(wav, sample_rate=self.sr)
272 |         return torch.from_numpy(watermarked_wav).unsqueeze(0)


--------------------------------------------------------------------------------
/src/chatterbox/vc.py:
--------------------------------------------------------------------------------
  1 | from pathlib import Path
  2 | 
  3 | import librosa
  4 | import torch
  5 | import perth
  6 | from huggingface_hub import hf_hub_download
  7 | from safetensors.torch import load_file
  8 | 
  9 | from .models.s3tokenizer import S3_SR
 10 | from .models.s3gen import S3GEN_SR, S3Gen
 11 | 
 12 | 
 13 | REPO_ID = "ResembleAI/chatterbox"
 14 | 
 15 | 
 16 | class ChatterboxVC:
 17 |     ENC_COND_LEN = 6 * S3_SR
 18 |     DEC_COND_LEN = 10 * S3GEN_SR
 19 | 
 20 |     def __init__(
 21 |         self,
 22 |         s3gen: S3Gen,
 23 |         device: str,
 24 |         ref_dict: dict=None,
 25 |     ):
 26 |         self.sr = S3GEN_SR
 27 |         self.s3gen = s3gen
 28 |         self.device = device
 29 |         self.watermarker = perth.PerthImplicitWatermarker()
 30 |         if ref_dict is None:
 31 |             self.ref_dict = None
 32 |         else:
 33 |             self.ref_dict = {
 34 |                 k: v.to(device) if torch.is_tensor(v) else v
 35 |                 for k, v in ref_dict.items()
 36 |             }
 37 | 
 38 |     @classmethod
 39 |     def from_local(cls, ckpt_dir, device) -> 'ChatterboxVC':
 40 |         ckpt_dir = Path(ckpt_dir)
 41 |         
 42 |         # Always load to CPU first for non-CUDA devices to handle CUDA-saved models
 43 |         if device in ["cpu", "mps"]:
 44 |             map_location = torch.device('cpu')
 45 |         else:
 46 |             map_location = None
 47 |             
 48 |         ref_dict = None
 49 |         if (builtin_voice := ckpt_dir / "conds.pt").exists():
 50 |             states = torch.load(builtin_voice, map_location=map_location)
 51 |             ref_dict = states['gen']
 52 | 
 53 |         s3gen = S3Gen()
 54 |         s3gen.load_state_dict(
 55 |             load_file(ckpt_dir / "s3gen.safetensors"), strict=False
 56 |         )
 57 |         s3gen.to(device).eval()
 58 | 
 59 |         return cls(s3gen, device, ref_dict=ref_dict)
 60 | 
 61 |     @classmethod
 62 |     def from_pretrained(cls, device) -> 'ChatterboxVC':
 63 |         # Check if MPS is available on macOS
 64 |         if device == "mps" and not torch.backends.mps.is_available():
 65 |             if not torch.backends.mps.is_built():
 66 |                 print("MPS not available because the current PyTorch install was not built with MPS enabled.")
 67 |             else:
 68 |                 print("MPS not available because the current MacOS version is not 12.3+ and/or you do not have an MPS-enabled device on this machine.")
 69 |             device = "cpu"
 70 |             
 71 |         for fpath in ["s3gen.safetensors", "conds.pt"]:
 72 |             local_path = hf_hub_download(repo_id=REPO_ID, filename=fpath)
 73 | 
 74 |         return cls.from_local(Path(local_path).parent, device)
 75 | 
 76 |     def set_target_voice(self, wav_fpath):
 77 |         ## Load reference wav
 78 |         s3gen_ref_wav, _sr = librosa.load(wav_fpath, sr=S3GEN_SR)
 79 | 
 80 |         s3gen_ref_wav = s3gen_ref_wav[:self.DEC_COND_LEN]
 81 |         self.ref_dict = self.s3gen.embed_ref(s3gen_ref_wav, S3GEN_SR, device=self.device)
 82 | 
 83 |     def generate(
 84 |         self,
 85 |         audio,
 86 |         target_voice_path=None,
 87 |     ):
 88 |         if target_voice_path:
 89 |             self.set_target_voice(target_voice_path)
 90 |         else:
 91 |             assert self.ref_dict is not None, "Please `prepare_conditionals` first or specify `target_voice_path`"
 92 | 
 93 |         with torch.inference_mode():
 94 |             audio_16, _ = librosa.load(audio, sr=S3_SR)
 95 |             audio_16 = torch.from_numpy(audio_16).float().to(self.device)[None, ]
 96 | 
 97 |             s3_tokens, _ = self.s3gen.tokenizer(audio_16)
 98 |             wav, _ = self.s3gen.inference(
 99 |                 speech_tokens=s3_tokens,
100 |                 ref_dict=self.ref_dict,
101 |             )
102 |             wav = wav.squeeze(0).detach().cpu().numpy()
103 |             watermarked_wav = self.watermarker.apply_watermark(wav, sample_rate=self.sr)
104 |         return torch.from_numpy(watermarked_wav).unsqueeze(0)


--------------------------------------------------------------------------------