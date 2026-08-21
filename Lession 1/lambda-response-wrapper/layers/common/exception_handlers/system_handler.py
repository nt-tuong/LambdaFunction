from http import HTTPStatus
from aws_lambda_powertools import Logger

from dto.common.error_dto import ErrorDto
from common.exception_handlers.base_response import build_error_response


logger = Logger()


def handle_system_exception(ex: Exception):
    logger.error(f"Unhandled System Error: {str(ex)}", exc_info=True)
    errors = [ErrorDto(message=f"Internal Server Error: {str(ex)}")]
    return build_error_response(errors=errors, logic_status_code=HTTPStatus.INTERNAL_SERVER_ERROR)