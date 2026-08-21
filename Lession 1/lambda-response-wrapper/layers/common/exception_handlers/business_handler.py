from aws_lambda_powertools import Logger

from dto.common.error_dto import ErrorDto
from common.exception_handlers.base_response import build_error_response


logger = Logger()


class BusinessException(Exception):
    def __init__(self, error_code: int, message: str, status_code: int = 400):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code

def handle_business_exception(ex: BusinessException):
    logger.warning(f"Business exception: {ex.message}", extra={"errorCode": ex.status_code})
    errors = [ErrorDto(message=ex.message)]
    return build_error_response(errors=errors, logic_status_code=ex.status_code)