FROM ghcr.io/comput3ai/c3-rembg-gradio:latest

# Download all rembg models
RUN rembg d

# Use the original entrypoint
CMD ["python", "app.py"]