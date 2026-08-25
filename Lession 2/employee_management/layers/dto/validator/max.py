from functools import wraps
from typing import Any, Callable

from pydantic_core import PydanticCustomError


ValidatorFunc = Callable[..., Any]


def Max(max_value: int | float):
    def decorator(func: ValidatorFunc) -> ValidatorFunc:
        @wraps(func)
        def wrapper(cls, value, info):
            if value is not None and value > max_value:
                raise PydanticCustomError(
                    "max",
                    f"{info.field_name} must be less than or equal to {max_value}",
                )

            return func(cls, value, info)

        return wrapper

    return decorator
