FROM ghcr.io/comput3ai/c3-whisperx-gradio

# Copy the preloadialization script
COPY --chmod=755 preload.py /app/preload.py

# Run the preloadialization script
RUN python /app/preload.py

# Command to run when the container starts
CMD ["python", "app.py"]