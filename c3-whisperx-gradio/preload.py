import os
import torch
import gc
from faster_whisper.utils import download_model
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

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

def download_alignment_model(model_name):
    """
    Downloads the language alignment model files from HuggingFace
    """
    print(f"Downloading alignment model: {model_name}...")
    try:
        # This downloads and caches the model files
        processor = Wav2Vec2Processor.from_pretrained(model_name)
        model = Wav2Vec2ForCTC.from_pretrained(model_name)
        print(f"Alignment model {model_name} downloaded successfully")
        
        # Clean up memory
        del processor
        del model
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception as e:
        print(f"Error downloading alignment model {model_name}: {e}")

# Download each whisper model
whisper_models = ["tiny", "small", "medium", "large-v2"]
for model_name in whisper_models:
    try:
        download_whisper_model(model_name)
    except Exception as e:
        print(f"Error downloading {model_name}: {e}")

# Add English alignment model (from torchaudio)
# This will ensure the English model is downloaded but not initialized
print("Downloading English alignment model...")
try:
    download_alignment_model("WAV2VEC2_ASR_BASE_960H")
except Exception as e:
    print(f"Error downloading English alignment model: {e}")

print("All models have been downloaded and cached")
