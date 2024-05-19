from kivymd.uix.screen import MDScreen


class FavoritosScreen(MDScreen):
    pass

    def tela_alvenaria(self):
        self.manager.current = "alvenariaScreen"

    def tela_hidraulica(self):
        self.manager.current = "hidraulicaScreen"

    def tela_eletrica(self):
        self.manager.current = "eletricaScreen"

    def tela_cuidados(self):
        self.manager.current = "cuidadosScreen"

    def tela_pet(self):
        self.manager.current = "petScreen"

    def tela_tech(self):
        self.manager.current = "techScreen"
        
    def tela_limpeza(self):
        self.manager.current = "limpezaScreen"

    def tela_jardinagem(self):
        self.manager.current = "jardinagemScreen"

    def tela_outros(self):
        self.manager.current = "outrosScreen"
        
    def voltar_para_home(self):
        self.manager.current = "teladoisScreen"
        
    def editaPerfil(self):
        self.manager.current = "editarperfilScreen"
        
    def favoritos(self):
        self.manager.current = "favoritosScreen"
        
    def listar(self):
        self.manager.current = "listartodosScreen"
