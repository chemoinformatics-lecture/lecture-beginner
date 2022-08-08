from rdkit.Chem import PandasTools

df = PandasTools.LoadSDF('data/data_set.sdf')
df = df.drop('ROMol', axis=1)
df.to_csv('data/output.csv', index=False)