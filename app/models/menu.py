from main               import db
from models.restaurante import Restaurante
from sqlalchemy         import CheckConstraint

class Menu(db.Model):
    cod_menu        = db.Column(db.Integer, primary_key=True)
    nom_menu        = db.Column(db.Text)
    costo           = db.Column(db.Float)
    tipo            = db.Column(db.Text, nullable=False, default='default')
    cod_restaurante = db.Column(db.Integer, db.ForeignKey(Restaurante.cod_restaurante))

    __table_args__  = (CheckConstraint('tipo IN ("default", "personalizado")'),)

    productos       = db.relationship('Producto_Menu', backref='menu', lazy='dynamic')
    pedidos         = db.relationship('Menu_Pedido', backref='menu', lazy='dynamic')


    def __init__(self, nom_menu, costo, cod_restaurante, tipo=None):
        self.nom_menu        = nom_menu
        self.costo           = costo
        self.tipo            = tipo
        self.cod_restaurante = cod_restaurante
