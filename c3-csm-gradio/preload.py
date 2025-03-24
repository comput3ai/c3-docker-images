import torch
import os
import gc
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download
from models import Model
from moshi.models import loaders
from generator import load_csm_1b, load_llama3_tokenizer
from watermarking import load_watermarker

# Disable Triton compilation
os.environ["NO_TORCH_COMPILE"] = "1"

# Select the best available device
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"
print(f"Using device: {device}")

# 1. Initialize Llama 3.2 tokenizer (downloads the model)
print("Initializing Llama 3.2 1B tokenizer...")
tokenizer = load_llama3_tokenizer()
print("Llama 3.2 1B tokenizer initialized")

# 2. Initialize Mimi audio tokenizer
print("Initializing Mimi audio tokenizer...")
mimi_weight = hf_hub_download(loaders.DEFAULT_REPO, loaders.MIMI_NAME)
mimi = loaders.get_mimi(mimi_weight, device=device)
mimi.set_num_codebooks(32)
print("Mimi audio tokenizer initialized")

# 3. Initialize watermarker
print("Initializing watermarker...")
watermarker = load_watermarker(device=device)
print("Watermarker initialized")

# 4. Initialize CSM-1B model (including the Llama backbone)
print("Loading CSM 1B model...")
model = Model.from_pretrained("sesame/csm-1b")
model.to(device=device, dtype=torch.bfloat16)
print("CSM 1B model parameters loaded")

# 5. Download example prompt files (optional but useful to have cached)
print("Downloading example prompt files...")
prompts = [
    "prompts/conversational_a.wav",
    "prompts/conversational_b.wav"
]
for prompt in prompts:
    prompt_file = hf_hub_download(repo_id="sesame/csm-1b", filename=prompt)
    print(f"Downloaded {prompt}")

# 6. Initialize the full generator (which combines all components)
print("Initializing full generator...")
generator = load_csm_1b(device=device)
print("Full generator initialized")

# Free memory
del generator
del model
del mimi
del tokenizer
del watermarker
gc.collect()
if device == "cuda":
    torch.cuda.empty_cache()

print("All components initialized and memory cleared")
