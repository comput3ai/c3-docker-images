FROM ghcr.io/comput3ai/c3-whisperx-gradio

# Copy the initialization script
COPY --chmod=755 init.py /app/init.py

# Run the initialization script
RUN python /app/init.py

# Command to run when the container starts
CMD ["python", "app.py"]