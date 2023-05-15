from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField

class LogIn(FlaskForm):
    usuario = StringField("usuario")
    enviar = SubmitField("enviar")