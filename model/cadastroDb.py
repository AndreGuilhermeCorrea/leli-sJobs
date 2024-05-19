import requests
import json

class CadastroDb:

  def cadastrar(cpf, senha, email, nome, sobrenome):
    #link do db
    firebase = 'https://lelisbase-default-rtdb.firebaseio.com'
    dados = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'senha': senha}
    respostaFuncao = CadastroDb.consulta_usuario(cpf)  
    
    if(cpf in respostaFuncao):
      return False
    else:
      requests.put(f'{firebase}/usuarios/{cpf}.json', data =json.dumps(dados))
      return True
     
  def consulta_usuario(cpf):
    pass
    firebase = 'https://lelisbase-default-rtdb.firebaseio.com/'
    #get (consulta)
    consulta = requests.get(f'{firebase}usuarios.json', data=json.dumps(cpf))
    res = json.dumps(consulta.json())     
    return res
  
  def editar_usuario(cpf, senha, email, nome, sobrenome):
    pass
    firebase = 'https://lelisbase-default-rtdb.firebaseio.com/'
    dados = {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'senha': senha}
    #path (edita)
    edicao = requests.patch(f'{firebase}/usuarios/{cpf}.json',data=json.dumps(dados))
    res = json.dumps(edicao.json()) 
    return res
