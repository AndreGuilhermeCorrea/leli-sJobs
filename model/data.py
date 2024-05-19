import requests
import json
from model.emailUser import EmailUser

class data:

  def checking(cpf, senha):
   
    #link do db
    firebase = 'https://lelisbase-default-rtdb.firebaseio.com'
    
    usuario = f'{firebase}/usuarios/{cpf}'

    # Chama a função para recuperar o email do usuário
    sender_email = requests.get(f'{usuario}/email.json')

    #get (consulta)
    consulta = requests.get(f'{usuario}/senha.json',data=json.dumps(senha))

    resposta = consulta.text  
    senha2 = '"'+senha+'"'
    
    EmailUser.set_email(sender_email.text)
    remetente = EmailUser.get_email()
    print(remetente)
    
    if(senha2 ==  resposta):
      return True
    else:
      return False
