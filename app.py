from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
    conn = dbase.dbConnection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    productsReceived = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=productsReceived)

# Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    conn = dbase.dbConnection()
    cursor = conn.cursor()
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
            (name, price, quantity)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    else:
        return notFound()

# Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    conn = dbase.dbConnection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE name = %s", (product_name,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    conn = dbase.dbConnection()
    cursor = conn.cursor()
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        cursor.execute(
            "UPDATE products SET name = %s, price = %s, quantity = %s WHERE name = %s",
            (name, price, quantity, product_name)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=3600)