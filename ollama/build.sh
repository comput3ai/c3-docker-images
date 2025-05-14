#!/bin/bash

# Build xlarge version
echo "Building xlarge version..."
docker build -f Dockerfile.xlarge -t comput3ai/ollama:xlarge .

# Build large version
echo "Building large version..."
docker build -f Dockerfile.large -t comput3ai/ollama:large .

# Build small version
echo "Building small version..."
docker build -f Dockerfile.small -t comput3ai/ollama:small .

# Print completion message
echo "All builds completed successfully!"
