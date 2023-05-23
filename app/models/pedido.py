from main                import db
from models.carro_compra import Carro_Compra

class Pedido(db.Model):
    cod_pedido        = db.Column(db.Integer, primary_key=True)
    costo_total       = db.Column(db.Float)
    cod_carro_compra  = db.Column(db.Integer, db.ForeignKey(Carro_Compra.cod_carro_compra))

    carritos             = db.relationship('Menu_Pedido', backref='pedido', lazy='dynamic')

    def __init__(self, costo_total, cod_carro_compra):
        self.costo_total = costo_total
        self.cod_carro_compra = cod_carro_compra
