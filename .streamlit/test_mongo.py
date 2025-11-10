from pymongo import MongoClient

uri = "mongodb://freddy_db_user:freddy1991@ac-fjs35ss-shard-00-00.cluster0.fjs35ss.mongodb.net:27017,ac-fjs35ss-shard-00-01.cluster0.fjs35ss.mongodb.net:27017,ac-fjs35ss-shard-00-02.cluster0.fjs35ss.mongodb.net:27017/recomendador_Deportes?ssl=true&replicaSet=atlas-fjs35ss-shard-0&authSource=admin&retryWrites=true&w=majority"

try:
    cliente = MongoClient(uri, serverSelectionTimeoutMS=10000)
    print("🟢 Intentando conectar con MongoDB Atlas...")
    info = cliente.server_info()
    print("✅ Conexión exitosa con MongoDB Atlas")
    print("Versión del servidor:", info["version"])
except Exception as e:
    print("❌ Error al conectar con MongoDB:", e)
