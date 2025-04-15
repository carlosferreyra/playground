# Existing code remains...

# Python 3.13 new features

# New f-string syntax for multiline expressions
long_expression = f"""{
    "hello"
    "world"
}"""

# New type parameter syntax with constraints (PEP 696)
from typing import TypeVar, SupportsFloat

T = TypeVar('T', bound=SupportsFloat)
def square[T: SupportsFloat](x: T) -> T:
    return x * x

# Enhanced error messages for TypeErrors
try:
    x: int = "not an int"  # More detailed type error messages in 3.13
except TypeError as e:
    print(e)

# Performance improvements for dict operations
# (No syntax changes, but dictionaries are more efficient in 3.13)
d = {"key": "value"}

# New asyncio features
import asyncio

async def example():
    # Enhanced task groups and cancellation handling
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(asyncio.sleep(1))
