from sqlalchemy import (
    Table,
    Column,
    Index,
    Integer,
    Text,
    Numeric,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    )

from pyramid.security import Allow, Everyone

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base	()


class Login(object):
  __name__ = None
  __acl__ = [(Allow, 'clientes','clientes'),
	     (Allow,'gerentes','gerentes')]
  def __init__(self,request):
    pass

class Projetos(Base):
    __tablename__ = 'projetos'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer,primary_key=True)
    nome = Column(Text)
    objetivo = Column(Text)
    asis = Column(Text)
    tobe = Column(Text)
    aprovacao = Column(Text)
    status = Column(Text)
    valor = Column(Text)
    gerente_id = Column(Integer, ForeignKey('gerentes.id'))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    alteracoes = relationship("Alteracoes")
    def __init__(self, nome, objetivo, asis,tobe, aprovacao, status, gerentes, clientes,valor):
      self.nome = nome
      self.objetivo = objetivo
      self.asis = asis
      self.tobe = tobe
      self.aprovacao = aprovacao
      self.status = status
      self.gerente_id = gerentes
      self.cliente_id = clientes
      self.valor = valor
    
class Tarefas(Base):
    __tablename__ = "tarefas"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    descricao = Column(Text)
    status = Column(Integer)
    projeto_id = Column(Integer, ForeignKey("projetos.id"))
    gerente_id = Column(Integer, ForeignKey("gerentes.id"))
    def __init__(self, descricao,status,projeto,gerente):
      self.descricao = descricao
      self.status = status
      self.projeto_id = projeto
      self.gerente_id = gerente

class Gerentes(Base):
    __tablename__ = 'gerentes'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    nome = Column(Text)
    senha = Column(Text)
    email = Column(Text, unique=True)
    telefone = Column(Text)
    area = Column(Text)
    projetos = relationship("Projetos")
    tarefas = relationship("Tarefas")

    def __init__(self, nome,senha,email,telefone,area):
      self.nome = nome
      self.senha = senha
      self.email = email
      self.telefone = telefone
      self.area = area

class Clientes(Base):
    __tablename__ = 'clientes'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    nome = Column(Text)
    email = Column(Text)
    senha = Column(Text)
    telefone = Column(Text)
    empresa = Column(Text)
    projetos = relationship("Projetos")
    def __init__(self, nome,senha,email,empresa,telefone):
      self.nome = nome
      self.senha = senha
      self.email = email
      self.empresa = empresa
      self.telefone = telefone

class Alteracoes(Base):
    __tablename__ = 'alteracoes'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, autoincrement=True, primary_key=True)
    descricao = Column(Text)
    interacao = Column(Integer)
    projeto_id = Column(Integer, ForeignKey("projetos.id"))
    def __init__(self, descricao,pid,interacao):
      self.descricao = descricao
      self.projeto_id = pid
      self.interacao = interacao
      
class Emails(Base):
    __tablename__ = 'Emails'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(Text)
    corpo = Column(Text)
    def __init__(self, nome,corpo):
      self.nome = nome
      self.corpo = corpo