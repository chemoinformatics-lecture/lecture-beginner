from sqlalchemy.orm import sessionmaker
from setting import ENGINE

# セッション作成
SessionClass = sessionmaker(ENGINE)
session = SessionClass()

# SELECT
ids = session.query(User.tweet_id).all()

# DataFrameに変換
df = pd.DataFrame(ids)