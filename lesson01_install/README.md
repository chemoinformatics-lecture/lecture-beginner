# なぜ

プログラミングを学ぶことで、以下のことも身に付けられます。

1. 退屈な作業をパソコンに命令して行わせることができる
2. 論理的な思考法が身に付く
3. 世界とつながることができる
4. 考え方や考えたことを記録しておける
5. 先人たちの知恵を借りることができる

# どのように
- プログラミング言語はpythonを使う。pythonは初学者にも学びやすい。 また、ケモインフォマティクスや機械学習の分野で使われることが多く、ライブラリーが豊富にある。
- 環境作成の便利なツール、効率的にコードを書くツール、書いたコードを管理する共有する便利なツールを使う。

# 何をするか
pythonを学んだり効率的にコードを書く上で便利な３つの

1, anacondaをインストールする。<br>
windows, mac, linuxのどれでもインストールできます。自分の使っているものに合わせてインストールしてください。

https://www.anaconda.com/products/individual

2, pycharmのcommunity版をインストールする。<br>
windows, mac, linuxのどれでもインストールできます。自分の使っているものに合わせてインストールしてください。

https://www.jetbrains.com/ja-jp/pycharm/download

3, git hubにアカウントを作成する。<br>
webサイトにアクセスして、サインアップしてください。

https://github.com/

pycharmとgithubを連携する。（このとき、パソコンにgitがインストールされていない場合にはインストールされる）

# condaで環境を作成していきます。

pythonは、3.8で作ってください。

```
# レッスン1, 2用
conda update -n base -c defaults conda
conda install jupyter
conda install -c anaconda pandas
conda install -c conda-forge matplotlib
# レッスン3用
conda install -c mcs07 pubchempy
# レッスン4用
conda install -c conda-forge rdkit
# レッスン５用
conda install -c conda-forge tqdm
# レッスン6用
conda install -c intel scikit-learn
# レッスン7用
conda install -c conda-forge scikit-plot
conda install -c conda-forge pycaret
```

scikit-learnはM1 mac用が別途あります。

#以下は任意
発表資料を作成する際に使用しています。
```
conda install -c conda-forge rise
conda install nbconvert
```

# 講義動画

https://vimeo.com/showcase/8854093

#注意点
### 作成者はwindowsとmacの両方を使用していますが、主にmacを使うことが多いです。
サーバー（重たい計算とかを行わせたり、ホームページを公開したりする）などではCentOSやUbuntsなどのLinuxを用います。
これらを外部から操作するときには、コマンドだけで操作するときもあるのでコマンド操作を覚えたほうがよいと思って
macを使ってコマンド操作についても動画などに入れていました。

windowsでも別途コマンド操作方法を別途覚えればできるのですが、Linuxのコマンド操作よりも使用用途は少ないかなと思います。 windowsのコマンド操作については、必要最低限以外に講義の中で紹介したりサポートすることは無いと思います。
これらの部分は興味がないようでしたら今のところ勉強しなくても大丈夫だと思います（プログラミングを覚えるだけでも大変なので）。

### python自体は、どのプラットフォーム(windows, mac, linux)でも同じように操作できます。
プラットフォーム上で行うコマンドの操作などは異なります。macはコマンド操作の部分などで、Linuxを使うときの操作と似ています。
windowsでどうやって対応するかは、以下などが参考になると思います。

Linuxコマンド：Windowsコマンド対応表<br>
https://qiita.com/asmin/items/d53e71ed98a377ca7823

LinuxコマンドとWindowsコマンドの違いなどで検索してください。

# 他の方法の紹介
以上の選定基準としては、よく使われていたり、初心者にも優しいという点で選んでいます。
他にどんな選択肢があるかも簡単に紹介しておきます。
以下のことは、わからなくても大丈夫です。紹介だけです。

pythonは、最新版が3.10になっていますが、anacondaがデフォルトで3.8なので3.8にします。

1, anacondaをインストールしなくても、以下の方法で環境管理もできます。
- miniconda : Anacondaの最小構成版。pythonのインストールは簡単に行えるが、必要なパッケージや実行環境の構築はcondaを使用して個別に行う。
- pip と venv : pythonの標準ライブラリーで管理。
- pipenv : pipenvは、１つでpipとvenvの両方の機能を持っている。

2, pycharmをインストールしなくても、他のエディターや統合開発環境 などを使ってもできます。
- Visual Studio code : 拡張機能が豊富で軽量な人気No1のエディター
- spyder : anacondaにも入っているエディター
- Sublime Text : 軽量なテキストエディター
- Atom : エディタ、パッケージによる機能拡張を特徴
- neovim : vimの中で人気のエディター

3, git hubを使わなくてもcodeの管理は以下の方法でもできます。
- AWS Code Commit : gitをamazon のAWSで管理できる
- Cloud Source Repositories : gitをgoogle のGCPで管理できる

講義の中で紹介したりサポートすることは無いと思いますが、自分にあったものを選んで構いません。
