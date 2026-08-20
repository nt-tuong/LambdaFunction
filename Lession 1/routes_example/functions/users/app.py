from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import Logger
from routes import router

logger = Logger(service="users")
app = APIGatewayRestResolver()
app.include_router(router)


@logger.inject_lambda_context
def lambda_handler(event, context):
    return app.resolve(event, context)
