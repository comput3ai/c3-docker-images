import os
import torch
import gc
from huggingface_hub import snapshot_download
import json

# Get model repository from environment variable with default
MODEL_REPO = os.environ.get("TRELLIS_MODEL_REPO", "jetx/trellis-image-large")
print(f"Preloading models from: {MODEL_REPO}")

# Download the main Trellis model and all its components
print(f"Downloading Trellis model from {MODEL_REPO}...")
try:
    # This downloads the entire model repository including pipeline.json and all model files
    model_path = snapshot_download(
        repo_id=MODEL_REPO,
        cache_dir=os.environ.get("HF_HOME", None)  # Use HF_HOME if set, otherwise default
    )
    print(f"Trellis model downloaded successfully to: {model_path}")
    
    # Read pipeline.json to see what models are included
    pipeline_config_path = os.path.join(model_path, "pipeline.json")
    if os.path.exists(pipeline_config_path):
        with open(pipeline_config_path, 'r') as f:
            config = json.load(f)
            models_list = config.get('args', {}).get('models', {})
            print(f"Models included in pipeline: {list(models_list.keys())}")
    
except Exception as e:
    print(f"Error downloading Trellis model: {e}")
    raise

# Download DINOv2 model that's used for image conditioning
# The app loads this via torch.hub which has its own caching
print("Downloading DINOv2 model...")
try:
    # Force download of the DINOv2 model that Trellis uses
    # Based on the code, it uses the model name from the pipeline args
    # Let's check what model is specified
    if os.path.exists(pipeline_config_path):
        with open(pipeline_config_path, 'r') as f:
            config = json.load(f)
            dinov2_model_name = config.get('args', {}).get('image_cond_model', 'dinov2_vitb14_reg')
    else:
        # Default to the commonly used model
        dinov2_model_name = 'dinov2_vitb14_reg'
    
    print(f"Loading DINOv2 model: {dinov2_model_name}")
    dinov2_model = torch.hub.load('facebookresearch/dinov2', dinov2_model_name, pretrained=True)
    print(f"DINOv2 model {dinov2_model_name} downloaded successfully")
    
    # Clean up memory
    del dinov2_model
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        
except Exception as e:
    print(f"Error downloading DINOv2 model: {e}")
    # Don't raise here as it might still work with lazy loading

print("All models have been preloaded successfully!")