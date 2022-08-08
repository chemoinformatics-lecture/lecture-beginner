import sys
import pandas as pd
from setting import CONNECTION

sys.stderr.write("*** 開始 ***\n")

# データの読み込み
df = pd.read_csv('data/output.csv')
# SQLへの書き込み
df.to_sql('test',CONNECTION,if_exists='append',index=None)
# SQLの接続をクローズ
CONNECTION.close()

sys.stderr.write("*** 終了 ***\n")
# ------------------------------------------------------------------