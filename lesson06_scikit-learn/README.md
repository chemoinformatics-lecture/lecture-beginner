# なぜ


# どのように


# 何をするか
scikit-learnは、Pythonの機械学習ライブラリです。
「サイキット・ラーン」と読みます。
scikit-learnはオープンソース（BSD license）で公開されており、個人／商用問わず、誰でも無料で利用することができます。

# 講義動画

https://vimeo.com/showcase/8867477

# コードや行っていること

1. test データとtraining データの分割
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 10)
```

2. modelの選定と学習
```
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(max_depth = 100, n_estimators = 500, n_jobs = -1, random_state = 100)
model.fit(X_train, y_train)
```
fitで学習
モデルの選定で何を選べるかは、[公式ドキュメント](https://scikit-learn.org/stable/modules/classes.html)を参照

3. 精度の確認, メトリクス(metrics)

```
metrics.mean_absolute_error(y_true, y_pred, *)
metrics.mean_squared_error(y_true, y_pred, *)
metrics.mean_absolute_percentage_error(...)
metrics.r2_score(y_true, y_pred, *[, ...])
```

https://scikit-learn.org/stable/modules/classes.html#regression-metrics

4. 未知データの予測
`model.predict(X_test)`

