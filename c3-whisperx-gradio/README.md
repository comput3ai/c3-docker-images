# c3-whisperx-gradio

This repository extends the base WhisperX Gradio interface with pre-downloaded models to improve startup performance.

## Overview

The standard WhisperX Gradio image downloads models on first use, which can cause significant delays and timeout issues in production environments. This extended image pre-downloads all necessary models during the Docker build process, ensuring faster startup times and better reliability.

## Features

- Pre-downloads all Whisper models (tiny, small, medium, large-v2) 
- Pre-downloads the English language alignment model (WAV2VEC2_ASR_BASE_960H)
- Automatically initializes models at container startup via `preload.py`
- Maintains all functionality of the original WhisperX Gradio interface

## Technical Details

The pre-loading mechanism works by:

1. Using `faster_whisper.utils.download_model()` to download Whisper models directly
2. Using HuggingFace's Transformers library to download the alignment model
3. Running this process during Docker image build, rather than at runtime

This approach ensures that the models are already in the local cache when the application starts, eliminating download time during initialization.

## Usage

Use this image instead of the base WhisperX Gradio image when you need consistent startup performance, especially in production environments with potential timeout constraints.

```bash
docker pull c3/whisperx-gradio:latest
docker run -p 7860:7860 c3/whisperx-gradio:latest
```

## Development

If you need to modify the preloading behavior, edit the `preload.py` script. This script is executed during the Docker build process to download and cache all required models.

---

Based on the original WhisperX project and its Gradio interface. See the source repository for more details about WhisperX functionality.