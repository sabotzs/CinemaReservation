import sys
from view import *
from users import create_users


class Application:
    @classmethod
    def build(cls):
        create_users()


    @classmethod
    def admin(cls):
        create_super_admin()

    @classmethod
    def admin_view(cls):
        super_admin_welcome()

    # @classmethod
    # def update_info(cls):
    #     db = Database()
    #     db.cursor.execute(INSERT_MOVIES)
    #     db.cursor.execute(INSERT_PROJECTIONS)
    #     db.cursor.execute(INSERT_RESERVATIONS)

    #     db.connection.commit()
    #     db.connection.close()

    @classmethod
    def start(cls):
        login()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':

        Application.build()
        Application.admin()
    elif command == 'start':
        Application.start()
    elif command == 'super':
        Application.admin_view()
    else:
        raise ValueError(f'Unknown command {command}.')
