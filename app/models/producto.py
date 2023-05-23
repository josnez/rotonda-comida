from main             import db
from models.categoria import Categoria

class Producto(db.Model):
    cod_producto  = db.Column(db.Integer, primary_key=True)
    nom_producto  = db.Column(db.Text)
    costo         = db.Column(db.Float)
    cod_categoria = db.Column(db.Integer, db.ForeignKey(Categoria.cod_categoria))

    menus         = db.relationship('Producto_Menu', backref='producto', lazy='dynamic')

    def __init__(self, nom_producto, costo, cod_categoria):
        self.nom_producto  = nom_producto
        self.costo         = costo
        self.cod_categoria = cod_categoria