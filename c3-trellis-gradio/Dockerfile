FROM ghcr.io/comput3ai/c3-trellis-gradio

## Run to download models
#RUN set -e && \
#    bash -c ' \
#    # Start the application \
#    ./venv/bin/python app.py & \
#    # Store the PID \
#    APP_PID=$! \
#    # Wait for initialization (120 seconds) \
#    echo "Waiting for initialization..." && \
#    sleep 900 && \
#    echo "Initialization period complete" && \
#    # Kill the main process \
#    kill $APP_PID && \
#    # Wait for process to terminate \
#    wait $APP_PID || true && \
#    echo "Initialization completed successfully"'

# Set the final command
CMD ["./venv/bin/python", "app.py"]
