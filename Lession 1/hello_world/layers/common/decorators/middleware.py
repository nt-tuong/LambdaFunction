from aws_lambda_powertools.middleware_factory import lambda_handler_decorator

@lambda_handler_decorator(trace_execution=True)
def middleware_custom(handler, event, context):
    try:
        # TODO Implement logic here,
        print("Middleware logic executed before the handler")
        pass
        
    except Exception as e:
        raise e
    finally:
        return handler(event, context)