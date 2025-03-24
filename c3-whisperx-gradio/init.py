import whisperx
import torch
import gc

# Load each model and then free memory
device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "float16"

# Tiny model
model = whisperx.load_model("tiny", device, compute_type=compute_type)
del model; gc.collect(); torch.cuda.empty_cache()

# Small model
model = whisperx.load_model("small", device, compute_type=compute_type)
del model; gc.collect(); torch.cuda.empty_cache()

# Medium model
model = whisperx.load_model("medium", device, compute_type=compute_type)
del model; gc.collect(); torch.cuda.empty_cache()

# Large-v2 model
model = whisperx.load_model("large-v2", device, compute_type=compute_type)
del model; gc.collect(); torch.cuda.empty_cache()

print("All models loaded successfully")
