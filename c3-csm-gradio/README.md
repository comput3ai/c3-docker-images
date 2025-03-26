# c3-csm-gradio

This repository extends the base CSM (Composed Speech Model) Gradio interface with pre-downloaded models to improve startup performance and reliability.

## Overview

The standard CSM Gradio image downloads models on first use, which can cause significant delays and timeout issues in production environments. This extended image pre-downloads and initializes all necessary models during the Docker build process, ensuring faster startup times and better reliability.

## Features

- Pre-downloads and initializes all required CSM components:
  - Llama 3.2 1B tokenizer
  - Mimi audio tokenizer
  - Watermarking module
  - CSM-1B speech generation model
  - Example prompt files
- Automatically loads models during container build via `preload.py`
- Cleans up memory after initialization
- Maintains all functionality of the original CSM Gradio interface

## Technical Details

The pre-loading mechanism works by:

1. Downloading all model components from HuggingFace
2. Properly initializing each component to ensure cache files are created
3. Loading example prompts to ensure they're cached
4. Properly releasing memory after initialization
5. Running this process during Docker image build, rather than at runtime

This approach ensures that all models are already in the local cache when the application starts, eliminating download time during initialization.

## Usage

Use this image instead of the base CSM Gradio image when you need consistent startup performance, especially in production environments with potential timeout constraints.

```bash
docker pull c3/csm-gradio:latest
docker run -p 7860:7860 c3/csm-gradio:latest
```

## Development

If you need to modify the preloading behavior, edit the `preload.py` script. This script is executed during the Docker build process to download and cache all required models.

The key components that get preloaded are:
- Llama 3.2 1B tokenizer
- Mimi audio tokenizer 
- Watermarking module
- CSM-1B (Composed Speech Model) from sesame/csm-1b
- Example conversation prompts

---

Based on the original CSM (Composed Speech Model) project and its Gradio interface. See the source repository for more details about CSM functionality.