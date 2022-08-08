import sys
import pandas as pd
from setting import CONNECTION

# ------------------------------------------------------------------
sys.stderr.write("*** 開始 ***\n")

df=pd.read_sql_query('SELECT * FROM test WHERE ID = CNN CONNECTION', CONNECTION)

print(df.head())
#
CONNECTION.close()

sys.stderr.write("*** 終了 ***\n")
# ------------------------------------------------------------------