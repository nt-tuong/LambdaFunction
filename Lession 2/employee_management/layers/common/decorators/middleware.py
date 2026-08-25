from http import HTTPStatus
from aws_lambda_powertools import Logger
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator

import json

from dto.common.response_factory import ResponseFactory
from dto.common.result_out_dto import ResultOutDto


logger = Logger()


@lambda_handler_decorator(trace_execution=True)
def middleware_custom(handler, event, context):
    response = handler(event, context)

    if isinstance(response, dict) and "body" in response:
        raw_body = response.get("body")
        if isinstance(raw_body, str):
            try:
                data_payload = json.loads(raw_body)
            except json.JSONDecodeError:
                data_payload = raw_body
        else:
            data_payload = raw_body

        if isinstance(data_payload, dict) and "hasError" in data_payload:
            final_body = data_payload
        else:
            final_body = ResponseFactory.success(data=data_payload).model_dump()

        response["statusCode"] = HTTPStatus.OK
        response["body"] = json.dumps(final_body, ensure_ascii=False)
        return response

    if isinstance(response, ResultOutDto):
        final_body = response.model_dump()
    else:
        final_body = ResponseFactory.success(data=response).model_dump()

    return {
        "statusCode": HTTPStatus.OK,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps(final_body, ensure_ascii=False)
    }
