import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("sqlite:///test_db.sqlite3")

SessionClass = sessionmaker(bind=engine)
session = SessionClass()