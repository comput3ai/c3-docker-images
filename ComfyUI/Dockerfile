FROM nvidia/cuda:12.8.1-cudnn-runtime-ubuntu24.04

# Install Python and required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
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
    pip install comfy-cli

# Install ComfyUI
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI install --nvidia

# Install ComfyUI custom_nodes
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-manager
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-videohelpersuite
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install comfyui-easy-use
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install ComfyUI_Sonic
RUN source /app/venv/bin/activate && comfy --skip-prompt --workspace /app/ComfyUI node install was-node-suite-comfyui

# Custom Nodes outside of ComfyUI Repository
RUN source /app/venv/bin/activate && cd /app/ComfyUI/custom_nodes && git clone https://github.com/nedos/ComfyUI-CSM-Nodes.git && cd ComfyUI-CSM-Nodes && pip install -r requirements.txt

# Create model directories to ensure proper permissions
RUN mkdir -p /app/ComfyUI/models/checkpoints /app/ComfyUI/models/sonic /app/ComfyUI/models/sesame /app/ComfyUI/models/sesame_tokenizer

# Expose port (default ComfyUI port is 8188)
EXPOSE 8188

# Set the entrypoint to source the venv and then launch ComfyUI
ENTRYPOINT ["/bin/bash", "-c", "source /app/venv/bin/activate && comfy --workspace /app/ComfyUI launch -- --listen 0.0.0.0"]