from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity


class UsersRepository:

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
    