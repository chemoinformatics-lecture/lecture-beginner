# なぜ


# どのように
pythonで化合物を扱うことができるRDKitの簡単な使い方を学んでいく。

# 講義動画

https://vimeo.com/showcase/8857611

# 何をするか

- 分子の読み込みと表示と出力
```
#１分子の読み込み
rdkit.Chem.MolFromMolBlock(mol_block)
rdkit.Chem.MolFromSmiles(smiles)
rdkit.Chem.MolFromInchi(Inchi)
#複数分子の読み込み
rdkit.Chem.SDMolSupplier(SDF)
rdkit.Draw.MolsToGridImage(mols)
rdkit.Chem.PandasTools.LoadSDF(SDF)
#Pandasの復習
df["smiles"] = df["ROMol"].map(Chem.MolToSmiles)
```

- Descriptorsの使い方
```
from rdkit.Chem import Descriptors
#TPSAの出力
Descriptors.TPSA(mol)
#HBDの出力
Descriptors.NumHDonors(mol)
# PandasToolsを使いながらDescriptorsを行う。
from rdkit.Chem import PandasTools
df = PandasTools.LoadSDF('data/PubChem_TCI_phenol_records.sdf')
df["TPSA"] = df["ROMol"].map(Descriptors.TPSA)
# 全てを取得
for i, j in Descriptors.descList:
    df[i] = df["ROMol"].map(j)
```

- 分子の取り扱い方
```
# RDKitの分子を取り扱う
# 環関係
ringinfo = mol.GetRingInfo()
ringinfo.NumRings()
# 結合関係
bonds_info = mol.GetBonds()
bond.GetBondType()
begin_atom = bond.GetBeginAtom()
begin_atom.GetSymbol()
end_atom = bond.GetEndAtom()
end_atom.GetSymbol()
atoms_info = mol.GetAtoms()
# 原子関係
atoms_info = mol.GetAtoms()
atom.GetIdx()
atom.GetSymbol()
atom.GetNumRadicalElectrons()
atom.GetFormalCharge()
```

- 構造変換
```
1番大きなフラグメントを残して他を除去
rdkit.Chem.MolStandardize.fragment.LargestFragmentChooser()

水素の付加
rdkit.Chem.AddHs(mol, addCoords=True)

構造最適化
rdkit.AllChem.MMFFOptimizeMolecule(mol)
```

- 部分構造探索
```
#Smartsによる部分構造検索
patt = Chem.MolFromSmarts('smarts')
matches = [mol for mol in mols if mol.HasSubstructMatch(patt)]
Draw.MolsToGridImage(matches)
```

# 番外編
化合物の類似性評価
