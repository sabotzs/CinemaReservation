import re
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
            pass

