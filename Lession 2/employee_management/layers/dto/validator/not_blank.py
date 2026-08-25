from functools import wraps
from typing import Any, Callable

from pydantic_core import PydanticCustomError


ValidatorFunc = Callable[..., Any]


def NotBlank(func: ValidatorFunc) -> ValidatorFunc:
    @wraps(func)
    def wrapper(cls, value, info):
        if value is None:
            raise PydanticCustomError(
                "not_blank",
                f"{info.field_name} must not be blank",
            )

        if isinstance(value, str) and not value.strip():
            raise PydanticCustomError(
                "not_blank",
                f"{info.field_name} must not be blank",
            )

        return func(cls, value, info)

    return wrapper
