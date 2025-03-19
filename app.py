from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Producto

app = Flask(__name__)
db = dbase.dbConection()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products', methods=['POST'])
def addproduct():
    products = db['products']
    nombre = request.form['nombre']
    titulo = request.form['titulo']
    autor = request.form['autor']

    if nombre and titulo and autor:
        product = Producto(nombre, titulo, autor)
        products.insert_one(product.paraConexiondb())
        return redirect(url_for('home'))
    else:
        return notfound()

@app.route('/usuarios', methods=['POST'])
def addusuario():
    usuarios = db['usuarios']
    nombre = request.form['nombre']
    correo = request.form['correo']
    celular = request.form['celular']

    if nombre and correo and celular:
        usuario = {'nombre': nombre, 'correo': correo, 'celular': celular}
        usuarios.insert_one(usuario)
        return redirect(url_for('home'))
    else:
        return notfound()

@app.route('/prestamos', methods=['POST'])
def addprestamo():
    prestamos = db['prestamos']
    dia = request.form['dia']
    hora = request.form['hora']
    libro = request.form['libro']

    if dia and hora and libro:
        prestamo = {'dia': dia, 'hora': hora, 'libro': libro}
        prestamos.insert_one(prestamo)
        return redirect(url_for('home'))
    else:
        return notfound()

@app.errorhandler(404)
def notfound(error=None):
    message = {
        'mensaje': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)