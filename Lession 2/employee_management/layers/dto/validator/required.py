from functools import wraps
from typing import Any, Callable


def Required(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Marker for a required field.

    Missing fields are handled by Pydantic via Field(...).
    This decorator is kept for consistency with other validators.
    """
    @wraps(func)
    def wrapper(cls, value, info):
        return func(cls, value, info)

    return wrapper