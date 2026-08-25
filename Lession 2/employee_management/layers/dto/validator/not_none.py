from functools import wraps
from typing import Any, Callable

from pydantic_core import PydanticCustomError


ValidatorFunc = Callable[..., Any]


def NotNone(func: ValidatorFunc) -> ValidatorFunc:
    @wraps(func)
    def wrapper(cls, value, info):
        if value is None:
            raise PydanticCustomError(
                "not_none",
                f"{info.field_name} must not be none",
            )

        return func(cls, value, info)

    return wrapper
