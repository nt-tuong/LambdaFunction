from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger
from routes import router

from common.decorators.middleware import middleware_custom
from common.exception_handlers import register_exception_handlers


logger = Logger(service="users")
app = APIGatewayRestResolver()
app.include_router(router, prefix="/api/v1")


register_exception_handlers(app)


@logger.inject_lambda_context
@middleware_custom
def lambda_handler(event, context):
    return app.resolve(event, context)
