import pandas
from rdkit import Chem
from rdkit.Chem import PandasTools
from rdkit.Chem import Descriptors

class RDKitSmilesAnalyser():
    def __init__(self, smiles):
        self.smiles = smiles
        self.mol = Chem.MolFromSmiles(self.smiles)

    def print_TPSA(self):
        return print(Descriptors.TPSA(self.mol))


class RDkitSdfAnalyser():
    def __init__(self, sdffile):
        self.sdffile = sdffile
        self.df = pandas.DataFrame()
        self.df = PandasTools.LoadSDF(self.sdffile)

    def print_selfdf(self):
        return print(self.df)

    def add_TPSA(self):
        self.df["TPSA"] = self.df["ROMol"].map(Descriptors.TPSA)
        return self.df

    def add_molLogP(self):
        self.df["MolLogP"] = self.df["ROMol"].map(Descriptors.MolLogP)
        return self.df

    def del_mol(self):
        self.df = self.df.drop("ROMol", axis=1)
        return self.df

    def output_csv(self):
        return self.df.to_csv("output.csv")

# importしただけで、その読み込んだライブラリの処理が実行されるのは面倒なので、
# if __name__ == “__main__“: という一文を書いておくと、特定のライブラリをインポートした時に
# その内部のプログラムが動かないようにするために記述します。

# acetone = RDKitSmilesAnalyser("CC(=O)C")
# print("TPSAは")
# acetone.print_TPSA()

if __name__ == '__main__':
    logdatasetdf = RDkitSdfAnalyser("data/logSdataset1290_2d.sdf")
    print("読み込み")
    logdatasetdf.print_selfdf()
    logdatasetdf.add_TPSA()
    print("TPSA追加")
    logdatasetdf.print_selfdf()
    logdatasetdf.add_molLogP()
    print("molLogP追加")
    logdatasetdf.print_selfdf()
    logdatasetdf.del_mol()
    print("del mol")
    logdatasetdf.print_selfdf()
    logdatasetdf.output_csv()