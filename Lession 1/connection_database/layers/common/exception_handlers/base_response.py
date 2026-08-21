import json
from http import HTTPStatus
from typing import List, Dict, Any, Optional
from aws_lambda_powertools.event_handler import Response, content_types

from dto.common.error_dto import ErrorDto
from dto.common.response_factory import ResponseFactory 


def build_error_response(
    errors: List[ErrorDto], 
    logic_status_code: int, 
    request_headers: Optional[Dict[str, Any]] = None
) -> Response:
    """Tạo Response trả về cho Powertools với HTTP Status = 200 OK"""
    error_dto_response = ResponseFactory.error(
        errors=errors, 
        logic_status_code=logic_status_code
    ).model_dump()

    response_headers = {
        "Content-Type": content_types.APPLICATION_JSON,
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE"
    }

    if request_headers:
        normalized_headers = {k.lower(): v for k, v in request_headers.items() if isinstance(k, str)}
        origin = normalized_headers.get("origin")
        if origin:
            response_headers["Access-Control-Allow-Origin"] = origin
            response_headers["Vary"] = "Origin"

    return Response(
        status_code=HTTPStatus.OK,
        content_type=content_types.APPLICATION_JSON,
        headers=response_headers,
        body=json.dumps(error_dto_response, ensure_ascii=False)
    )
