# なぜ
先人たちの知恵を借りて、名前から簡単な化学的な情報へと変換する

# どのように
これまでに非常に多くの化合物が単離または合成されており、その化学的性質に関する膨大な知見が蓄積されている。
これら化合物の情報を一カ所に集めたものが化学データベースです。
このデータベースにアクセスすることで、先人たちの知恵を借りることができる。
データベースの中には、pythonで処理することができるものも用意されており大量のデータも処理しやすい。

# 講義動画
https://vimeo.com/showcase/8854108

# 何をするか
pubchem及びpubchempyを使って化合物の検索ダウンロードを学ぶ。

## pubchem
アメリカのNIH傘下のNCBIによって2004年に管理・運営が開始された化合物データベースで，原子数1000以下かつ1000結合以下の比較的小さな分子が収録されている。

https://pubchem.ncbi.nlm.nih.gov/

## pubchempy
PubChemデータベースにpythonからアクセスするためのライブラリがPubChemPyです．上述の3つのデータベースにアクセスする方法と，取得したエントリーから物性などの様々な性質を取り出す方法が実装されてい

https://pubchempy.readthedocs.io/en/latest/

## コード

- ライブラリーの呼び出し (pcpと略すことが多い)

`import pubchempy as pcp`

- 化合物の検索

`compounds = pcp.get_compounds('化合物の名前', 'name')`

- 1つの化合物の名前で複数のデータを確認する。
```
compound = "alanine"
properties = ['iupacname', 'molecularformula', 'molecularweight', 'canonicalsmiles']
pcp.get_properties(properties, compound, 'name', as_dataframe=True)
```

# 他の方法
- ChemSpider <br>
http://www.chemspider.com/

解説記事 <br>
https://future-chem.com/chem-spi-py/

- CAS Common Chemistry 

CAS番号や名前を入れると化合物を取得できる。
https://commonchemistry.cas.org/

「CAS Common Chemistryは、化学情報にアクセスするためのオープンなコミュニティリソース。

CAS REGISTRY®に登録されている約50万種類の化学物質は、一般的な化学物質や頻繁に規制される化学物質、高校や学部の化学の授業に関連する化学物質など、コミュニティの関心事をカバーしている。

この化学情報は、アメリカ化学会の一部門として、専門科学者の監修のもと、提供されている。」

後ろのcas番号を変更すれば、化合物の情報に直接アクセスできる。

https://commonchemistry.cas.org/detail?cas_rn=67-64-1