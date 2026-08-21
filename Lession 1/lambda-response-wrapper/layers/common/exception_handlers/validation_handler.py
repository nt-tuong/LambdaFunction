from http import HTTPStatus

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.openapi.exceptions import RequestValidationError

from dto.common.error_dto import ErrorDto
from common.exception_handlers.base_response import build_error_response


logger = Logger()


def validation_exception_handler(ex: RequestValidationError):
    logger.warning("Request failed validation", exc_info=True)
    errors = [
        ErrorDto(message=f"Field '{'.'.join(map(str, err['loc']))}': {err['msg']}")
        for err in ex.errors()
    ]
    return build_error_response(errors=errors, logic_status_code=400)