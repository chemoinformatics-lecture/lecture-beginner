##############################################################################
# 次の２つのリストの中に入っている最も分子量が小さいsmilesとその分子量を返す関数を作成せよ。
smiles_list1 = ["CC(=O)C", "C1=CC=C(C=C1)O", "CC1=CC=CC=C1"]
smiles_list2 = [
    "C[C@@]12CCC[C@](C)(C1CC[C@@]13CC(=C)[C@@](C1)(CCC23)OC1OC(CO)C(OC2OC(CO)C(O)C(O)C2O)C(O)C1OC1OC(CO)C(O)C(O)C1O)C(=O)OC1OC(CO)C(O)C(O)C1O",
    "C[C@@]12CCCC(C)(C1CC[C@@]13CC(=C)[C@](C1)(CCC23)O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@@H]1O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O)C(=O)O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O",
    "CC1=CC2=C(C=C1C)N(CC(O)C(O)C(O)CO)C1=NC(=O)[N-]C(=O)C1=N2",
    "CC1(C)O[C@H]2CC(=O)OC[C@@]22[C@H]1CC(=O)[C@]1(C)[C@@H]2CC[C@@]2(C)[C@@H](OC(=O)[C@H]3O[C@@]123)C1=COC=C1",
]
##############################################################################

from rdkit import Chem
from rdkit.Chem import Descriptors

def minimum_molecule_print(smiles_list):
    mol_dict = {}
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        mol_weight = Descriptors.ExactMolWt(mol)
        mol_dict[smiles] = float(mol_weight)
    print(min(mol_dict, key=mol_dict.get))
    print(min((mol_dict).values()))

if __name__ == '__main__':
    print("------------------------------------")
    print("smiles_list1の最小分子量とそのsmilesは")
    minimum_molecule_print(smiles_list1)

    print("------------------------------------")
    print("smiles_list2の最小分子量とそのsmilesは")
    minimum_molecule_print(smiles_list2)
