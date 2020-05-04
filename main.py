import sys
from db import Database
from db_schema import CREATE_USERS
from index_view import welcome


class Application:
    @classmethod
    def build(cls):
        db = Database()
        db.cursor.execute()

        db.connection.commit()
        db.connection.close()

    @classmethod
    def start(cls):
        welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
 