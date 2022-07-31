from rdkit import Chem
import sascore

if __name__ == '__main__':
    mol = Chem.MolFromSmiles("Cc1c(C(=O)NCCO)[n+](=O)c2ccccc2n1[O-]")
    print(sascore.calculateScore(mol))
