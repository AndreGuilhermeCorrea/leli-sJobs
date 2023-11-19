from kivymd.uix.screen import MDScreen
import sys


class TelaDoisScreen(MDScreen):
    pass

    def tela_servicos(self):
        self.manager.current = "servicosScreen"
        
    def tela_login(self):
        self.manager.current = "login" 
        
    def sair(self):
        sys.exit()   