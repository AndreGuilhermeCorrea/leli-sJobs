from kivymd.uix.screen import MDScreen
import sys

class HidraulicaScreen(MDScreen):
    pass

    def voltar_para_home(self):
        self.manager.current = "teladoisScreen"
        
    def editaPerfil(self):
        self.manager.current = "editarperfilScreen"
        
    def favoritos(self):
        self.manager.current = "favoritosScreen"
        
    def listar(self):
        self.manager.current = "listartodosScreen"
    
    def tela_cadastrados(self): 
        self.manager.current = "perfisScreen"

    def volta(self):
        self.manager.current = "servicosScreen"

    def sair(self):
        sys.exit()          
