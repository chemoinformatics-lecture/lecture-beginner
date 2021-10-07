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

1, anacondaをインストールする。<br>
windows, mac, linuxのどれでもインストールできます。自分の使っているものに合わせてインストールしてください。

2, pycharmのcommunity版をインストールする。<br>
windows, mac, linuxのどれでもインストールできます。自分の使っているものに合わせてインストールしてください。

3, git hubにアカウントを作成する。<br>
webサイトにアクセスして、サインアップしてください。

# condaで環境を作成していきます。

pythonは、3.8で作ってください。

```
conda install jupyter
conda install -c anaconda pandas
conda install scikit-learn
conda install -c conda-forge rdkit
conda install -c mcs07 pubchempy
conda install -c conda-forge matplotlib
conda install -c intel scikit-learn
```

scikit-learnはM1 mac用が別途あります。

#以下は任意

発表資料を作成する際に使用しています。
```
conda install -c conda-forge rise
conda install nbconvert
```

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
