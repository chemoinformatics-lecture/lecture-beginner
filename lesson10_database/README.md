# なぜ
- データフレーム(pandasやエクセルなど)で扱えるデータ量には限界がある
- 多量のデータを処理するには、色々なデータベースに登録していくのが良い。
- web上のデータベースに登録するやり方を学ぶ

# どのように
- データベースの登録方法を学ぶ
- 簡単なSQL構文を学ぶ

# 何をするか
- ローカルのパソコンとWEB上のデータベースの操作を学ぶ
- データベースのCRUDができるようになる
- 無料で登録できるデータベースにデータの読み書きをしてみる

CRUDとは、永続的なデータを取り扱うソフトウェアに要求される4つの基本機能である、
データの作成（Create）、読み出し（Read）、更新（Update）、削除（Delete）の頭文字を繋げた語

# sql
SQLightでローカルのパソコンにデータを入力する。

```
conda install -c anaconda sqlalchemy
```
SQLiteは設定不要で利用することができる。
ほかのデータベースであれば、設定ファイルを用意して、プロセスの起動や停止、データベースインスタンスの設定が必要。

```
conda install -c conda-forge mysqlclient
```
が必要になる。

sqliteの簡単な操作方法

- 起動
`sqlite3 "DBのファイル名"`
- 終了
`sqlite> .quit `
- テーブル一覧
`sqlite> .table`
- データベース情報
`sqlite> .table`
- テーブルの中身を表示 (5行まで)
`sqlite> select * from table名 LIMIT 5;`
- テーブルの要素一覧
`sqlite> .schema`

# chemicalliteの使い方
ChemicaLite
ケモインフォマティクスアプリケーション用のSQLiteデータベース拡張。分子やフィンガープリントの保存、ディスクリプタの計算、化学データベース上での化学クエリの実行が可能。
https://chemicalite.readthedocs.io/en/latest/installation.html

# databaseに入れるデータ
eMoleculesは世界中の様々なサプライヤーのカタログ製品をまとめて検索できるプラットフォーム。
無料でダウンロードできるリストがある。
https://downloads.emolecules.com/

食品関係のデータベース
https://foodb.ca

# planetscaleを利用してオンラインで保存

PlanetScaleの無料枠を使用してデータを保存する。

https://planetscale.com/

PlanetScaleというサーバレスDBが凄く勢いのあるサービスらしいのでQuick Startやってみた

https://qiita.com/tak001/items/cfbaa9dcb542929ff235

# 既存のデータベース
Quantum Chemistry (QC) Archive

https://qcarchive.molssi.org/

# 参考記事
- [PlanetcaleをSQLAlchemyを使ってPandasで読み書きする](https://zenn.dev/sotono/articles/917a165ff6b17e)

# さらに学びたい人むけ
### paizaラーニング
- [＃01:データベースとは ](https://paiza.jp/works/sql/new-primer/sql-new-primer-1/73000)


# この講義では、やらないけど重要だと思われるもの
### MySQL以外のRDBS(リレーショナルデータベース)
- Postgre SQL
- Oracle Database

PostgreSQLを少し行ったことがあります。今後、別講義で使い方作成動画を作るかも。

### NoSQLデータベース (ドキュメント ストア)
- MongoDB
- Firebase
- DynamoDB
- Couchbase
- Cosmos DB


### グラフデータベース
- neo4j
- ArangoDB
- Cosmos DB 

neo4jを少し行ったことがあります。今後、別講義で使い方作成動画を作るかも。

