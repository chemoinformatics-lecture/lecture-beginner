from sqlalchemy import create_engine
import sqlite3

db = sqlite3.connect(
    "test.db",              #ファイル名
    isolation_level=None,
)

engine = create_engine('sqlite:///test.db')

print(db)