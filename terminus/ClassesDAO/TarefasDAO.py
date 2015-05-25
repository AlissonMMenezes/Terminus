from ..models import (
    DBSession,
    Tarefas,
    Projetos,
    Gerentes,
    )

class TarefasDAO:
  def salvar(self,data):
    descricao = data["Descricao"]
    status = data["Status"]
    projeto = data["Projeto"]
    gerente = data["Gerente"]
    try:
      DBSession.add(Tarefas(descricao,status,projeto,gerente))
      print("Salvo com sucesso!")
      retorno = "Salvo com sucesso!"
    except Exception as e:
      print ("Erro: ",e)
      retorno = "Erro!"
    return retorno
  
  def atualizar(self, data):
    self.id = data["id"]
    self.status = data["status"]
    try:
      retorno = DBSession.query(Tarefas).filter_by(id=self.id).update({"status":self.status})
      retorno = {"status":"list-group-item-success","message":"Salvo com Sucesso!"}
    except Exception as e:
      print("Erro! ",e)
      retorno = {"status":"","message":"Erro!"}
    
    return retorno
    
  def excluir(self, data):
    print("excluir")
   
  def listar(self,data):
    id = data["pid"]
    try:
      retorno = DBSession.query(Tarefas,Projetos,Gerentes).filter_by(projeto_id=id).join((Projetos, Tarefas.projeto_id == Projetos.id),(Gerentes, Tarefas.gerente_id == Gerentes.id)).all()
      print (retorno)
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno