from sqlalchemy import Column, String, Integer, MetaData, Table
from crud.database import Base, Register, engine

metadata = MetaData()

user = Table('usuarios', metadata,
Column('idUsuario', Integer, primary_key=True, autoincrement=True),
Column('nome', String(244)),
Column('telefone', String(9)),
Column('ddd', String(2)),
Column('idade', String(2)),
Column('email', String(244)),
Column('mensagem', String(244)))

# metadata.create_all(engine)

class Usuarios(Base, Register):

    __tablename__ = "usuarios"

    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(125))
    telefone = Column(String(9))
    ddd = Column(String(2))
    idade = Column(String(2))
    email = Column(String(244))
    mensagem = Column(String(244))
