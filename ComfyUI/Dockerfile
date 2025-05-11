# Define the version as a build argument
ARG COMFYUI_VERSION=v0.3.33

# Base downloader stage with common setup
FROM nvidia/cuda:12.8.1-cudnn-runtime-ubuntu24.04

# Re-declare the ARG after FROM
ARG COMFYUI_VERSION

# Install Python and required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -s /bin/bash comfyuser

# Set up workspace directory and adjust permissions
WORKDIR /app
RUN chown -R comfyuser:comfyuser /app

# Switch to the non-root user
USER comfyuser

# Create virtual environment
RUN python3 -m venv /app/venv

# Use shell form for commands that need to source the activation script
SHELL ["/bin/bash", "-c"]

# Install comfy-cli and required dependencies
RUN source /app/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install torch torchvision torchaudio && \
    pip install triton && \
    pip install comfy-cli

# Install ComfyUI
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI install --version $COMFYUI_VERSION --nvidia

# Install ComfyUI custom_nodes
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-manager
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-videohelpersuite
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-easy-use
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install ComfyUI_Sonic
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install ComfyUI-GGUF
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install ComfyUI-WanVideoWrapper
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui_essentials
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-art-venture
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-logicutils
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-kjnodes
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install was-node-suite-comfyui

# Create model directories to ensure proper permissions
RUN mkdir -p /app/ComfyUI/models/checkpoints /app/ComfyUI/models/sonic /app/ComfyUI/models/vae /app/ComfyUI/models/text_encoders /app/ComfyUI/models/diffusion_models /app/ComfyUI/models/clip_vision

# Expose port (default ComfyUI port is 8188)
EXPOSE 8188

# Set the entrypoint to source the venv and then launch ComfyUI
ENTRYPOINT ["/bin/bash", "-c", "source /app/venv/bin/activate && comfy --workspace /app/ComfyUI launch -- --listen 0.0.0.0"]
