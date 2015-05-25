from ..models import (
    DBSession,
    Gerentes,
    )

import hashlib

class GerentesDAO:
  def salvar(self,data):
    nome = data["Nome"]
    email = data["Email"]
    telefone = data["Telefone"]
    senha = hashlib.sha512(data["Senha"]).hexdigest()
    area = data["Area"]    
    try:
      e = DBSession.query(Gerentes).filter_by(email=email).count()
      if not e:
	DBSession.add(Gerentes(nome,senha,email,telefone,area))
	print("Salvo com sucesso!")
	retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
      else:
	retorno = {"status":"alert alert-danger","message":"Email ja cadastrado"}
    except Exception as e:
      print ("Erro: ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    return retorno
  
  def atualizar(self, data):
    self.id = data["id"]
    self.nome = data["Nome"]
    self.email = data["Email"]
    self.telefone = data["Telefone"]
    self.senha = hashlib.sha512(data["Senha"]).hexdigest()
    self.area = data["Area"]
    try:
      retorno = DBSession.query(Gerentes).filter_by(id=self.id).update({"nome":self.nome,"senha":self.senha,"email":self.email,"telefone":self.telefone,"area":self.area})
      retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print("Erro! ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    
    return retorno
    
  def excluir(self, data):
    self.id = data
    try:   
      retorno = DBSession.query(Gerentes).filter_by(id=self.id).delete()
    except Exception as e:
      print("Erro: ",e)

  def listar(self):
    try:
      retorno = DBSession.query(Gerentes).all()
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno
  
  def buscar(self, id_gerente):
    self.id = id_gerente
    try:
      retorno = DBSession.query(Gerentes).filter_by(id=self.id).one()
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno