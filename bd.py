from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener el URI desde la variable de entorno
uri = os.getenv("MONGO_URI")

# Validar la existencia del URI
if not uri:
    raise ValueError("⚠️ ERROR: No se encontró la variable de entorno MONGO_URI. Asegúrate de tener tu archivo .env")

# Conectar con MongoDB
try:
    client = MongoClient(uri)
    db = client["peliculasDB"]
    coleccion = db["peliculas"]
except Exception as e:
    print("❌ Error al conectar con MongoDB:", e)

# ---- FUNCIONES CRUD ----

def agregar_pelicula(titulo, año, genero):
    data = {"titulo": titulo, "año": año, "genero": genero}
    coleccion.insert_one(data)

def obtener_peliculas():
    return list(coleccion.find())

def eliminar_pelicula(titulo):
    coleccion.delete_one({"titulo": titulo})

def modificar_pelicula(titulo_original, nuevo_titulo, nuevo_año, nuevo_genero):
    coleccion.update_one(
        {"titulo": titulo_original},
        {"$set": {"titulo": nuevo_titulo, "año": nuevo_año, "genero": nuevo_genero}}
    )
