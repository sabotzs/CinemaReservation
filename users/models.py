import re
from db_schema import Database
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserModel:
    def __init__(self, *, user_id, email, password):
        self.id = user_id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        if not (re.search(regex, email)):
            raise ValueError("Wrong email! ")
        else:
            fetched = UserModel.email_exists(email)
            if fetched is not None:
                raise ValueError("Email already exists! ")
        # TODO: validate password

    @staticmethod
    def email_exists(email):
        db = Database()
        check_unique_email_query = '''
            SELECT id, email, password, salt
                FROM users
                WHERE email = ?;
        '''
        db.cursor.execute(check_unique_email_query, (email,))
        fetched = db.cursor.fetchone()
        db.connection.commit()
        db.connection.close()
        return fetched
