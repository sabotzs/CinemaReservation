import unittest
from users.users_gateway import create, validate_pass, validate_email


class TestCreateUser(unittest.TestCase):
    def test_pass_without_upper_letters(self):
        exc = None
        password = "password"
        email = "boss@abv.bg"
        try:
            create(email=email, password=password)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)

    def test_validate_email(self):
        exc = None
        password = "password"
        email = "bossabv.bg"
        try:
            create(email=email, password=password)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)



if __name__ == '__main__':
    unittest.main()