
from abc import ABC, abstractmethod
from database.tables.users import Users
from typing import List


# Interface
class UsersDao(ABC):
    @abstractmethod
    def get_all_user(self) -> List[Users]:
        pass
