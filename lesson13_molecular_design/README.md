# なぜ


# どのように
分子を設計する手法を確認する。

# 何をするか

- GDB-11, GDB-13 and GDB-17
それぞれ、11, 13, 17原子までのC、N、O、S、ハロゲンからなる分子のデータベース(低分子有機化合物を、化学的安定性と合成可能性に関する簡単なルールに従って列挙したもの)
17原子までのもので1,664億個のデータベース。  
https://pubs.acs.org/doi/10.1021/ci300415d  
https://pubs.acs.org/doi/10.1021/ar500432k  
https://future-chem.com/chemical-space-gdb/  
データはsmiles形式でdownloadできる。  
https://gdb.unibe.ch/downloads/


- BRICS（Breaking of Retrosynthetically Interesting Chemical Substructures）  
https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cmdc.200800178  
https://future-chem.com/rdkit-brics/

- Bayesian molecular design with a chemical language model 
SMILES化学言語表記に従った既存の化合物のASCII文字列を自然言語処理することで、よく出現する化学的断片のパターンを獲得する化学言語モデルを算出する。
分子設計の手法に使える。  
https://link.springer.com/article/10.1007/s10822-016-0008-z

分子設計
https://github.com/MolecularAI/Reinvent