#!/bin/bash

# Build large version
echo "Building large version..."
docker build -f Dockerfile.large -t comput3ai/ollama:large .

# Build medium version
echo "Building medium version..."
docker build -f Dockerfile.medium -t comput3ai/ollama:medium .

# Build small version
echo "Building small version..."
docker build -f Dockerfile.small -t comput3ai/ollama:small .

# Print completion message
echo "All builds completed successfully!"
