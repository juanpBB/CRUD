from pymongo import MongoClient 
import certifi
MONGO_URI='mongodb+srv://juan:<Lukas010827>@cluster0.1cf3m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
ca= certifi.where()

def dbConection():
    try:
        client= MongoClient._connect(MONGO_URI,tlsCAFile=ca) #asi se crea una conexion a la base de datos,
        #el ca sigo sin entender porque pasa o para que es pero sigamos
        db= client["ddb_produc_app"]
    except:
        print("error de conexion a la base de datos")
    return db
    

