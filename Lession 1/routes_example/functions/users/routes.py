from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.event_handler.exceptions import NotFoundError

router = Router()

# free sample
USERS = [
    {"user_cd": "0001", "name": "Nguyen Van A", "email": "a.nguyen@example.com"},
    {"user_cd": "0002", "name": "Tran Thi B", "email": "b.tran@example.com"},
    {"user_cd": "0003", "name": "Le Van C", "email": "c.le@example.com"},
]


@router.get("/users")
def get_all_users():
    return {"data": USERS, "total": len(USERS)}


@router.get("/users/<user_cd>")
def get_user_by_cd(user_cd: str):
    user = next((u for u in USERS if u["user_cd"] == user_cd), None)
    if not user:
        raise NotFoundError(f"User '{user_cd}' not found")
    return {"data": user}
