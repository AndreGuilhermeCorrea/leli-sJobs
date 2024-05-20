import requests
import json
import datetime

class ChatManager:

        #CHAMADA DAS FUNÇÕES DE MANIPULAÇÃO DAS MENSAGENS DO CHAT
            ####from model.chatManager import ChatManager

            ####ChatManager.criar_conversa('remetente2@email.com', 'destinatario2@email.com')
            ####ChatManager.recuperar_mensagens('destinatario2@email.com')
            ####ChatManager.recuperar_texto_mensagens('destinatario2@email.com')
            ####ChatManager.recuperar_textos_por_remetente('destinatario2@email.com', 'remetente2@email.com')
            ####ChatManager.recuperar_textos_por_remetente_hhmm('destinatario2@email.com', 'remetente2@email.com')

        #CHAMADA DA FUNÇÃO PARA CRIAÇÃO DE NÓ
            ####ChatManager.criar_no(cpf) 

    #formata o email para fazer uso no db
    def format_email(email):
        return email.replace('@', '_a_').replace('.', '_')
            
    #formata o email de retorno do db
    def format_email_back(email):
        return email.replace('_a_', '@').replace('_', '.')      
     
    #CRIA A MENSAGEM NO DB
    def criar_conversa(remetente_email, destinatario_email, texto_msg):
        pass
        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com' 
         
        destino = ChatManager.format_email(destinatario_email)
        origem = ChatManager.format_email(remetente_email)

        # Adiciona a mensagem à conversa
        timestamp = datetime.datetime.now().isoformat()
        mensagem_data = {
        'destinatario': destino,  
        'texto': texto_msg,
        'remetente': origem,
        'timestamp': timestamp
        }
        dados = {'mensagem': mensagem_data}
        # Adiciona a mensagem ao nó da conversa
        requests.post(f'{firebase}/chatDB/{destino}.json', data=json.dumps(dados))

    #CRIA UM NÓ NO DB
    def criar_no(cpf):
        print(cpf)
        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'
        #firebase = 'https://lelisprestadordb-default-rtdb.firebaseio.com' 
        # Dados a serem adicionados ao nó
        dados = {
            "cpf": cpf,
            "outros_dados": "valor",
            "mais_dados": "outro_valor"
            #dados adicionais PARA enviar
        }
        response = requests.put(f'{firebase}/prestadorDB.json', data=json.dumps(dados))
        print(response)

    #RECUPERA TODAS AS MENSAGEM DE DETERMINADO DESTINATÁRIO
    def recuperar_texto_mensagens(destinatario_email):
            firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'

            destino = ChatManager.format_email(destinatario_email)

            # Faz uma solicitação GET para recuperar todas as mensagens do destinatário
            response = requests.get(f'{firebase}/chatDB/{destino}.json')

            if response.status_code == 200:
                data = response.json()
                if data:
                    for key, value in data.items():
                        if isinstance(value, dict) and 'mensagem' in value:
                            mensagem = value['mensagem']
                            texto = mensagem.get('texto', '')
                            print(f"Texto: {texto}")
                else:
                    print("Nenhuma mensagem encontrada.")
            else:
                print("Erro ao recuperar as mensagens.")

    #RECUPERA SO O TEXTO DA MENSAGEM com filtro apenas com remetente respectivo
    @staticmethod
    def recuperar_texto_mensagens_chat(destinatario_email, remetente_email):
        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'
        destinatario = ChatManager.format_email(destinatario_email)
        remetente = ChatManager.format_email(remetente_email)

        response = requests.get(f'{firebase}/chatDB/{destinatario}.json')
        if response.status_code == 200:
            data = response.json()
            mensagens = []
            if data:
                for value in data.values():
                    if 'mensagem' in value:
                        mensagem = value['mensagem']
                        destinatario_db = mensagem['destinatario']
                        remetente_db = mensagem['remetente']
                        if destinatario == destinatario_db and remetente_db == remetente:
                            # Ajusta o formato do timestamp
                            timestamp = mensagem['timestamp']
                            # Formata o timestamp para exibição (HH:MM)
                            hora_formatada = timestamp[11:16]  # Obtém apenas a parte do horário (HH:MM)
                            mensagens.append({
                                'texto': mensagem['texto'],
                                'timestamp': hora_formatada
                            })
            return mensagens
        return []
   
