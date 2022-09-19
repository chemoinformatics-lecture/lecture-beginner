from sqlalchemy import Column, String
from sqlalchemy.types import Float
from sqlalchemy.ext.declarative import declarative_base

from settings import engine


Base = declarative_base()

class CompoundName(Base):
    __tablename__ = "name"
    inchikey = Column("InCHIKey", String(767), primary_key=True)
    smiles = Column("rdkit_smiles", String(767))

class Pubchemcid():
    __tablename__ = "cid"
    inchikey = Column("InCHIKey", String(767), primary_key=True)
    cid = Column("cid", )

class Solubility():
    __tablename__ = "solvility"
    inchikey = Column("InCHIKey", String(767), primary_key=True)
    table_smiles = Column("rdkit_smiles", String(767))
    logp = Column("logP", Float)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)