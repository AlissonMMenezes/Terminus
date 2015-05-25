from ..models import (
    DBSession,
    Emails,
    )

class EmailsDAO:
  def salvar(self,data):
    self.nome = data["Nome"]
    self.corpo = data["Corpo"]    
    try:
      DBSession.add(Emails(self.nome,self.corpo))
      print("Salvo com sucesso!")
      retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print ("Erro: ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    return retorno

  
  def atualizar(self, data):
    self.id = data["Id"]
    self.nome = data["Nome"]
    self.corpo = data["Corpo"]    
    try:
      e = DBSession.query(Emails).filter_by(id=self.id).count()
      if not e:
	DBSession.add(Emails(self.nome,self.corpo))
	print("Salvo com sucesso!")
	retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
      else:
	retorno = DBSession.query(Emails).filter_by(id=self.id).update({"nome":self.nome,"corpo":self.corpo})
	retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}	
    except Exception as e:
      print ("Erro: ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    return retorno
  
  def buscar(self, nome_email):
    self.nome = nome_email
    try:
      retorno = DBSession.query(Emails).filter_by(nome=self.nome).one()
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno
    
  def listar(self):
    try:
      retorno = DBSession.query(Emails).all()
      print (retorno)
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno