import json
from common.decorators.middleware import middleware_custom

@middleware_custom
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, World!",
            # "location": ip.text.replace("\n", "")
        }),
    }
