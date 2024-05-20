import requests
import json
import datetime
from model.chatManager import ChatManager


class EmailManager:

    #uso na MANIPULAÇÃO DAS MENSAGENS DO CHAT
            ####from model.chatManager import ChatManager

            ####ChatManager.criar_conversa('remetente2@email.com', 'destinatario2@email.com')
            ####ChatManager.recuperar_mensagens('destinatario2@email.com')
            ####ChatManager.recuperar_texto_mensagens('destinatario2@email.com')
            ####ChatManager.recuperar_textos_por_remetente('destinatario2@email.com', 'remetente2@email.com')
            ####ChatManager.recuperar_textos_por_remetente_hhmm('destinatario2@email.com', 'remetente2@email.com')

            #cria um no passando o cpf
            ####criaNo = ChatManager.criar_no(cpf) 


    #formata o email para fazer uso no db
    def format_email(email):
        return email.replace('@', '_a_').replace('.', '_')
            
    #formata o email de retorno do db
    def format_email_back(email):
        return email.replace('_a_', '@').replace('_', '.')      
     
    #cria as mensagens no db
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


    def criar_no(cpf):
        print(cpf)

        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'
        #firebase = 'https://lelisprestadordb-default-rtdb.firebaseio.com' 

            # Dados a serem adicionados ao nó
        dados = {
            "cpf": cpf,
            "outros_dados": "valor",
            "mais_dados": "outro_valor"
            # Adicione aqui os dados adicionais que deseja enviar
        }


        response = requests.put(f'{firebase}/prestadorDB.json', data=json.dumps(dados))
        print(response)

    #recupera as mensagens no db
    def recuperar_mensagens(destinatario_email):
        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'

        destino = ChatManager.format_email(destinatario_email)

        # Faz uma solicitação GET para recuperar todas as mensagens do destinatário
        response = requests.get(f'{firebase}/chatDB/{destino}.json')

        if response.status_code == 200:
            data = response.json()
            if data:
                print(f"Mensagens para {destino}:")
                for key, value in data.items():
                    if isinstance(value, dict) and 'mensagem' in value:
                        mensagem = value['mensagem']
                        print(f"Texto: {mensagem['texto']}, Remetente: {mensagem['remetente']}, Timestamp: {mensagem['timestamp']}")
            else:
                print("Nenhuma mensagem encontrada.")
        else:
            print("Erro ao recuperar as mensagens.")


    #RECUPERA SO O TEXTO DA MENSAGEM
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
    def recuperar_textos_por_remetente(destinatario_email, remetente_email):
        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'
        
        destino = ChatManager.format_email(destinatario_email)

        origem = ChatManager.format_email(remetente_email)
        
        # Faz uma solicitação GET para recuperar todas as mensagens do destinatário
        response = requests.get(f'{firebase}/chatDB/{destino}.json')
        data = response.json()
        if data:
                print(f"Textos das mensagens para {destino} enviadas por {origem}:")
                for key, value in data.items():
                    if isinstance(value, dict):
                        mensagem = value.get('mensagem') 
                        if mensagem:
                            remetente = mensagem.get('remetente')
                            texto = mensagem.get('texto')
                            if remetente == origem:
                                print(texto)
                        else:
                            print("Nenhuma mensagem encontrada.")
        else:
            print("Nenhuma mensagem encontrada.")

    def recuperar_textos_por_remetente_hhmm(destinatario_email, remetente_email):
        firebase = 'https://lelisjobschatdb-default-rtdb.firebaseio.com'
        
        destino = ChatManager.format_email(destinatario_email)
        origem = ChatManager.format_email(remetente_email)
        
        # Faz uma solicitação GET para recuperar todas as mensagens do destinatário
        response = requests.get(f'{firebase}/chatDB/{destino}.json')
        data = response.json()
        
        if data:
            print(f"Textos das mensagens para {destinatario_email} enviadas por {remetente_email}:")
            for key, value in data.items():
                if isinstance(value, dict):
                    mensagem = value.get('mensagem') 
                    if mensagem:
                        remetente = mensagem.get('remetente')
                        texto = mensagem.get('texto')
                        if remetente == origem:
                            timestamp = mensagem.get('timestamp')
                            hora = datetime.datetime.fromisoformat(timestamp).strftime('%H:%M')
                            print(f"Texto: {texto}")
                            print(f"Hora: {hora}")
                    else:
                        print("Nenhuma mensagem encontrada.")
        else:
            print("Nenhuma mensagem encontrada.")