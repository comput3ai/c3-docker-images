# C3 Docker Images

This repository contains optimized Docker images for various AI/ML tools and frameworks used at Comput3. Our goal is to provide pre-configured, production-ready containers that reduce deployment time and ensure consistent environments across our infrastructure.

## Current Optimizations

### Ollama

Located in `/ollama`, this directory contains three variants of Ollama images with pre-loaded models:

- `comput3ai/ollama:large` - Full suite of models for comprehensive AI capabilities
- `comput3ai/ollama:medium` - Balanced selection of models for general use
- `comput3ai/ollama:small` - Minimal set of models for lightweight deployments

To build these images locally:

```bash
cd ollama
chmod +x build.sh
./build.sh
```

## Image Details

All images are hosted on GitHub Container Registry (ghcr.io) under the `comput3ai` organization.

### Version Tagging

- `latest` - Points to the most recent stable build
- `large` - Full version with all models
- `medium` - Mid-sized version with selected models
- `small` - Minimal version with essential models

## Contributing

This is an ongoing optimization effort. If you have suggestions for improvements or want to contribute additional optimizations, please feel free to open an issue or submit a pull request.

## License

This repository is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

### Model Licenses

The pre-loaded models in our Docker images are subject to their respective upstream licenses. Please refer to each model's original source for specific licensing terms and conditions.

## Support

For questions and support, please open an issue in this repository.
