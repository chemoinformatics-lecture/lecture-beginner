from rdkit.Chem import PandasTools
from rdkit.Chem import Descriptors

from setting import CONNECTION

class SdfaddSQL():
    def __init__(self, sdffile):
        self.sdf = sdffile
        self.df = PandasTools.LoadSDF(self.sdf)

    def add_info(self):
        self.df["TPSA"] = self.df["ROMol"].map(Descriptors.TPSA)
        self.df["MolLogP"] = self.df["ROMol"].map(Descriptors.MolLogP)

    def del_mol(self):
        self.df = self.df.drop("ROMol", axis=1)

    def add_sql(self):
        self.df.to_sql('test', CONNECTION, if_exists='append', index=None)

if __name__ == '__main__':
    logdatasetdf = SdfaddSQL("data/logSdataset1290_2d.sdf")
    logdatasetdf.add_info()
    logdatasetdf.del_mol()
    logdatasetdf.add_sql()
