from main          import db
from models.menu   import Menu
from models.pedido import Pedido

class Menu_Pedido(db.Model):
    cod_menu_pedido = db.Column(db.Integer, primary_key=True)
    cod_menu        = db.Column(db.Integer, db.ForeignKey(Menu.cod_menu))
    cod_pedido      = db.Column(db.Integer, db.ForeignKey(Pedido.cod_pedido))
    
    def __init__(self, cod_menu, cod_pedido):
        self.cod_menu   = cod_menu
        self.cod_pedido = cod_pedido