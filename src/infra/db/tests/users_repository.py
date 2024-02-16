from typing import List
from src.domain.models.users import Users

class UsersRepositorySpy():
    def __init__(self) -> None:
        self.insert_user_params = {}
        self.select_users_params = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_params["first_name"] = first_name
        self.insert_user_params["last_name"] = last_name
        self.insert_user_params["age"] = age

    def select_users(self, first_name: str) -> List[Users]:
        self.select_users_params['first_name'] = first_name
        return [
            Users(23, first_name, 'last_name', 43),
            Users(44, first_name, 'last_name', 43),
            Users(32, first_name, 'last_name', 42),
            Users(21, first_name, 'last_name', 43),
        ]
