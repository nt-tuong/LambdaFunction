from functools import wraps
from typing import Any, Callable

from pydantic_core import PydanticCustomError


ValidatorFunc = Callable[..., Any]


def _field_name(info) -> str:
    return info.field_name


def Min(min_value: int | float):
    def decorator(func: ValidatorFunc) -> ValidatorFunc:
        @wraps(func)
        def wrapper(cls, value, info):
            if value is not None and value < min_value:
                raise PydanticCustomError(
                    "min",
                    f"{_field_name(info)} must be greater than or equal to {min_value}",
                )

            return func(cls, value, info)

        return wrapper

    return decorator
