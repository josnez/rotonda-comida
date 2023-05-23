from main            import db
from models.producto import Producto
from models.menu     import Menu

class Producto_Menu(db.Model):
    cod_producto_menu = db.Column(db.Integer, primary_key=True)
    cod_producto      = db.Column(db.Integer, db.ForeignKey(Menu.cod_menu))
    cod_menu          = db.Column(db.Integer, db.ForeignKey(Producto.cod_producto))

    ingredientes      = db.relationship('Producto_Ingrediente', backref='producto', lazy='dynamic')

    def __init__(self, cod_producto, cod_menu):
        self.cod_producto = cod_producto
        self.cod_menu     = cod_menu