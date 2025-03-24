import os
import torch
import gc
from faster_whisper.utils import download_model

# This script downloads model files directly using faster-whisper's mechanism
# which is what WhisperX uses under the hood

def download_whisper_model(model_name):
    """
    Downloads the Whisper model files without initializing a model
    """
    print(f"Downloading {model_name} model files...")
    # This will download the model files to cache without initializing the models
    cache_dir = download_model(model_name)
    print(f"{model_name} model downloaded successfully to {cache_dir}")

    # Clean up memory
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return cache_dir

# Download each model
models = ["tiny", "small", "medium", "large-v2"]
for model_name in models:
    try:
        download_whisper_model(model_name)
    except Exception as e:
        print(f"Error downloading {model_name}: {e}")

print("All models have been downloaded and cached")
