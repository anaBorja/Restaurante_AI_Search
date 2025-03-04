import os
import json
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Cargar variables de entorno
load_dotenv()
COSMOSDB_CONNECTION_STRING = os.getenv("COSMOSDB_CONNECTION_STRING")
BLOB_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Conectar a CosmosDB
client = MongoClient(COSMOSDB_CONNECTION_STRING)
db = client["restaurantedb"]
collection = db["menus2"]  # Asegúrate de que la colección esté bien configurada

# Conectar a Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
container_name = "menusextraido"  # Contenedor donde están los JSON extraídos

def download_json_from_blob(blob_name):
    """Descarga el JSON desde Azure Blob Storage y lo devuelve como diccionario."""
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        json_data = blob_client.download_blob().readall()
        return json.loads(json_data)
    except Exception as e:
        print(f"❌ Error al descargar JSON desde Blob Storage: {e}")
        return None

def store_menu_in_cosmos(menu_json):
    """Almacena el menú en CosmosDB sin la necesidad de la shard key."""
    try:
        if not menu_json:
            print("⚠️ No hay datos para insertar en CosmosDB.")
            return

        # Obtener la fecha actual en formato YYYY-MM-DD
        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        # Obtener nombre del restaurante para el _id (si es necesario)
        nombre_restaurante = menu_json.get("restaurante", "desconocido").replace(" ", "_")

        # Crear ID único combinando fecha y nombre del restaurante
        menu_json["_id"] = f"{fecha_actual}_{nombre_restaurante}"

        # Insertar en CosmosDB
        collection.insert_one(menu_json)
        print(f"✅ Menú guardado en CosmosDB con ID: {menu_json['_id']}")
    except Exception as e:
        print(f"❌ Error al guardar en CosmosDB: {e}")

# Nombre del archivo JSON en el contenedor (ajusta esto según tu lógica de nombres)
blob_name = "restaurante_el_buen_sabor.json"

# Descargar JSON y almacenarlo en CosmosDB
menu_json = download_json_from_blob(blob_name)
store_menu_in_cosmos(menu_json)
