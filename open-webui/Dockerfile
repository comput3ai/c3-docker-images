# Start with the base image
FROM ghcr.io/open-webui/open-webui:v0.5.20

# Run the initialization process
ENV WEBUI_AUTH=false

RUN set -e && \
    bash -c ' \
    # Start the application \
    bash start.sh & \
    # Store the PID \
    APP_PID=$! \
    # Wait for initialization (120 seconds) \
    echo "Waiting for initialization..." && \
    sleep 300 && \
    echo "Initialization period complete" && \
    # Kill the main process \
    kill $APP_PID && \
    # Wait for process to terminate \
    wait $APP_PID || true && \
    echo "Initialization completed successfully"'

# Set the final command
CMD ["bash", "start.sh"]
