from ..models import (
    DBSession,
    Projetos,
    Alteracoes,
    )

class AlteracoesDAO:  
  def salvar(self,data):
    descricao = data["Descricao"]
    projetoID = data["pid"]
    Interacao = data["Interacao"]
    try:
      DBSession.add(Alteracoes(descricao,projetoID, Interacao))
      print("Salvo com sucesso!")
      retorno = "Salvo com sucesso!"
    except Exception as e:
      print ("Erro: ",e)
      retorno = "Erro!"
    return retorno
  
  def atualizar(self, data):
    print("atualizar")
    
  def excluir(self, data):
    print("excluir")
   
  def buscar(self,data):
    id = data["pid"]
    try:
      retorno = DBSession.query(Alteracoes,Projetos).filter_by(projeto_id=id).join((Projetos, Alteracoes.projeto_id == Projetos.id)).all()
      print (retorno)
    except Exception as e:
      print ("Erro: ",e)
      retorno = e
    return retorno