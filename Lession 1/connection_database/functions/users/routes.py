from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.event_handler.exceptions import NotFoundError

from dao.impl.users_dao_impl import UsersDaoImpl
from service.impl.users_service_impl import UsersServiceImpl

router = Router()


# free sample
USERS = [
    {"user_cd": "0001", "name": "Nguyen Van A", "email": "a.nguyen@example.com"},
    {"user_cd": "0002", "name": "Tran Thi B", "email": "b.tran@example.com"},
    {"user_cd": "0003", "name": "Le Van C", "email": "c.le@example.com"},
]


user_dao = UsersDaoImpl()
user_service = UsersServiceImpl(user_dao)


@router.get("/users")
def get_all_users():
    users = user_service.get_all_user()
    print("-------------------- [START] users Routes --------------------")
    print(users)
    print("-------------------- [END] users Routes --------------------")
    return {"data": users, "total": len(users)}


@router.get("/users/<user_cd>")
def get_user_by_cd(user_cd: str):
    user = next((u for u in USERS if u["user_cd"] == user_cd), None)
    if not user:
        raise NotFoundError(f"User '{user_cd}' not found")
    return {"data": user}
