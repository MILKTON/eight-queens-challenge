from .db import Base, engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, JSON
from sqlalchemy import Sequence
from .db import Session

class soluciones(Base):
    __tablename__ = "soluciones"
    id = Column(Integer,Sequence('id'),primary_key=True)
    reinas = Column(Integer, unique=True, nullable=False,primary_key=True)
    soluciones = Column(String, nullable=False)

    def __init__(self,NumReinas,Solucion):
        self.reinas=NumReinas
        self.soluciones=Solucion

    def insertar_registro(self): #dentro de la clase soluciones
        Session.add(self)

def init_db():
  Base.metadata.create_all(bind=engine)