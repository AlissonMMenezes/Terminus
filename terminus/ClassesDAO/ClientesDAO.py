from ..models import (
    DBSession,
    Clientes,
    )
import hashlib

class ClientesDAO:
  def salvar(self,data):
    nome = data["Nome"]
    email = data["Email"]
    senha = hashlib.sha512(data["Senha"]).hexdigest()
    empresa = data["Empresa"]
    telefone = data["Telefone"]
    try:
      DBSession.add(Clientes(nome,senha,email,empresa,telefone))
      print("Salvo com sucesso!")
      retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print ("Erro: ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    return retorno
  
  def buscar(self, id_cliente):
    self.id = id_cliente
    try:
      retorno = DBSession.query(Clientes).filter_by(id=self.id).one()
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno
  
  def atualizar(self, data):
    self.id = data["Id"]
    self.nome = data["Nome"]
    self.email = data["Email"]
    self.senha = hashlib.sha512(data["Senha"]).hexdigest()
    self.empresa = data["Empresa"]
    self.telefone = data["Telefone"]
    if not data["Senha"]:
      res = DBSession.query(Clientes).filter_by(id=self.id).one()
      self.senha = res.senha
    
    try:
      retorno = DBSession.query(Clientes).filter_by(id=self.id).update({"nome":self.nome,"senha":self.senha,"email":self.email,"telefone":self.telefone,"empresa":self.empresa})
      retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print("Erro! ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    
    return retorno
    
  def excluir(self, data):
    self.id = data
    try:   
      retorno = DBSession.query(Clientes).filter_by(id=self.id).delete()
    except Exception as e:
      print("Erro: ",e)
   
  def listar(self):
    try:
      retorno = DBSession.query(Clientes).all()
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno