import sys
from db_schema import *
from view import *


class Application:
    @classmethod
    def build(cls):
        db = Database()

        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_PROJECTIONS)
        db.cursor.execute(CREATE_RESERVATIONS)
        db.cursor.execute(CREATE_ADMINS)
        db.cursor.execute(CREATE_CLIENTS)

        db.connection.commit()
        db.connection.close()

    @classmethod
    def admin(cls):
        create_super_admin()

    @classmethod
    def admin_view(cls):
        super_admin_welcome()

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
        login()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
        Application.update_info()
        Application.admin()
    elif command == 'start':
        Application.start()
    elif command == 'super':
        Application.admin_view()
    else:
        raise ValueError(f'Unknown command {command}.')
