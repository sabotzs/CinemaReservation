import unittest
import sys
sys.path.append('.')
from users import *
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


class TestCreateUser(unittest.TestCase):
    def test_pass_without_upper_letters(self):
        g = UserGateway()
        exc = None
        password = "password"
        email = "boss@abv.bg"
        try:
            g.create(email=email, password=password)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)

    def test_validate_email(self):
        g = UserGateway()
        exc = None
        password = "password"
        email = "bossabv.bg"
        try:
            g.create(email=email, password=password)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)

    def test_vaidate_movie_info_wrong_input(self):
        g = UserGateway()
        name = "The Shining"
        rating = "8.9"
        res = g.validate_movie_info(name, rating)
        self.assertEqual(res, False)

    def test_validate_movie_info_correct_input(self):
        g = UserGateway()
        name = "The shining"
        rating = 8.7
        res = g.validate_movie_info(name, rating)
        self.assertEqual(res, True)

    def test_unvalid_email_input(self):
        g = UserGateway()
        email = "joro.bg"
        res = g.validate_email(email)
        self.assertEqual(res, False)

    def test_valid_email_input(self):
        g = UserGateway()
        email = "joro@morski.bg"
        res = g.validate_email(email)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
