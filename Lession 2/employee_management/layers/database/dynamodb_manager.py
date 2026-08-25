import os
import boto3

_dynamodb_resource = None


def get_dynamodb_resource():
    global _dynamodb_resource
    if _dynamodb_resource is None:
        endpoint_url = os.environ.get("DYNAMODB_ENDPOINT_URL") or None
        _dynamodb_resource = boto3.resource(
            "dynamodb",
            region_name=os.environ.get("AWS_REGION", "ap-southeast-1"),
            endpoint_url=endpoint_url,
        )
    return _dynamodb_resource
