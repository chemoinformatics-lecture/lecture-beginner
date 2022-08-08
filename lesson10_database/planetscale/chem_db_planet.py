from sqlalchemy import Column, String
from setting import Base, ENGINE

class User(Base):
    """
    ユーザモデル
    """

    __tablename__ = "test"
    user_id = Column("user_id", String(767), primary_key=True)
    data = Column("data", String(767))


def main():
    Base.metadata.create_all(ENGINE)


if __name__ == "__main__":
    main()