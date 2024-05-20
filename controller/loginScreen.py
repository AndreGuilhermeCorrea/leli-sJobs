import sys
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from model.data import data
from model.emailUser import EmailUser


class LoginScreen(MDScreen):
    pass
  
    def on_login(self):
        #Recebe dados dos textfields     
        cpf = self.manager.get_screen('login').ids.cpf.text
        senha = self.manager.get_screen('login').ids.password.text    
        
        testeCampos = self.teste_campos(cpf,senha)
        
        if(testeCampos == True):
           self.teste(cpf,senha) 
   
    def teste(self, cpf, senha):
        
        error_label = self.ids.error_label
        dadosDb = data.checking(cpf, senha)
        
        if(dadosDb == True):
            EmailUser.set_cpf(cpf)

            self.manager.current = "teladoisScreen"
            self.limpar_dados()
        else:   
            error_label.text = "Dados nao conferem"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)

def teste_campos(self, cpf, senha):

        error_label = self.ids.error_label       
        
        if(cpf == '')and( senha == ''):
            error_label.text = "Insira os dados para logar"
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False
        elif(senha == ''):
            error_label.text = "Insira a senha para logar"
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False
        elif(cpf == '' ):           
            error_label.text = "Insira o CPF para logar"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False
        elif(len(cpf) != 11 ):           
            error_label.text = "Dados incorretos"  
            Clock.schedule_once(lambda dt: self.limpar_erro_label(), 2)
            return False
        else:
            return True
            
    def limpar_erro_label(self):
        # Limpe o texto da label
        self.ids.error_label.text = ""
        self.ids.cpf.text = ""  
        self.ids.password.text = ""
        
    def limpar_dados(self):
        self.ids.cpf.text = ""  
        self.ids.password.text = ""
        
    def sair(self):
        sys.exit()
        
    def cadastrar(self):
        self.manager.current = "cadastrarScreen"


