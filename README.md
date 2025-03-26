# Comput3.ai Docker Images 🚀

[![GitHub stars](https://img.shields.io/github/stars/comput3ai/c3-docker-images?style=flat-square)](https://github.com/comput3ai/c3-docker-images/stargazers)
[![GitHub license](https://img.shields.io/github/license/comput3ai/c3-docker-images?style=flat-square)](https://github.com/comput3ai/c3-docker-images/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/comput3ai/c3-docker-images/pulls)

This repository contains Docker images for [Comput3.ai](https://comput3.ai), providing pre-configured containers for running various AI models through Ollama, a web interface through Open WebUI, stable diffusion image generation with ComfyUI, and optimized speech and audio processing services.

## Repository Structure

- `ollama/` - Contains Dockerfiles for various Ollama model configurations
- `open-webui/` - Contains a Dockerfile for the Open WebUI interface
- `ComfyUI/` - Contains a Dockerfile for setting up ComfyUI with common extensions
- `c3-whisperx-gradio/` - Contains a Dockerfile for optimized WhisperX speech-to-text with Gradio interface
- `c3-csm-gradio/` - Contains a Dockerfile for Composed Speech Model (CSM) with Gradio interface

## Ollama Images

All Ollama images are built on top of the official Ollama image and come pre-loaded with specific models for different use cases. Each container follows a multi-stage build process to efficiently download and prepare models.

### 🪶 Small Container (`ollama/Dockerfile.small`)

A lightweight container with small models that can run on limited hardware.

**Models included:**
- **Llama3:3b** (8-bit quantized): Meta's lightweight yet capable model for general text tasks
- **Hermes3:3b** (8-bit quantized): User-aligned model with improved steering capabilities

**Ideal for:** Edge devices, personal computers with limited resources, quick experimentation

### 🐘 Large Container (`ollama/Dockerfile.large`)

A high-performance container with larger models for advanced capabilities.

**Models included:**
- **Llama3:70b** (4-bit quantized): Meta's most powerful multilingual LLM optimized for dialogue, outperforming many open and closed source chat models
- **Hermes3:70b** (4-bit quantized): Powerful generalist language model with advanced agentic capabilities, improved reasoning, and long context coherence
- **Deepseek-R1:70b** (4-bit quantized): DeepSeek's first-generation reasoning model with performance comparable to OpenAI-o1
- **QwQ:32b** (8-bit quantized): Reasoning model achieving competitive performance against state-of-the-art reasoning models

**Ideal for:** High-end workstations, GPU-equipped systems, production environments

### ⚡ Fast Container (`ollama/Dockerfile.fast`)

Combines small and medium models for a balance of speed and capability.

**Models included:**
- All models from the small container
- **Llama3:8b** (8-bit quantized): Meta's multilingual model optimized for dialogue use cases
- **Hermes3:8b** (8-bit quantized): Enhanced version with improved multi-turn conversation capabilities
- **Deepseek-R1:8b** (8-bit quantized): Reasoning-focused model with performance comparable to larger models
- **Phi4:14b** (8-bit quantized): Microsoft's state-of-the-art 14B parameter model with 16k token context window, built on synthetic data and optimized for instruction following
- **Gemma3:27b**: Google's powerful multimodal model built on Gemini technology, featuring a 128K context window and support for over 140 languages
- **QwQ:32b** (4-bit quantized): Qwen's specialized reasoning model capable of enhanced performance on complex reasoning tasks

**Ideal for:** Development environments requiring a variety of model sizes

### 🌟 All Container (`ollama/Dockerfile.all`)

A comprehensive collection of all models across all size categories.

**Models included:**
- All models
- **Qwen2.5-coder:32b** (8-bit quantized): Larger code-specific Qwen model for advanced code tasks

**Ideal for:** Testing environments, situations where model flexibility is paramount

### 💻 Coder Container (`ollama/Dockerfile.coder`)

Specialized for code generation and programming tasks.

**Models included:**
- **Qwen2.5-coder:32b** (8-bit quantized): The latest series of Code-Specific Qwen models with significant improvements in code generation, reasoning, and fixing
- **CodeGemma:7b** (fp16): Google's powerful, lightweight model for code completion, generation, and instruction following
- **CodeLlama:34b** (8-bit quantized): Meta's specialized code model supporting multiple programming languages including Python, C++, Java, PHP, TypeScript, C#, and Bash
- **Deepseek-coder-v2:16b** (fp16): Open-source Mixture-of-Experts code model with performance comparable to GPT4-Turbo in code-specific tasks
- **QwQ:32b** (8-bit quantized): Reasoning model that enhances performance in complex programming problem-solving

**Ideal for:** Software development, code completion, programming assistance

## Open WebUI 🌐

The `open-webui` directory contains a Dockerfile that builds on top of the official Open WebUI image. It pre-initializes the application during build time to ensure quick startup when deployed.

## Speech Processing Containers 🔊

### 🎤 WhisperX Gradio Container (`c3-whisperx-gradio`)

An optimized container for speech-to-text transcription with alignment features.

**Features:**
- Pre-downloads all Whisper models (tiny, small, medium, large-v2)
- Pre-downloads the English language alignment model
- Automatically initializes models at container startup
- Provides a user-friendly Gradio interface

**Ideal for:** Speech-to-text transcription, subtitling, and audio analysis with precise word-level alignments

### 🗣️ CSM Gradio Container (`c3-csm-gradio`)

A container for the Composed Speech Model (CSM) that enables high-quality speech generation.

**Features:**
- Pre-downloads and initializes all required CSM components:
  - Llama 3.2 1B tokenizer
  - Mimi audio tokenizer
  - Watermarking module
  - CSM-1B speech generation model
- Provides a Gradio interface for easy use

**Ideal for:** Voice generation, text-to-speech applications, and audio content creation

## ComfyUI 🎨

The ComfyUI container provides a ready-to-use environment for stable diffusion image generation with a feature-rich UI.

**Features included:**
- Base ComfyUI installation with NVIDIA GPU support
- ComfyUI Manager for easy extension and model management
- Video Helper Suite for video generation workflows
- Easy-Use nodes for streamlined workflows
- Sonic nodes for audio processing capabilities
- WAS Node Suite with additional advanced nodes

**Ideal for:** Image generation, AI art creation, and video synthesis workflows

## Building Images 🏗️

Comput3.AI publishes these Docker images for transparency and to help the AI community. By making the build process open and accessible, we aim to foster collaboration and innovation in AI deployment.

### Building from Source

To build the standard set of Ollama images (small, medium, large), use the build script:

```bash
git clone https://github.com/comput3/c3-docker-images.git
cd c3-docker-images/ollama
./build.sh
```

To build other variants (fast, all, coder), use Docker build directly:

```bash
cd ollama
docker build -f Dockerfile.fast -t comput3/ollama:fast .
```

For building the Open WebUI image:

```bash
cd open-webui
docker build -t comput3/open-webui:latest .
```

For building the ComfyUI image:

```bash
cd ComfyUI
docker build -t comput3/comfyui:latest .
```

For building the WhisperX Gradio image:

```bash
cd c3-whisperx-gradio
docker build -t comput3/whisperx-gradio:latest .
```

For building the CSM Gradio image:

```bash
cd c3-csm-gradio
docker build -t comput3/csm-gradio:latest .
```

### Build Time Considerations ⏱️

Building these images requires downloading the AI models, which can vary in time depending on your internet connection speed. The larger containers (especially the "all" and "large" variants) will take significantly longer to build.

Approximate build times on a 500Mbps connection:
- 🪶 Small container: 3-6 minutes
- 🏃 Medium container: 9-18 minutes
- 🐘 Large container: 25-50 minutes
- 🌟 All container: 35-70 minutes
- 💻 Coder container: 12-36 minutes
- 🎨 ComfyUI container: 15-30 minutes
- 🎤 WhisperX Gradio container: 10-20 minutes
- 🗣️ CSM Gradio container: 15-25 minutes

⚠️ If your connection is slower, build times will increase proportionally. Be patient - these models are worth the wait! ⚠️

### Model Usage and Licensing 📜

Please note that while these Docker images are provided under the MIT license, the AI models contained within them are subject to the End User License Agreements (EULAs) of their respective creators:

- 🔹 Meta's Llama 3 and Code Llama models are subject to the [Llama 3 Community License](https://ai.meta.com/llama/license/)
- 🔸 Microsoft's Phi-4 model is subject to the [Microsoft Research License](https://huggingface.co/microsoft/phi-4/blob/main/LICENSE)
- 🔶 Qwen models are subject to the [Qwen License Agreement](https://qwenlm.github.io/blog/qwen-license/)
- 🔷 DeepSeek models are subject to the [DeepSeek License](https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/LICENSE)
- 🔹 Google's Gemma 3 model is subject to the [Gemma License](https://ai.google.dev/gemma/terms)
- 🎨 ComfyUI and its extensions are subject to their respective licenses
- 🎤 WhisperX is subject to the [MIT License](https://github.com/m-bain/whisperX/blob/main/LICENSE)
- 🗣️ CSM (Composed Speech Model) is subject to its respective license

⚖️ Be sure to review these licenses before using these models in your applications. Comput3.AI provides these containers to make AI more accessible, but we respect the intellectual property rights of model creators!

## Usage 🔧

### Running Ollama 🤖

```bash
docker run -d --name ollama -p 11434:11434 comput3/ollama:medium
```

You can swap `:medium` with `:small`, `:large`, `:fast`, `:all`, or `:coder` depending on your needs!

### Running Open WebUI 🖥️

```bash
docker run -d --name open-webui -p 3000:3000 -e OLLAMA_API_BASE_URL=http://ollama:11434 --link ollama comput3/open-webui:latest
```

### Running WhisperX Gradio 🎤

```bash
docker run -d --name whisperx-gradio -p 7860:7860 comput3/whisperx-gradio:latest
```

You can access the WhisperX Gradio interface by navigating to `http://localhost:7860` in your web browser.

### Running CSM Gradio 🗣️

```bash
docker run -d --name csm-gradio -p 7861:7860 comput3/csm-gradio:latest
```

You can access the CSM Gradio interface by navigating to `http://localhost:7861` in your web browser.

### Running ComfyUI 🎨

```bash
docker run -d --name comfyui -p 8188:8188 --gpus all comput3/comfyui:latest
```

You can access ComfyUI by navigating to `http://localhost:8188` in your web browser.

### Using Docker Compose 🐳

For the best experience, connect multiple containers using Docker Compose:

```yaml
# docker-compose.yml
version: '3'
services:
  ollama:
    image: comput3/ollama:medium
    ports:
      - "11434:11434"
    volumes:
      - ollama-data:/root/.ollama
    restart: unless-stopped

  open-webui:
    image: comput3/open-webui:latest
    ports:
      - "3000:3000"
    environment:
      - OLLAMA_API_BASE_URL=http://ollama:11434
    depends_on:
      - ollama
    restart: unless-stopped
    
  whisperx-gradio:
    image: comput3/whisperx-gradio:latest
    ports:
      - "7860:7860"
    restart: unless-stopped
    
  csm-gradio:
    image: comput3/csm-gradio:latest
    ports:
      - "7861:7860"
    restart: unless-stopped
    
  comfyui:
    image: comput3/comfyui:latest
    ports:
      - "8188:8188"
    volumes:
      - ./models:/app/ComfyUI/models
      - ./outputs:/app/ComfyUI/output
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    restart: unless-stopped

volumes:
  ollama-data:
```

Run with: `docker-compose up -d` 🚀

### Hardware Requirements 💪

Recommended minimum specs for each container type:

- 🪶 **Small**: 4GB RAM, 2 CPU cores, 5GB disk space
- 🏃 **Medium**: 8GB RAM, 4 CPU cores, 15GB disk space
- 🐘 **Large**: 16GB RAM, 8 CPU cores, 40GB disk space + GPU recommended
- ⚡ **Fast**: 8GB RAM, 4 CPU cores, 20GB disk space
- 🌟 **All**: 32GB RAM, 8+ CPU cores, 60GB disk space + GPU strongly recommended
- 💻 **Coder**: 16GB RAM, 8 CPU cores, 30GB disk space + GPU recommended
- 🎨 **ComfyUI**: 16GB RAM, 6 CPU cores, 10GB disk space + NVIDIA GPU required
- 🎤 **WhisperX Gradio**: 8GB RAM, 4 CPU cores, 10GB disk space + GPU recommended for faster transcription
- 🗣️ **CSM Gradio**: 8GB RAM, 4 CPU cores, 10GB disk space + GPU recommended for faster speech generation

## Contributing 👥

Contributions are welcome! Please feel free to submit a Pull Request. Here are ways you can help:

- 🐛 Report bugs and issues
- ✨ Suggest new features or model configurations
- 📝 Improve documentation
- 🔧 Submit optimizations to Dockerfiles
- 🧪 Test on different hardware configurations

## About Comput3.AI 🌐

[Comput3.AI](https://comput3.ai) is committed to making AI accessible and transparent. We believe in:

- 🔓 Open source collaboration
- 🧠 Democratizing access to AI technology
- 🌱 Supporting the AI community
- 🛠️ Providing practical tools for real-world applications
- 🎨 Enabling creative AI workflows with stable diffusion tools like ComfyUI
- 🔊 Making speech and audio AI accessible to everyone

These Docker images are published to foster innovation and help developers easily experiment with state-of-the-art AI models and creative tools.

## License 📄

This project is licensed under the terms of the MIT license. ✅

---

Made with ❤️ by the Comput3.AI team