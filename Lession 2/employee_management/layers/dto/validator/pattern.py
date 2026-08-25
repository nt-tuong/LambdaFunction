from functools import wraps
from typing import Any, Callable

from pydantic_core import PydanticCustomError


ValidatorFunc = Callable[..., Any]


def Pattern(pattern: str):
    import re

    compiled_pattern = re.compile(pattern)

    def decorator(func: ValidatorFunc) -> ValidatorFunc:
        @wraps(func)
        def wrapper(cls, value, info):
            if value is not None:
                if not isinstance(value, str):
                    raise PydanticCustomError(
                        "pattern",
                        f"{info.field_name} must be a string",
                    )

                if not compiled_pattern.fullmatch(value):
                    raise PydanticCustomError(
                        "pattern",
                        f"{info.field_name} has invalid format",
                    )

            return func(cls, value, info)

        return wrapper

    return decorator
