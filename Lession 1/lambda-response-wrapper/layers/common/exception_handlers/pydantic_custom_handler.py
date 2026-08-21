from aws_lambda_powertools import Logger
from pydantic_core import PydanticCustomError

from dto.common.error_dto import ErrorDto
from common.exception_handlers.base_response import build_error_response


logger = Logger()


def handle_pydantic_custom_error(ex: PydanticCustomError):
    logger.warning("Pydantic custom error caught", exc_info=True)
    error_type = ex.type.upper() if hasattr(ex, 'type') else 'CUSTOM_ERROR'
    error_msg = ex.message_template if hasattr(ex, 'message_template') else str(ex)
    
    errors = [ErrorDto(message=f"[{error_type}] {error_msg}")]
    return build_error_response(errors=errors, logic_status_code=400)