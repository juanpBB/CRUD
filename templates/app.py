from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase #esto sirve para darle a entender que es una base de datos (creo)
from product import Product #esto sirve para que nosotros le demos la clase y cumpla con sus funciones, es decir importamos la funcion en nuestra app

#methodo post
app= Flask(__name__)
db= dbase.dbConection() #esta es la conexion de la base de datos

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products', methods=['POST'])
def addproduct():
    products = db['products'] #asi se crea la collection
    nombre = request.form['nombre'] #se toma los datos de la casilla del formulario 'nombre'
    titulo= request.form['titulo'] #se toma los datos de la casilla del formulario 'titulo'
    autor=request.form['autor'] #se toma los datos de la casilla del formulario 'autor'

    if nombre and titulo and autor:
        products = products(nombre,titulo,autor)
        products.insert_one(products.paraConexiondb())
        Response= jsonify({
            'nombre': nombre,
            'autor':autor,
            'titulo':titulo
        })
        return redirect(url_for('home'))
    else:
        return notfound()
@app.errorhandler(404)
def notfound (error=None):
    message={
        'mensaje': 'no encontreado' + request.url,
        'status': '404 not found'
    }
    Response =jsonify(message)
    Response.status_code=404
    return Response
if __name__ == '__main__':
    app.run(debug=True, port=5000)
# todos estos pasos, desde crear el template, hasta crear el render_template que sirve para darle origen a la primera pagina que se vera.
