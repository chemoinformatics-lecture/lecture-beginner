# なぜ

プログラミングを学ぶことで、以下のことも身に付けられます。

1. 論理的な思考法が身に付く

2. 退屈な作業をパソコンに命令して行わせることができる
   
3. 世界とつながることができる
   
4. 先人たちの知恵を借りることができる

5. 考え方や考えたことを記録しておける

# どのように

環境作成の便利なツールを使い、効率的にコードを書くツールを使って、書いたコードを管理する共有する便利なツールも使う。

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