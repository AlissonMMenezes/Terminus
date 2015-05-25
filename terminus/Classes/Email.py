from pyramid_mailer.mailer import Mailer
from pyramid_mailer.message import Message
import transaction


class Email:
  subject = ""
  sender = ""
  recipient = ""
  body = ""
  
  def Enviar(self,sub,sen,rec,body, m):
    self.subject = sub
    self.sender = sen
    self.recipient = rec
    self.body = body    
    message = Message(subject="Terminus: Cadastro",
		      sender="contato@responsus.com.br",
		      recipients=[self.recipient],
		      body=self.body)
    m.send(message)
    transaction.commit()
    
    
    
    