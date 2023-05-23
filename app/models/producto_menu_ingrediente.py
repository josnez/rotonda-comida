from main import db
from models.producto_menu import Producto_Menu
from models.ingrediente import Ingrediente

class Producto_Ingrediente(db.Model):
    cod_producto_ingrediente = db.Column(db.Integer, primary_key=True)
    cod_producto_menu        = db.Column(db.Integer, db.ForeignKey(Producto_Menu.cod_producto_menu))
    cod_ingrediente          = db.Column(db.Integer, db.ForeignKey(Ingrediente.cod_ingrediente))

    def __init__(self, cod_producto_menu, cod_ingrediente):
        self.cod_producto_menu = cod_producto_menu
        self.cod_ingrediente   = cod_ingrediente