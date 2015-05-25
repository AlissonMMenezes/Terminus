from ..models import (
    DBSession,
    Projetos,
    Gerentes,
    Clientes,
    )



class LoginDAO():
  GROUPS = {}
  USER = {}
  def LoginGerente(self, login):
    try:
      g = DBSession.query(Gerentes).filter_by(email=login).one()
      self.USER[g.email] = g.senha
      self.USER["nome"] = g.nome
      self.GROUPS[g.email] = ["gerentes"]
      return self.USER
    except Exception as e:
      print("Erro: ",e)
      return {"Erro":"Erro"}
  
  def LoginCliente(self, login):
    try:
      c = DBSession.query(Clientes).filter_by(email=login).one()
      self.USER[c.email] = c.senha
      self.USER["id"] = c.id
      self.USER["nome"] = c.nome
      self.GROUPS[c.email] = ["clientes"]
      print(self.USER)
      return self.USER
    except Exception as e:
      print("Erro: ",e)
      return {"Erro":"Erro"}
    
  def groupfinder(self,userid, request):
    if userid in self.USER:
        return self.GROUPS.get(userid, [])
