from main import db

class Categoria(db.Model):
    cod_categoria = db.Column(db.Integer, primary_key=True)
    nom_categoria = db.Column(db.Text)

    productos     = db.relationship('Producto', backref='categoria', lazy='dynamic')

    def __init__(self, nom_categoria):
        self.nom_categoria   = nom_categoria
