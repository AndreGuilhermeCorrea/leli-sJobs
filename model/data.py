import requests
import json

class data:

  def checking(cpf, senha):
   
    #link do db
    firebase = 'https://lelisbase-default-rtdb.firebaseio.com'
    
    usuario = f'{firebase}/usuarios/{cpf}'
   
    #get (consulta)
    consulta = requests.get(f'{usuario}/senha.json',data=json.dumps(senha))
    resposta = consulta.text   
    senha2 = '"'+senha+'"'
    
    if(senha2 ==  resposta):
      return True
    else:
      return False




