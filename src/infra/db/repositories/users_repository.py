from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from typing import List

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_registry = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                db_connection.session.add(new_registry)
                db_connection.session.commit()
            except Exception as exception:
                db_connection.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, fisrt_name: str) -> List[Users]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session
                    .query(UsersEntity)
                    .filter_by(
                        first_name = fisrt_name
                    ).all()
                )
                return data
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
