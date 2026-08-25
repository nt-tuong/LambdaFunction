from functools import wraps
from aws_lambda_powertools import Logger
from sqlalchemy.orm import Session

from database.database_manager import get_session


logger = Logger()


def session_scope(handler):
    @wraps(handler)
    def wrapper(event, context, *args, **kwargs):
        session: Session = get_session()
        try:
            result = handler(
                event,
                context,
                *args,
                **kwargs,
            )
            # session.commit()

            return result

        finally:
            session.close_all()

    return wrapper
