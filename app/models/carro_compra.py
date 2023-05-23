from main           import db
from models.cliente import Cliente

class Carro_Compra(db.Model):
    cod_carro_compra = db.Column(db.Integer, primary_key=True)
    costo_total      = db.Column(db.Float)
    cod_cliente      = db.Column(db.Integer, db.ForeignKey(Cliente.cod_cliente))

    pedidos          = db.relationship('Pedido', backref='carrito', lazy='dynamic')

    def __init__(self, costo_total, cod_cliente):
        self.costo_total = costo_total
        self.cod_cliente = cod_cliente
    