# なぜ
テストを書いたり、配布物を作ったりする意味

# どのように
オリジナルのコードなどをPIPで配布する方法を学びます。

# 何をするか


# 講義動画

## docstring

参考ファイル
- [GoogleスタイルのPython Docstringの入門](https://qiita.com/11ohina017/items/118b3b42b612e527dc1d)
- [[Python]可読性を上げるための、docstringの書き方を学ぶ（NumPyスタイル）](https://qiita.com/simonritchie/items/49e0813508cad4876b5a)
- [[Python] docstringのスタイルと書き方](https://qiita.com/flcn-x/items/393c6f1f1e1e5abec906)


## デバッグ
1. printでデバッグ
print文を書き込む。

2. pycharmの機能でデバッグ
デバックしたいところをクリックして、 ▷マークの横の虫マークでデバッグできるようになる。

3. pdb(発展編)
import pdb で色々とできます。上記の二つで物足りない人は、こちらを勉強してみてください。 
- https://docs.python.org/ja/3/library/pdb.html

4. 時間計測
- time関数
<br>[処理時間を計測する](https://www.python.ambitious-engineer.com/archives/3355)
- Python プロファイラ
<br>[Pythonの処理が遅いときにプロファイラを使って原因を調べる方法](https://paiza.hatenablog.com/entry/2018/09/10/Python%E3%81%AE%E5%87%A6%E7%90%86%E3%81%8C%E9%81%85%E3%81%84%E3%81%A8%E3%81%8D%E3%81%AB%E3%83%97%E3%83%AD%E3%83%95%E3%82%A1%E3%82%A4%E3%83%A9%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E5%8E%9F%E5%9B%A0)
<br>[Pythonプロファイラ](https://docs.python.org/ja/3/library/profile.html)

## テスト
- Unittest
[Python標準のunittestの使い方メモ](https://qiita.com/aomidro/items/3e3449fde924893f18ca)

- doctest
Python にはソースコードのドキュメンテーションをサポートするための docstring という文字列を使ってドキュメントを作成することができます。
- さらに docstring には関数の使用例を記述するための構文が用意されています。
- またその使用例を示すコードは関数が実際に記述したとおりに振る舞うかどうかをテストする機能も備わっており doctest と呼ばれます。
[Pythonでdocstringにテストコードを記述するdoctestの書き方、使い方](https://note.nkmk.me/python-doctest-example/)

- pytest
[pytestの使い方](https://rinatz.github.io/python-book/ch08-02-pytest/)

# プログラムの配布方法
## ライセンス形態
1. MIT License
- 作成者や著作権者は、製品に対しての義務や責任を何ら負わないこと
- 著作権の表示を保持すること
2. BSD License (3-clause BSD License)
- 作成者や著作権者は、製品に対しての義務や責任を何ら負わないこと
- 著作権の表示を保持すること
- 派生した製品に、勝手に製品の宣伝または推薦者として組織や貢献者の名前を使用しないこと
3. Apache License
- 作成者や著作権者は、製品に対しての義務や責任を何ら負わないこと
- 著作権と特許権の表示を保持すること
- 製品を改変した場合は、その変更点を示すこと
- 製品中の特許に対して特許侵害を主張する場合は、その特許ライセンスは終了する
4. GNU General Public License (GPL)
- 作成者や著作権者は、製品に対しての義務や責任を何ら負わないこと
- 著作権の表示を保持すること
- 改変、再頒布の前提としてソースコードへのアクセスができること
- 製品を改変した場合は、その変更点を示すこと
- 製品を改変した場合もGPLで配布すること

### 参考資料
[GitHubでライセンスを設定する](https://qiita.com/shibukk/items/67ad0a5eda5a94e5c032)

## pipで配布
- setup.pyを作成 <br>
https://architecting.hateblo.jp/entry/2020/12/24/173311
  

## condaで配布
- Condaパッケージの作成方法
https://qiita.com/iisaka51/items/5828a50744be209705d0