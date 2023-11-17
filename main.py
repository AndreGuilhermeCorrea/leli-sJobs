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
     
    }

    #classes que controlam os kv's
    CLASSES = {
        "MainScreenManager": "controller.screenmanager",
        
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