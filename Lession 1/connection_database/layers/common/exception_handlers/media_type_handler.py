from aws_lambda_powertools import Logger

from dto.common.error_dto import ErrorDto
from common.exception_handlers.base_response import build_error_response


logger = Logger()


def handle_unsupported_media_type(ex: NotImplementedError):
    logger.error("NotImplementedError caught", exc_info=True)
    error_msg = str(ex) or "Only JSON body is supported"
    errors = [ErrorDto(errorCode=4150, message=error_msg)]
    return build_error_response(errors=errors, logic_status_code=415)