# .github/prompts Directory

This directory is a special VS Code workspace feature that contains custom instructions for GitHub
Copilot. Any markdown (`.md`) files placed here will be used by Copilot to understand
workspace-specific requirements when generating code suggestions.

## Purpose

The `.github/prompts` directory helps you:

- Customize Copilot's behavior for this specific workspace
- Define project-specific coding patterns and conventions
- Share standardized instructions across team members
- Maintain consistency in generated code

## Usage

1. Create `.md` files in this directory with your instructions
2. Each file should focus on specific aspects (e.g., style, architecture, testing)
3. Instructions will be applied to Copilot's suggestions in this workspace
4. Changes take effect immediately when files are saved

## Example Structure

```zsh
.github/prompts/
├── README.md         # Directory explanation (this file)
├── style-guide.md    # Coding style instructions
├── architecture.md   # Project structure guidelines
└── testing.md       # Testing requirements
```

## Example Usage

Here's an example of how to use workspace-specific instructions for Python development:

Create a file named `python-guidelines.md` in this directory:

````markdown
# Python Development Guidelines

When writing Python code in this workspace:

## Code Style

- Use type hints for all function parameters and return types
- Follow PEP 8 naming conventions

  - snake_case for functions and variables
  - PascalCase for classes

- Use type hints for all function parameters and return types
- Follow PEP 8 naming conventions

  - `snake_case` for functions and variables
  - PascalCase for classes

- Use meaningful variable names that describe their purpose

## Error Handling

- Use specific exception types instead of bare except
- Include error messages that aid debugging
- Log exceptions with appropriate logging levels

## Example Pattern

```python

from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

def process_data(items: List[str]) -> Optional[str]:
    try:
        return next(item for item in items if item.startswith('valid_'))
    except StopIteration:
        logger.warning("No valid items found in the list")
        return None
    except Exception as e:
        logger.error(f"Unexpected error processing items: {e}")
        raise
```
````

<!-- close markdown  -->

## Learn More

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Configuration](https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment)
