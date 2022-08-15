from rdkit import Chem
import sascore

if __name__ == '__main__':
    # mol = Chem.MolFromSmiles("Cc1c(C(=O)NCCO)[n+](=O)c2ccccc2n1[O-]")
    # print(sascore.calculateScore(mol))

    path = 'data/TasteDB.smi'
    mol_dict = {}

    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            try:
                mol = Chem.MolFromSmiles(line)
                score = sascore.calculateScore(mol)
                mol_dict[line] = float(score)
            except:
                print("error:" + line, end="")

    print(mol_dict)

