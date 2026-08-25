from typing import Generic, TypeVar
from pydantic import BaseModel, Field

from dto.common.error_dto import ErrorDto


T = TypeVar("T")


class ResultOutDto(BaseModel, Generic[T]):
    status_code: int = 200
    error: list[ErrorDto] = Field(default_factory=list)
    hasError: bool = False
    data: T | list[T] | None = None
