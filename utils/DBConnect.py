import os
import sqlite3
import sqlite3 as sql
from os import PathLike
from sqlite3 import Cursor, Connection


class DBConnect:
    @staticmethod
    def get_db(database: str | bytes | PathLike[str] | PathLike[bytes]) -> Connection | Exception:
        try:
            if os.path.exists(database):
                return sqlite3.connect(database)
            else:
                raise FileNotFoundError("Файл базы данных не найден.")
        except Exception as e:
            return e
