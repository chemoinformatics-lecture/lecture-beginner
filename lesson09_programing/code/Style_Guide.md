
# なぜstyle guideがあるのか
- Pythonで書かれた幅広いコードのスタイルを一貫させると読みやすくなる。(ただし、一貫性にこだわりすぎるのは、狭い心の現れ)

https://pep8-ja.readthedocs.io/ja/latest/

- 他の人がコードを読みやすくする。

 
#pythonのLinterの基本
- Stylistic Lintの代表的なlinter: pycodestyle(もともとpep8だった)
  https://qiita.com/simonritchie/items/bb06a7521ae6560738a7
- Logical Lintの代表的なlinter: pyflakes
- pycodestyleとpyflakesのラッパーライブラリ: flake8

# flake8をインストールして使用する例。


# その他のlinter
- fake8より厳しいlinter : pylint
  
# 自動フォーマッター
- black
- autopep8
- yapf

# docstringのフォーマット
関数やクラスを説明するコメント文を docstringと呼び, これについてもいくつかの流儀がある.
https://qiita.com/simonritchie/items/49e0813508cad4876b5a
- PEP257
- nump
- google
