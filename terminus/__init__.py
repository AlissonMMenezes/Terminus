from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import SignedCookieSessionFactory
from pyramid_mailer.mailer import Mailer

my_session_factory = SignedCookieSessionFactory('itsaseekreet')

from .models import (
    DBSession,
    Base,
    )
from .ClassesDAO.LoginDAO import *


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    l = LoginDAO()
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)    
    Base.metadata.bind = engine
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=l.groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings, root_factory="terminus.models.Login")
    config.registry['mailer'] = Mailer.from_settings(settings)
    config.set_session_factory(my_session_factory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    #Admin routes
    config.add_route('adm', '/adm')
    config.add_route('clientes', '/adm/clientes')
    config.add_route('gerentes', '/adm/gerentes')
    config.add_route('novoprojeto', '/adm/novoprojeto')
    config.add_route('novogerente', '/adm/novogerente')
    config.add_route('addgerente', '/adm/addgerente')
    config.add_route('editargerente', '/adm/{id}/editargerente')
    config.add_route('deletargerente', '/adm/{id}/deletargerente')
    config.add_route('deletarcliente', '/adm/{id}/deletarcliente')
    config.add_route('atualizargerente', '/adm/atualizargerente')
    config.add_route('novocliente', '/adm/novocliente')
    config.add_route('addcliente', '/adm/addcliente')
    config.add_route('projeto', '/adm/projeto/{pid}/')
    config.add_route('addprojeto', '/adm/addprojeto')
    config.add_route('tarefa', '/adm/projeto/{id}/addtarefa')
    config.add_route('finalizar-tarefa', '/adm/projeto/{id}/finalizar/{status}/{pid}')
    config.add_route("responder-alteracao","adm/{id}/responderalteracao/{pid}")
    config.add_route("configuracoes","/adm/configuracoes")
    config.add_route("cadastro-email","/adm/cadastro-email/")
    config.add_route("atualizar-email","/adm/atualizar-email/")

    #Client routes
    config.add_route('login-gerentes', '/adm/login')
    config.add_route("cliente-index","/{id}/index")
    config.add_route("cliente-dados","/{id}/dados")
    config.add_route("cliente-atualizar","/{id}/atualizarcliente")
    config.add_route("projeto-cliente","/{id}/projeto/{pid}")
    config.add_route("projeto-aprovacao","/{id}/projetoaprovacao/{pid}")
    config.add_route("solicitar-alteracao","/{id}/solicitaralteracao/{pid}")
    config.scan()
    return config.make_wsgi_app()

