# Python Development Guidelines

When writing Python code in this workspace:

## Code Style

- Use type hints for all function parameters and return types
- Follow PEP 8 naming conventions
  - snake_case for functions and variables
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
