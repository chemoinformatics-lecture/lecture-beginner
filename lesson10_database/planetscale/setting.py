from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
import os

# .envファイルを作成して、そこに情報を書き込んでいる必要がある。

HOST = os.getenv("HOST")
USER = os.getenv("USERNAME")
PASSWD = os.getenv("PASSWORD")
DB = os.getenv("DATABASE")

# データベース接続
ENGINE = create_engine(
    f"mysql://{USER}:{PASSWD}@{HOST}/{DB}?ssl_mode=VERIFY_IDENTITY",
    connect_args={"ssl": {"ca": "/etc/ssl/cert.pem"}},
)
session = scoped_session(sessionmaker(bind=ENGINE))

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()

