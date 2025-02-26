import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
COSMOSDB_CONNECTION_STRING = os.getenv("COSMOSDB_CONNECTION_STRING")
client = MongoClient(COSMOSDB_CONNECTION_STRING)
db = client["restaurantedb"]
collection = db["menus"]

def store_menu(menu_json):
    try:
        collection.insert_one(menu_json)
        print("✅ Menú guardado en CosmosDB.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Prueba
store_menu(menu_json)
