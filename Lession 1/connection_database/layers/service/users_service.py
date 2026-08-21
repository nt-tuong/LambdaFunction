from abc import ABC, abstractmethod


# Interface
class UsersService(ABC):
    @abstractmethod
    def get_all_user(self):
        pass