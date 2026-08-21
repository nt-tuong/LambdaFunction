from pydantic import BaseModel


class ErrorDto(BaseModel):
    errorCode: int
    message: str
