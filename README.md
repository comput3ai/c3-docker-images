# Comput3.ai Docker Images 🚀

[![GitHub stars](https://img.shields.io/github/stars/comput3ai/c3-docker-images?style=flat-square)](https://github.com/comput3ai/c3-docker-images/stargazers)
[![GitHub license](https://img.shields.io/github/license/comput3ai/c3-docker-images?style=flat-square)](https://github.com/comput3ai/c3-docker-images/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/comput3ai/c3-docker-images/pulls)

This repository contains Docker images for [Comput3.ai](https://comput3.ai), providing pre-configured containers for running various AI models through Ollama, a web interface through Open WebUI, and stable diffusion image generation with ComfyUI.

## Repository Structure

- `ollama/` - Contains Dockerfiles for various Ollama model configurations
- `open-webui/` - Contains a Dockerfile for the Open WebUI interface
- `ComfyUI/` - Contains a Dockerfile for setting up ComfyUI with common extensions

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

### Build Time Considerations ⏱️

Building these images requires downloading the AI models, which can vary in time depending on your internet connection speed. The larger containers (especially the "all" and "large" variants) will take significantly longer to build.

Approximate build times on a 500Mbps connection:
- 🪶 Small container: 3-6 minutes
- 🏃 Medium container: 9-18 minutes
- 🐘 Large container: 25-50 minutes
- 🌟 All container: 35-70 minutes
- 💻 Coder container: 12-36 minutes
- 🎨 ComfyUI container: 15-30 minutes

⚠️ If your connection is slower, build times will increase proportionally. Be patient - these models are worth the wait! ⚠️

### Model Usage and Licensing 📜

Please note that while these Docker images are provided under the MIT license, the AI models contained within them are subject to the End User License Agreements (EULAs) of their respective creators:

- 🔹 Meta's Llama 3 and Code Llama models are subject to the [Llama 3 Community License](https://ai.meta.com/llama/license/)
- 🔸 Microsoft's Phi-4 model is subject to the [Microsoft Research License](https://huggingface.co/microsoft/phi-4/blob/main/LICENSE)
- 🔶 Qwen models are subject to the [Qwen License Agreement](https://qwenlm.github.io/blog/qwen-license/)
- 🔷 DeepSeek models are subject to the [DeepSeek License](https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/LICENSE)
- 🔹 Google's Gemma 3 model is subject to the [Gemma License](https://ai.google.dev/gemma/terms)
- 🎨 ComfyUI and its extensions are subject to their respective licenses

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

### Using Docker Compose 🐳

For the best experience, connect the Open WebUI container to an Ollama container using Docker Compose:

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

volumes:
  ollama-data:
```

Run with: `docker-compose up -d` 🚀

### Running ComfyUI 🎨

```bash
docker run -d --name comfyui -p 8188:8188 --gpus all comput3/comfyui:latest
```

You can access ComfyUI by navigating to `http://localhost:8188` in your web browser.

### Using Volume Mounts with ComfyUI 📂

Volume mounts allow you to access files from your host system inside the Docker container, which is especially useful for ComfyUI model files and outputs.

```bash
docker run -d --name comfyui --gpus all \
  -v /local/path/to/models/checkpoints:/app/ComfyUI/models/checkpoints \
  -v /local/path/to/models/loras:/app/ComfyUI/models/loras \
  -v /local/path/to/outputs:/app/ComfyUI/output \
  -p 8188:8188 \
  comput3/comfyui:latest
```

For a more complete setup, you can use Docker Compose:

```yaml
# docker-compose.yml for ComfyUI
version: '3.8'

services:
  comfyui:
    image: comput3/comfyui:latest
    ports:
      - "8188:8188"
    volumes:
      # Model directories
      - ./models/checkpoints:/app/ComfyUI/models/checkpoints
      - ./models/loras:/app/ComfyUI/models/loras
      - ./models/controlnet:/app/ComfyUI/models/controlnet
      - ./models/vae:/app/ComfyUI/models/vae
      # Output directory
      - ./outputs:/app/ComfyUI/output
      # Custom workflows
      - ./workflows:/app/ComfyUI/workflows
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

The key model directories in the ComfyUI container are:
- `/app/ComfyUI/models/checkpoints` - Stable Diffusion model files (.safetensors, .ckpt)
- `/app/ComfyUI/models/loras` - LoRA adapters
- `/app/ComfyUI/models/controlnet` - ControlNet models
- `/app/ComfyUI/models/vae` - VAE models

Using volume mounts allows you to keep your models outside the container, making them easier to update and manage.

### Hardware Requirements 💪

Recommended minimum specs for each container type:

- 🪶 **Small**: 4GB RAM, 2 CPU cores, 5GB disk space
- 🏃 **Medium**: 8GB RAM, 4 CPU cores, 15GB disk space
- 🐘 **Large**: 16GB RAM, 8 CPU cores, 40GB disk space + GPU recommended
- ⚡ **Fast**: 8GB RAM, 4 CPU cores, 20GB disk space
- 🌟 **All**: 32GB RAM, 8+ CPU cores, 60GB disk space + GPU strongly recommended
- 💻 **Coder**: 16GB RAM, 8 CPU cores, 30GB disk space + GPU recommended
- 🎨 **ComfyUI**: 16GB RAM, 6 CPU cores, 10GB disk space + NVIDIA GPU required

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

These Docker images are published to foster innovation and help developers easily experiment with state-of-the-art AI models and creative tools.

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

## License 📄

This project is licensed under the terms of the MIT license. ✅

---

Made with ❤️ by the Comput3.AI team
