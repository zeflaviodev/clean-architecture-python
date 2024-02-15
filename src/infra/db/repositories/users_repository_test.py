import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
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

    sql = """
        SELECT
            *
        FROM 
            users 
        WHERE 
            first_name='{}' AND 
            last_name='{}' AND 
            age='{}'
    """.format(mocked_first_name, mocked_last_name, mocked_age)
    response = connection.execute(text(sql))
    data = response.fetchall()[0]

    assert data.first_name == mocked_first_name
    assert data.last_name == mocked_last_name
    assert data.age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id={data.id}
    '''))
    connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    mocked_first_name = "first_2"
    mocked_last_name = "last_2"
    mocked_age = 34

    user_repository = UsersRepository()
    user_repository.insert_user(
        first_name=mocked_first_name,
        last_name=mocked_last_name,
        age=mocked_age
    )

    response = user_repository.select_user(fisrt_name=mocked_first_name)

    data = response[0]

    assert data.first_name == mocked_first_name
    assert data.last_name == mocked_last_name
    assert data.age == mocked_age

    connection.execute(text(f'''
        DELETE FROM users WHERE id={data.id}
    '''))
    connection.commit()
