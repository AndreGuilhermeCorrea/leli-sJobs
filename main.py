import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

# main app class for kaki app with kivymd modules
class LelisApp(MDApp, App):

    #variável de ambiente
    DEBUG = 1 # set this to 0 make live app not working

    #arquivos kv (telas)
    KV_FILES = {
        os.path.join(os.getcwd(), "view/screenmanager.kv"),
        os.path.join(os.getcwd(), "view/loginScreen.kv"),
        os.path.join(os.getcwd(), "view/servicosScreen.kv"),
        os.path.join(os.getcwd(), "view/alvenariaScreen.kv"),
        os.path.join(os.getcwd(), "view/hidraulicaScreen.kv"),
        os.path.join(os.getcwd(), "view/eletricaScreen.kv"),
        os.path.join(os.getcwd(), "view/cuidadosScreen.kv"),
        os.path.join(os.getcwd(), "view/petScreen.kv"),
        os.path.join(os.getcwd(), "view/techScreen.kv"),
        os.path.join(os.getcwd(), "view/limpezaScreen.kv"),
        os.path.join(os.getcwd(), "view/jardinagemScreen.kv"),
        os.path.join(os.getcwd(), "view/outrosScreen.kv"),
        os.path.join(os.getcwd(), "view/cadastrarScreen.kv"),
        os.path.join(os.getcwd(), "view/teladoisScreen.kv"),
        os.path.join(os.getcwd(), "view/editarperfilScreen.kv"),
        os.path.join(os.getcwd(), "view/favoritosScreen.kv"),
        os.path.join(os.getcwd(), "view/listartodosScreen.kv"),      
  
    }

    #classes que controlam os kv's
    CLASSES = {
        "MainScreenManager": "controller.screenmanager",
        "LoginScreen": "controller.loginScreen",
        "ServicosScreen": "controller.servicosScreen",
        "AlvenariaScreen": "controller.alvenariaScreen",
        "HidraulicaScreen": "controller.hidraulicaScreen",
        "EletricaScreen": "controller.eletricaScreen",
        "CuidadosScreen": "controller.cuidadosScreen",
        "PetScreen": "controller.petScreen",
        "TechScreen": "controller.techScreen",
        "LimpezaScreen": "controller.limpezaScreen",
        "JardinagemScreen": "controller.jardinagemScreen",
        "OutrosScreen": "controller.outrosScreen",
        "CadastrarScreen": "controller.cadastrarScreen",
        "TelaDoisScreen": "controller.teladoisScreen",
        "EditarPerfilScreen": "controller.editarperfilScreen",
        "FavoritosScreen": "controller.favoritosScreen",
        "ListarTodosScreen": "controller.listartodosScreen",        
   
        
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    #método de construção da classe
    def build_app(self):
        
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="Blue"        
        #gerenciador de telas principal
        return Factory.MainScreenManager()

#roda o app
if __name__ == "__main__":
    LelisApp().run()