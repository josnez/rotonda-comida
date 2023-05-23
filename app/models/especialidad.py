from main import db

class Especialidad(db.Model):
    cod_especialidad = db.Column(db.Integer, primary_key=True)
    nom_especialidad = db.Column(db.Text)
    restaurantes     = db.relationship('Restaurante', backref='especialidad', lazy='dynamic')

    def __init__(self, nom_especialidad):
        self.nom_especialidad = nom_especialidad

    def __repr__(self):
        return "Especialidad - codigo: {} nombre: {}".format(self.cod_especialidad, self.nom_especialidad)

        