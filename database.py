from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://juan:pablo@cluster0.1cf3m.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
