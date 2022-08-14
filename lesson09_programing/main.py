from plusrdkit import RDKitSmilesAnalyser

# 他のファイルから呼び出して、実行した例
phenol = RDKitSmilesAnalyser("C1=CC=C(C=C1)O")
print("TPSAは")
phenol.print_TPSA()