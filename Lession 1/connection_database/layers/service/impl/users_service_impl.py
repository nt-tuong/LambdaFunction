from service.users_service import UsersService
from dao.users_dao import UsersDao


class UsersServiceImpl(UsersService):
    def __init__(self, users_dao: UsersDao):
        self.users_dao = users_dao

    def get_all_user(self):
        # convert to json data
        users = self.users_dao.get_all_user()
        print("-------------------- [START] users --------------------")
        print(users)
        print("convert to json data")
        print([user.to_dict() for user in users])
        print("-------------------- [END] users --------------------")
        return [user.to_dict() for user in users]
