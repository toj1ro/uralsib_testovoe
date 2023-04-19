import sqlite3
import sys
from sqlite3 import Connection, Cursor
from typing import Any, Optional


class DataBase:
    def __init__(self, db_name: str):
        self.conn: Optional[Connection] = None
        self.cur: Optional[Cursor] = None
        self.db_name = db_name

    def __enter__(self) -> Any:
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        try:
            self.conn.close()
        except Exception as e:
            print(f"Close connection fail, message:{e}")

    def execute_query(self, query: str, data: list[Any]) -> None:
        try:
            self.cur.executemany(query, data)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f"Query fail, message: {e}")
