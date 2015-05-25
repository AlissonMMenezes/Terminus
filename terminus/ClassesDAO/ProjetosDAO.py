from ..models import (
    DBSession,
    Projetos,
    Gerentes,
    Clientes,
    )

class ProjetosDAO:
  def salvar(self,data):
    nome = data["Nome"]
    objetivo = data["Objetivo"]
    asis = data["Asis"]
    tobe = data["Tobe"]
    aprovacao = data["Aprovacao"]
    status = data["Status"]
    gerente = data["Gerente"]
    cliente = data["Cliente"]
    valor = data["Valor"]
    
    try:
      g = DBSession.query(Gerentes).filter_by(nome=gerente).one()
      c = DBSession.query(Clientes).filter_by(nome=cliente).one()
      print("======== DEBUGANDO ========")
      print(g.nome)
      print(c.nome)
      print("======== DEBUGANDO ========")
      DBSession.add(Projetos(nome,objetivo,asis,tobe,aprovacao,status,g.id,c.id,valor))
      print ("Salvo com sucesso!")
      retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print ("Erro: ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    return retorno
  
  def atualizar(self, data):
    try:
      retorno = DBSession.query(Projetos).filter_by(id=data["pid"]).update({"aprovacao":data["aprovacao"]})
      retorno = {"status":"alert alert-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print("Erro! ",e)
      retorno = {"status":"alert alert-danger","message":"Erro!"}
    
    return retorno
    
  def excluir(self, data):
    print ("excluir")
  
  def buscar(self, data):
    try:
      retorno = DBSession.query(Projetos,Gerentes,Clientes).filter_by(id=data["pid"]).join((Gerentes,Projetos.gerente_id == Gerentes.id),(Clientes,Projetos.cliente_id == Clientes.id)).one()
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno   
  
  def listar(self):
    try:
      retorno = DBSession.query(Projetos,Gerentes,Clientes).join((Gerentes,Projetos.gerente_id == Gerentes.id),(Clientes,Projetos.cliente_id == Clientes.id)).all()
      print(retorno)
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno
  
  def listar_cliente(self, data):
    try:
      retorno = DBSession.query(Projetos,Gerentes,Clientes).filter_by(cliente_id=data).join((Gerentes,Projetos.gerente_id == Gerentes.id),(Clientes,Projetos.cliente_id == Clientes.id)).all()
      print(retorno)
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno