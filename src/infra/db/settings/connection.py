from sqlalchemy import create_engine
class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = '{}://{}:{}@{}:{}/{}'.format(
            'mysql+pymysql',
            'root',
            'root',
            '192.168.15.7',
            '3388',
            'clean_database'
        )
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        return create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine
