# Terminus

Terminus - Gerenciamento de Projetos é uma ferramenta bem básica desevolvida para fins de estudo. Foi originada com o objetivo de entregar um trabalho na faculdade sobre gerenciamento de projetos e nela foram definidas algumas características como:

* Área do Cliente
* Aprovação/Reprovação de Projeto
* Solicitar Alteração
* Solicitar Projeto
* Área dos Gerentes de Projeto
* Elaborar Projetos
* Definir Gerentes de Projetos
* Definir Matriz de Responsabilidade
* Cadastro de Clientes
* Cadastro de Projetos
* Ver/Responder Solicitações de Alteração

Se for executado o procedimento padrão de deploy da aplicação ela será executada na porta 6543, que é a padrão definida pelo framework Pyramid.
 
 Urls:
 > / - Area do cliente
 >
 > /adm - Area dos gerentes de projeto
 
 Usuário padrão:
 > **login:** admin@admin
 >
 > **senha:** admin

#### Sequência para instalação:

#### Dependencias do S.O.

apt-get install python python-setuptools python-dev sqlite3

##### Dependencias do Python

easy_install pyramid_mailer

##### Instalando a aplicação

python setup.py install

#### Executando o projeto

pserve development.ini --reload

https://culturadocaractere.com.br

