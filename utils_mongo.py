from pymongo import MongoClient
import pandas as pd

def conectar_mongo(uri, base, coleccion):
    """Conecta a MongoDB y devuelve un objeto de colección."""
    cliente = MongoClient(uri)
    db = cliente[base]
    col = db[coleccion]
    return col

def obtener_datos(coleccion):
    """Convierte la colección MongoDB en un DataFrame."""
    data = list(coleccion.find({}, {"_id": 0}))  # excluye el ObjectId
    return pd.DataFrame(data)
