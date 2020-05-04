import re
from ..db import Database
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class UserModel:
    def __init__(self, *, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        if not (re.search(regex, email)):
            raise ValueError("Wrong email! ")
        else:
            db = Database()
            check_unique_email_query = '''
                SELECT email
                    FROM users
                    WHERE email = ?
            '''
            db.cursor.execute(check_unique_email_query, (email))
            fetched = db.cursor.fetchone()
            if fetched is not None:
                raise ValueError("Email already exists! ")
        # TODO: validate password
