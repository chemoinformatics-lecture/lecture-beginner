# なぜ
効率よく学習モデルを見つける

# どのように
今までの復習をしながら、予測をしてみる。

# 何をするか
automlについて学ぶ

# automlについての比較

- いろいろなautomlの比較については以下を参照

https://atmarkit.itmedia.co.jp/ait/articles/2203/24/news004.html

今回は3つだけ紹介

# 1. pycaret
https://github.com/pycaret/pycaret

2022/08/08　現在　
github star 6100, fork 1400

- 無料で使用できるautomlの中で人気が高い
- データ分析の全工程でコードの行数を削減
- 環境構築で躓いたり、エラーがでたりすることも多い
- 学習コストが低く、扱いやすい
- 元々は、[Moez Ali](https://ca.linkedin.com/in/profile-moez)氏という天才が１人で作成
- 

### インストール方法

```
conda install -c conda-forge pycaret
conda install -c conda-forge scikit-learn==0.23.2 --force-reinstall
conda install -c conda-forge scikit-plot
```
そのままインストールするとエラーが出るので、scikit-learnのバージョンを落とす

lightGBM周りのエラーとlibompのインストール(mac)

`brew install libomp`

### 簡単な使い方とできること
|モジュール|	インポート方法|
| ---- | ---- |
|分類	|pycaret.classification|
|回帰	|pycaret.regression|
|クラスタリング|pycaret.clustering|
|異常検出|pycaret.anomaly|
|自然言語処理|pycaret.nlp|
|アソシエーション分析|pycaret.arules|

0. モジュールの呼び出し: from pycaret.classification import *
1. データの前処理： setup()
2. モデルの比較： compare_models()
3. 分析モデルの生成： create_model()
4. チューニング： tune_model()
5. 可視化： plot_model()
6. 評価： evaluate_model()
7. 予測： finalize_model(), predict_model()

### 参考サイト
- [pycaret official quickstart](https://pycaret.gitbook.io/docs/get-started/quickstart)
- [最速でPyCaretを使ってみた](https://qiita.com/s_fukuzawa/items/5dd40a008dac76595eea)
- [【機械学習】Pycaretでモデル比較が爆速化！？インストール方法〜可視化まで](https://qiita.com/G-Rape/items/53c7ef16a259cac487fe)
- [PyCaretの初心者向けまとめ（分類編）](https://qiita.com/shuhigashi/items/cb6816a1da1d347bbdc2)

# 2.evalml 
https://github.com/alteryx/evalml

2022/08/08　現在　
github star 520, fork 70

- sklearnに慣れている人ならば、学習コストが低く扱いやすい
- Alteryxが開発。Alteryxは、カリフォルニア州アーバインに本拠を置くアメリカのコンピューターソフトウェア企業

### インストール方法
```
conda install -c anaconda seaborn
conda install scikit-learn
conda install -c conda-forge evalml
```

### 使い方
0. データの前処理は、sklearnなどを用いる。

1. モデルの作成

automl = AutoMLSearch(X_train=X_train, y_train=y_train, problem_type='regression', objective='root mean squared error', 
                      additional_objectives=['mae', 'r2'], max_iterations=100, ensembling=True, 
                      random_seed=41, n_jobs=-1, verbose=True)
automl.search()

2. モデルの比較

automl.rankings

3. モデルの詳細の確認

automl.describe_pipeline(automl.rankings.iloc[0]["id"])

4. 推論

y_pred = best_model.predict(x_test)


### 参考サイト
- [AutoML（EvalML）を使ってみた](https://qiita.com/DS27/items/5f92599ddd3026817f33)


# 3. autokeras
https://github.com/keras-team/autokeras

2022/08/08　現在　
github star 8600, fork 1400

- Pythonのニューラルネットワーク構築のフレームワークKerasをもとに開発されているAutoMLのツール
- Efficitent Neural Architecture Search（ENAS）によるニューラルネットワークの構造設計
- マルチモーダル＆マルチタスクにも対応
-  DATA Lab at Texas A&M University　が開発