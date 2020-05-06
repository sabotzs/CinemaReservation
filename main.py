import sys
from db_schema import *
from index_view import *


class Application:
    @classmethod
    def build(cls):
        db = Database()

        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_PROJECTIONS)
        db.cursor.execute(CREATE_RESERVATIONS)

        db.connection.commit()
        db.connection.close()

    @classmethod
    def update_info(cls):
        db = Database()
        db.cursor.execute(INSERT_MOVIES)
        db.cursor.execute(INSERT_PROJECTIONS)
        db.cursor.execute(INSERT_RESERVATIONS)

        db.connection.commit()
        db.connection.close()

    @classmethod
    def start(cls):
        # login()
        welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    elif command == 'update':
        Application.update_info()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
