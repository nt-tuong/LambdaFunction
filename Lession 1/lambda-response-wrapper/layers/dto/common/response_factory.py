from http import HTTPStatus
from typing import List, TypeVar
from dto.common.result_out_dto import ResultOutDto
from dto.common.error_dto import ErrorDto
    

T = TypeVar("T")


class ResponseFactory:
    @staticmethod
    def success(data: T = None) -> ResultOutDto[T]:
        return ResultOutDto(
            status_code=HTTPStatus.OK,
            error=[],
            hasError=False,
            data=data
        )

    @staticmethod
    def error(errors: List[ErrorDto], logic_status_code: int = HTTPStatus.BAD_REQUEST, data: T = None) -> ResultOutDto[T]:
        return ResultOutDto(
            status_code=logic_status_code,
            error=errors,
            hasError=logic_status_code != HTTPStatus.OK,
            data=data
        )