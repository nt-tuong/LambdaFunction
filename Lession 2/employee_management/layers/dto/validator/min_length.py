from functools import wraps
from typing import Any, Callable

from pydantic_core import PydanticCustomError


ValidatorFunc = Callable[..., Any]


def MinLength(min_length: int):
    def decorator(func: ValidatorFunc) -> ValidatorFunc:
        @wraps(func)
        def wrapper(cls, value, info):
            if value is not None and len(value) < min_length:
                raise PydanticCustomError(
                    "min_length",
                    f"{info.field_name} must have at least {min_length} characters",
                )

            return func(cls, value, info)

        return wrapper

    return decorator
