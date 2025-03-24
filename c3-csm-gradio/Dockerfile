FROM ghcr.io/comput3ai/c3-csm-gradio:latest
ARG HF_TOKEN

# Copy the initialization script
COPY --chmod=755 init.py /app/csm/init.py

# Run the initialization script
RUN python /app/csm/init.py

# Command to run when the container starts
CMD ["python", "app.py"]
