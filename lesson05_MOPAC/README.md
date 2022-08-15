# なぜ
MOPAC (Molecular Orbital PACkage) は、MINDO、MNDO、AM1、PM3、PM5、Sparkle/PM3などの半経験的量子力学計算を行うための計算化学ソフトウェアである。


# どのようにするか

[mopac2016](http://openmopac.net/MOPAC2016.html)を用いてHOMOやLUMOなどを計算して、その値を取得する。
2021年8月17日にMOPAC2016の代理店での販売を終了し、Stewartの公式HPから実行バイナリの無料配布（オープンアクセス）が開始されている。

`conda install -c conda-forge mopac`

# 講義動画

https://vimeo.com/showcase/8857656

# 何をするか
1, MOPACの実行 (GUI, CUI)と得られる値の確認

2, RDKitによる配座探索

3, ファイルの入出力

4, 複数分子の実行

# 他の手段はあるか。
- gaussian

- Spartan

- GAMESS
