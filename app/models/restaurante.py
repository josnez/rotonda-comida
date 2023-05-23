from main                import db
from models.especialidad import Especialidad

class Restaurante(db.Model):
    cod_restaurante  = db.Column(db.Integer, primary_key=True)
    nom_restaurante  = db.Column(db.Text)
    cod_especialidad = db.Column(db.Integer, db.ForeignKey(Especialidad.cod_especialidad))
    
    menus            = db.relationship('Menu', backref='restaurante', lazy='dynamic')

    def __init__(self, nom_restaurante, cod_especialidad):
        self.nom_restaurante = nom_restaurante
        self.cod_especialidad = cod_especialidad

    def __repr__(self):
        return "Restaurante - codigo: {} nombre: {} cod especialidad: {}".format(
            self.cod_restaurante, self.nom_restaurante, self.cod_especialidad
        )