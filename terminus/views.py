# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
import pprint
import hashlib

from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    )

from .ClassesDAO.GerentesDAO import *
from .ClassesDAO.ClientesDAO import *
from .ClassesDAO.ProjetosDAO import *
from .ClassesDAO.TarefasDAO import *
from .ClassesDAO.LoginDAO import *
from .ClassesDAO.AlteracoesDAO import * 
from .ClassesDAO.EmailsDAO import * 
from .Classes.Email import *

@view_config(route_name='adm', renderer='templates/adm/index.pt', permission="gerentes")
def indexadm_view(request):
  if not request.session['logado']:
    headers = forget(request)
    return HTTPFound(location = "/adm")
  p = ProjetosDAO()
  retorno = p.listar()
  return {'resultado': retorno}    


@view_config(route_name='novoprojeto', renderer='templates/adm/novo-projeto.pt', permission="gerentes")
def novoprojeto_view(request):
    g = GerentesDAO()
    c = ClientesDAO()
    gerentes = g.listar()
    clientes = c.listar()
    return {'gerentes': gerentes, 'clientes': clientes,'retorno':""}

@view_config(route_name='addprojeto', renderer='templates/adm/novo-projeto.pt', permission="gerentes")
def addprojeto_view(request):
    p = ProjetosDAO()
    g = GerentesDAO()
    c = ClientesDAO()
    gerentes = g.listar()
    clientes = c.listar()
    print (request.POST)
    r = p.salvar(request.POST)
    return {'retorno': r,"gerentes":gerentes,"clientes":clientes}

@view_config(route_name='projeto', renderer='templates/adm/ver-projeto.pt', permission="gerentes")
def verprojeto_view(request):
    p = ProjetosDAO()
    t = TarefasDAO()
    g = GerentesDAO()
    a = AlteracoesDAO()
    gerentes = g.listar()    
    tarefas = t.listar(request.matchdict)
    projeto = p.buscar(request.matchdict)
    alteracoes = a.buscar(request.matchdict)
    return {'resultado': projeto,"Tarefas":tarefas,"gerentes":gerentes,"Alteracoes":alteracoes}
  
@view_config(route_name='tarefa', renderer='templates/adm/ver-projeto.pt',permission="gerentes")
def addtarefa_view(request):    
    t = TarefasDAO()
    v = request.GET
    r = t.salvar(request.GET)
    return HTTPFound(location="/adm/projeto/"+v["Projeto"]+"/")

@view_config(route_name='gerentes', renderer='templates/adm/gerentes.pt', permission="gerentes")
def gerentes_view(request):    
    g = GerentesDAO()
    r = g.listar()
    return {'resultado': r}

@view_config(route_name='novogerente', renderer='templates/adm/novo-gerente.pt', permission="gerentes")
def novogerente_view(request):     
    gerente = {"id":"","nome":'',"email":"","telefone":"","senha":"","area":""}
    return {"action":"addgerente", "gerente":gerente,"retorno":"","action":"addgerente"}

@view_config(route_name='editargerente', renderer='templates/adm/novo-gerente.pt', permission="gerentes")
def editargerente_view(request):    
    g = GerentesDAO()
    id_gerente = request.matchdict["id"]
    gerente = g.buscar(id_gerente)
    print(gerente)
    return {'action': "/adm/atualizargerente", "gerente":gerente,"retorno":""}

@view_config(route_name='atualizargerente', renderer='templates/adm/novo-gerente.pt', permission="gerentes")
def atualizargerente_view(request):    
    g = GerentesDAO()
    dados = request.POST
    gerente = g.atualizar(dados)
    print(gerente)
    return HTTPFound(location="/adm/"+dados["id"]+"/editargerente")

@view_config(route_name='addgerente', renderer='templates/adm/novo-gerente.pt', permission="gerentes")
def addgerente_view(request):    
    g = GerentesDAO()
    print (request.POST)
    r = g.salvar(request.POST)
    gerente = {"id":"","nome":'',"email":"","telefone":"","senha":"","area":""}
    return {'retorno': r,"action":"addgerente","gerente":gerente}

@view_config(route_name='deletargerente', renderer='templates/adm/gerentes.pt', permission="gerentes")
def deletargerente_view(request):    
    g = GerentesDAO()
    data = request.matchdict["id"]
    r = g.excluir(data)
    return HTTPFound(location="/adm/gerentes")

@view_config(route_name='clientes', renderer='templates/adm/clientes.pt',permission="gerentes")
def clientes_view(request):    
    c = ClientesDAO()
    r = c.listar()
    return {'resultado': r}
  
@view_config(route_name='novocliente', renderer='templates/adm/novo-cliente.pt',permission="gerentes")
def novocliente_view(request):     
    return {'retorno': ""}

@view_config(route_name='addcliente', renderer='templates/adm/novo-cliente.pt', permission="gerentes")
def addcliente_view(request):     
    c = ClientesDAO()
    print (request.POST)
    r = c.salvar(request.POST)

    if not "Erro!" in r['message']:
      m = Email()
      md = EmailsDAO()
      modelo_email = md.buscar('novo-cliente')
      mailer = request.registry['mailer']
      m.Enviar("Responsus: Cadastro no Terminus",
	       "contato@responsus.com.br",
	       request.POST['Email'],
	       modelo_email.corpo.replace("%l",request.POST["Email"]).replace("%s",request.POST["Senha"]),
	       mailer
	       )
    return {'retorno': r}

@view_config(route_name='deletarcliente', renderer='templates/adm/clientes.pt', permission="gerentes")
def deletargerente_view(request):    
    c = ClientesDAO()
    data = request.matchdict["id"]
    r = c.excluir(data)
    return HTTPFound(location="/adm/clientes")

