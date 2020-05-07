import sqlite3
from .settings import DB_NAME


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
