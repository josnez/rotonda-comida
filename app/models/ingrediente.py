from main import db

class Ingrediente(db.Model):
    cod_ingrediente = db.Column(db.Integer, primary_key=True)
    nom_ingrediente = db.Column(db.Text)
    
    menus           = db.relationship('Producto_Ingrediente', backref='ingrediente', lazy='dynamic')

    def __init__(self,nom_ingrediente):
        self.nom_ingrediente = nom_ingrediente