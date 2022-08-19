# なぜ
少ないデータを用いてデータを予測することは難しいことが知られています。
これを解決する手段の1つとして、転移学習やファインチューニングという手法がしられています。
転移学習は，ある学習領域(ドメイン)で事前学習 させたモデルを別の領域に適応させることで，通常よ りも少ないデータ量で効率よく学習を行えるとされる

論文がアクセプトされたら、作成予定です。

# どのように


# 何をするか


# 参考プログラム

https://github.com/poclab-web/fine-tuning-horac

# 参考資料

https://www.jstage.jst.go.jp/article/jnns/28/1/28_28/_pdf/-char/ja

https://www.slideshare.net/itakigawa/20209-238434263

https://www.cerpo.t.u-tokyo.ac.jp/news/upload/e55149bd64baae8eaff3d7f04c31bf4eb7716a10.pdf

https://datachemeng.com/transfer_learning/

# その他の方法

- synthetic minority oversampling technique (SMOTE). <br>
データ不足の問題に陥らないデータレベルのアプローチ法として Oversampling があります。 Oversampling の代表的な手法として良く知られているのが SMOTE (Synthetic Minority Oversampling TEchnique) です。 SMOTE は、少ない方のラベルが付いた各データ点同士を線でつなぎ、その線分上の任意の点をランダムに人工データとして生成する手法。拡張版が数多く提案されている。