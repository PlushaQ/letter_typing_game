import sqlite3
from typing import List, Tuple


class DatabaseConnection:
    def __init__(self, host: str):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


class Database:
    def __init__(self):
        with DatabaseConnection('scoreboard.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS scoreboard (score INT)')

    @staticmethod
    def add_record(score):
        with DatabaseConnection('scoreboard.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO scoreboard VALUES (?)', (score,))

    @staticmethod
    def get_top_five() -> List[Tuple[int]]:
        with DatabaseConnection('scoreboard.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT score FROM scoreboard ORDER BY score DESC LIMIT 5")
            top_five = cursor.fetchall()
        return top_five