@view_config(route_name='configuracoes', renderer='templates/adm/configuracoes.pt', permission="gerentes")
def configuracoes_view(request):     
    m = EmailsDAO()
    retorno = m.listar()
    return {'retorno': retorno}

@view_config(route_name='cadastro-email', renderer='templates/adm/configuracoes.pt', permission="gerentes")
def cadastroemail_view(request):         
    m = EmailsDAO()
    r = request.POST
    s = m.salvar(r)   
    return HTTPFound(location="/adm/configuracoes")

@view_config(route_name='atualizar-email', renderer='templates/adm/configuracoes.pt', permission="gerentes")
def atualizaremail_view(request):         
    m = EmailsDAO()
    r = request.POST
    s = m.atualizar(r)   
    return HTTPFound(location="/adm/configuracoes")

  
@view_config(route_name='responder-alteracao', permission="gerentes")
def responderalteracao_view(request):     
    a = AlteracoesDAO()
    r = request.params
    alt = a.salvar(request.params)
    return HTTPFound(location = "/adm/projeto/"+r["pid"]+"/")

@view_config(route_name='finalizar-tarefa', permission="gerentes")
def finalizartarefa_view(request):     
    t = TarefasDAO()
    r = request.matchdict
    alt = t.atualizar(request.matchdict)
    return HTTPFound(location = "/adm/projeto/"+r["pid"]+"/")
  
@view_config(route_name='login-gerentes', renderer='templates/adm/login.pt')
@forbidden_view_config(renderer="templates/adm/login.pt")
def login_gerente(request):
    session = request.session
    l = LoginDAO()
    login_url = request.resource_url(request.context, 'login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/adm'
    message = ''
    login = ''
    password = ''    
    if 'form.submitted' in request.params:
		login = request.params['login']
		password = hashlib.sha512(request.params['password']).hexdigest()
		USER = l.LoginGerente(login)
		if USER.get(login) == password:
			session['logado'] = USER.get("nome")
			headers = remember(request, login)
			return HTTPFound(location = "/adm",headers = headers)
		message = 'Falha ao acessar'

    return dict(
        message = message,
        url = request.application_url + '/adm/login',
        login = login,
        password = password,
        )

@view_config(name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.resource_url(request.context),
                     headers = headers)

#clientes - views - 
@view_config(route_name='cliente-index', renderer='templates/clientes/index.pt', permission="clientes")
def index_view(request):
  session = request.session
  if not request.session['logado']:
    headers = forget(request)
    return HTTPFound(location = "/")
  p = ProjetosDAO()
  c_id = request.matchdict["id"]
  retorno = p.listar_cliente(c_id)
  if int(c_id) != int(session["id"]):
    headers = forget(request)
    return HTTPFound(location = "/")
  return {'resultado': retorno}    

@view_config(route_name='cliente-dados', renderer='templates/clientes/cliente.pt', permission="clientes")
def cliente_dados_view(request):
  session = request.session
  c = ClientesDAO()
  c_id = request.matchdict["id"]
  dados = c.buscar(c_id)
  if int(c_id) != int(session["id"]):
    headers = forget(request)
    return HTTPFound(location = "/")
  return {'retorno': "",'dados':dados}  

@view_config(route_name='cliente-atualizar', renderer='templates/clientes/cliente.pt', permission="clientes")
def atualizarcliente_view(request):    
    c = ClientesDAO()
    dados = request.POST
    retorno = c.atualizar(dados)
    cliente = c.buscar(request.POST["Id"])
    return {'retorno':retorno, 'dados':cliente}

@view_config(route_name='projeto-cliente', renderer='templates/clientes/ver-projeto.pt', permission="clientes")
def clienteprojeto_view(request):
    session = request.session
    p = ProjetosDAO()
    t = TarefasDAO()
    g = GerentesDAO()
    a = AlteracoesDAO()
    gerentes = g.listar()
    tarefas = t.listar(request.matchdict)
    projeto = p.buscar(request.matchdict)
    alteracoes = a.buscar(request.matchdict)
    if int(projeto.Projetos.cliente_id) != int(session["id"]):
      headers = forget(request)
      return HTTPFound(location = "/")
    return {'resultado': projeto,"Tarefas":tarefas,"gerentes":gerentes,"Alteracoes":alteracoes}

@view_config(route_name='projeto-aprovacao', permission="clientes")
def projetoaprovacao_view(request):
    p = ProjetosDAO()
    r = p.atualizar(request.params)
    cid = request.params["cid"]
    pid = request.params["pid"]
    return HTTPFound(location = "/"+cid+"/projeto/"+pid)

@view_config(route_name='solicitar-alteracao', permission="clientes")
def solicitaralteracao_view(request):     
    a = AlteracoesDAO()
    r = request.params
    alt = a.salvar(request.params)
    return HTTPFound(location = "/"+r["cid"]+"/projeto/"+r["pid"])

@view_config(route_name='home', renderer='templates/clientes/login.pt')
def login(request):
    session = request.session
    l = LoginDAO()
    login_url = request.resource_url(request.context, 'login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/1/index'
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
		login = request.params['login']
		password = hashlib.sha512(request.params['password']).hexdigest()
		USER = l.LoginCliente(login)
		print (USER.get(login))
		cli_id = str(USER.get("id"))
		if USER.get(login) == password:
			session['logado'] = USER.get("nome")
			session['id'] = USER.get("id")
			headers = remember(request, login)
			return HTTPFound(location = "/"+cli_id+"/index",headers = headers)
		message = 'Falha ao acessar'

    return dict(
        message = message,
        url = request.application_url + '/login',
        login = login,
        )