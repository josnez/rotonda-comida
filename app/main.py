from flask            import Flask
from flask_restful    import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave'

""" Database configurations """
directory = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directory, 'rotondacomidas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)

class Restaurante(Resource):
    def get(self, value):
        return {'result': 'succes'}

#@app.route("/")
def init():
    return "render_template('portada.html')"

#@app.route("/login")
def login():
    return "render_template('logIn.html')"

#@app.route("/registro/restaurante")
def registro_restaurante():
    return "render_template('registroRestaurante.html')"

#@app.route("/registro/producto")
def registro_producto():
    return "Registro producto"

#@app.route("/registro/menu")
def registro_menu():
    return "Registro menu"

#@app.route("/consulta/productos")
def consulta_productos():
    return "Consulta productos"

#@app.route("/consulta/ingredientes")
def consulta_ingredientess():
    return "Consulta ingredientes"

api.add_resource(Restaurante, '/restaurante/<string:value>')

if __name__ == "__main__":
    app.run(debug=True)