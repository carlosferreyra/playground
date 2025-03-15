# Code Playground

A multi-language playground repository for testing and experimenting with different programming
languages, features, and tech stacks.

## Structure

This repository is organized to accommodate multiple programming languages and their respective
package managers:

### Java (Maven)

- Located in `java/` directory
- Uses Maven for dependency management
- Standard Maven project structure

### Python (uv)

- Located in `python/` directory
- Uses uv for dependency management
- Modern Python packaging and virtual environment management

### JavaScript/TypeScript (npm/bun)

- Located in `js/` and `ts/` directories
- Supports both npm and bun package managers
- Includes TypeScript configuration

## Getting Started

### Prerequisites

- Java JDK 11 or higher
- Maven 3.6+
- Python 3.8+
- uv package manager
- Node.js 18+ and npm
- Bun runtime

### Java Setup

```bash
mvn clean install
```

### Python Setup

```bash
uv venv
uv pip install -r requirements.txt
```

### JavaScript/TypeScript Setup

```bash
# Using npm
npm install

# Using bun
bun install
```

## Usage

This repository is meant for:

- Testing new language features
- Experimenting with different frameworks and libraries
- Learning and comparing different tech stacks
- Prototyping ideas
- Benchmarking different implementations

## Contributing

Feel free to create new directories for different experiments. Keep the code organized and
documented.

## License

This project is open source and available under the MIT License.
