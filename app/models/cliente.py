from main import db

class Cliente(db.Model):
    cod_cliente      = db.Column(db.Integer, primary_key=True)
    nom_cliente      = db.Column(db.Text)
    apellido_cliente = db.Column(db.Text)
    dir_cliente      = db.Column(db.Text)

    compras          = db.relationship('Carro_Compra', backref='cliente', lazy='dynamic')

    def __init__(self, nom_cliente, apellido_cliente, dir_cliente):
        self.nom_cliente      = nom_cliente
        self.apellido_cliente = apellido_cliente
        self.dir_cliente      = dir_cliente

