import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools



def readsdf(sdf):
    df = PandasTools.LoadSDF(sdf)
    df["InCHIKey"] = df["ROMol"].map(Chem.MolToInchiKey)
    df["rdkit_smiles"] = df["ROMol"].map(Chem.MolToSmiles)
    return df

def readcsv(csv, SMILES):
    '''
    :param csv: smilesの列があるファイルを指定
    :param SMILES: smilesの書かれている列名を指定
    :return: pandas detaframe
    '''

    df = pd.read_csv(csv)
    PandasTools.AddMoleculeColumnToFrame(df, SMILES)

    df["InCHIKey"] = df["ROMol"].map(Chem.MolToInchiKey)
    df["rdkit_smiles"] = df["ROMol"].map(Chem.MolToSmiles)
    return df

