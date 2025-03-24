FROM ghcr.io/comput3ai/c3-csm-gradio:latest
ARG HF_TOKEN

# Copy the initialization script (already executable)
COPY --chmod=755 init.sh /tmp/init.sh

# Execute the initialization script during build
RUN /tmp/init.sh

# Command to run when the container starts
CMD ["python", "app.py"]