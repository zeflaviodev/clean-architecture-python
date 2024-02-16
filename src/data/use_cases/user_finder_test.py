from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = "Nome"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_users_params['first_name'] == first_name
    assert response['type'] == 'Users'
    assert response['count'] == len(response['attributes'])
    assert not response['attributes']

def test_find_fail_in_valid_name():
    first_name = "Nome123"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"

def test_find_fail_in_long_name():
    first_name = "asdasdasdasdasdasdasdasdassadasdasddasdsd"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome muito grande para a busca"

def test_find_fail_user_empty():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_users(self, first_name: str):
            return []

    first_name = "Nome"

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nenhum usuario encontrado"
