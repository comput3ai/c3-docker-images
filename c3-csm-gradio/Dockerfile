FROM ghcr.io/comput3ai/c3-csm-gradio:latest
ARG HF_TOKEN

# Copy the preloadialization script
COPY --chmod=755 preload.py /app/csm/preload.py

# Run the preloadialization script
RUN python /app/csm/preload.py

# Command to run when the container starts
CMD ["python", "app.py"]
