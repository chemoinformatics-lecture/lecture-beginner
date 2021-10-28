# なぜ
データを整理することで、

# どのように
データの整理方法として、pythonでの

# 何をするか
主にpandasの処理です。

**① Pythonのバージョン確認、モジュールのimport、データの読み込み**

- pd.read_csv()
- df.head()
- df.tail()
- df.sample()

**② 簡単にデータの状態を確認する（行数列数カウント・データの選択的表示・重複の有無など）**

- df.shape()
- df.columns
- df.describe()

**③ データの処理(map）**

- df.set_index()
- df.rename()
- df.sort_values()
- df.to_datetime()
- df.sort_index()
- df.resample()
- df.apply()
- pd.cut()

**④ データの欠損状態の確認** 

- df.isnull()
- df.any()

**⑤ 値（欠損）の置き換えや削除**

- df.fillna()
- df.dropna()
- df.replace()
- df.mask()
- df.drop()

**⑥ 集計**

- df.value_counts()
- df.groupby()
- df.diff()
- df.rolling()
- df.pct_change()

**⑦ 可視化**

- df.plot()

**⑧ 変数の前処理**

- pd.get_dummies()

**⑨ 最後に、出来たデータをもう一度眺める**

- df.to_csv()

## エラーの見方を学ぶ。
https://docs.python.org/ja/3.8/library/exceptions.html