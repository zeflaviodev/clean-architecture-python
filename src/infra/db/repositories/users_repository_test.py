# from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 34

    user_repository = UsersRepository()
    user_repository.insert_user(
        first_name=mocked_first_name,
        last_name=mocked_last_name,
        age=mocked_age
    )
