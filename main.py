from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave'

@app.route("/")
def init():
    return render_template('portada.html')

@app.route("/registro/restaurante")
def registro_restaurante():
    return render_template('registroRestaurante.html')

@app.route("/registro/producto")
def registro_producto():
    return "Registro producto"

@app.route("/registro/menu")
def registro_menu():
    return "Registro menu"

@app.route("/consulta/productos")
def consulta_productos():
    return "Consulta productos"

@app.route("/consulta/ingredientes")
def consulta_ingredientess():
    return "Consulta ingredientes"

if __name__ == "__main__":
    app.run(debug=True)