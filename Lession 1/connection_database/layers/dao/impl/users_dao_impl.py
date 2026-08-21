from database.database_manager import get_session
from dao.users_dao import UsersDao
from database.tables.users import Users
from typing import List


class UsersDaoImpl(UsersDao):
    def __init__(self):
        session = get_session()
        self.session = session


    def get_all_user(self) -> List[Users]:
        return self.session.query(Users).all()
    