from kivymd.uix.screen import MDScreen
from model.cadastroDb import CadastroDb
from kivy.clock import Clock
import sys 

class CadastrarScreen(MDScreen):
    pass


    def cadastro_user(self):
     
        cpf = self.manager.get_screen('cadastrarScreen').ids.cpf.text
        senha = self.manager.get_screen('cadastrarScreen').ids.password1.text 
        senha2 = self.manager.get_screen('cadastrarScreen').ids.password2.text
        email =self.manager.get_screen('cadastrarScreen').ids.email.text
        nome =self.manager.get_screen('cadastrarScreen').ids.nome.text 
        sobrenome =self.manager.get_screen('cadastrarScreen').ids.sobrenome.text 
        testeCampos = self.teste_campos(cpf, senha,senha2, email, nome, sobrenome)
        
        if(testeCampos == True): 
            self.enviar(cpf, senha, email, nome, sobrenome)
    
    def enviar(self, cpf, senha, email, nome, sobrenome):       
            
        cadastrarDb = CadastroDb.cadastrar(cpf, senha, email, nome, sobrenome)            
        
        if(cadastrarDb == True):
            self.manager.current = "login"
            self.limpar_dados()   
        else:    
            CadastroDb.editar_usuario(cpf, senha, email, nome, sobrenome)
            self.limpar_dados()
            self.manager.current = "login"
            
    def teste_campos(self, cpf, senha, senha2, email, nome, sobrenome):
        error_label = self.ids.error_label         
        if(cpf == '')and(senha == '')and(senha2 =='')and(email =='')and(nome =='')and(sobrenome ==''):
            error_label.text = "Insira os dados para logar"
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False   
        elif(nome == '' ):           
            error_label.text = "Insira o NOME"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False               
        elif(sobrenome == '' ):           
            error_label.text = "Insira o SOBRENOME"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False                    
        elif(cpf == '' ):           
            error_label.text = "Insira o CPF"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False        
        elif(len(cpf) != 11 ):           
            error_label.text = "Dados incorretos"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False        
        elif(email == '' ):           
            error_label.text = "Insira o EMAIL"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False               
        elif(senha == ''):
            error_label.text = "Insira a senha"
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False        
        elif(senha2 == ''):
            error_label.text = "Insira a senha"
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False                                        
        elif(senha != senha2):           
            error_label.text = "Senhas divergentes"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False         
        else:
            return True
            
    def limpar_erro_label(self):
        # Limpe o texto da label
        self.ids.error_label.text = ""
        
    def limpar_dados(self):
        self.ids.nome.text= ""
        self.ids.sobrenome.text= ""
        self.ids.cpf.text = "" 
        self.ids.email.text = ""                 
        self.ids.password1.text= ""
        self.ids.password2.text= ""                        

    def tela_login(self):
        self.manager.current = "login"
        
    def sair(self):
        sys.exit()   