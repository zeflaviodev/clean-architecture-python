from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpNotFoundError, HttpBadRequestError

class UserFinder(UserFinderInterface):
    def __init__(self, user_repository: UsersRepositoryInterface):
        self.__users_repository = user_repository

    def find(self, first_name: str) -> Dict :
        self.__validate_name(first_name)

        users = self.__search_user(first_name)

        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError('Nome invalido para a busca')

        if len(first_name) > 18 :
            raise HttpBadRequestError('Nome muito grande para a busca')

    def __search_user(self, first_name: str) -> List[Users]:

        users = self.__users_repository.select_users(first_name)
        if not users: raise HttpNotFoundError('Nenhum usuario encontrado')
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append(
                {"first_name": user.first_name, "age": user.age}
            )
        return {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
    