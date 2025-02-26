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
collection = db["menus"]

# Conectar a Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
container_name = "menusextraido"  # Contenedor donde están los JSON extraídos

def download_json_from_blob(blob_name):
    """Descarga el JSON desde Azure Blob Storage y lo devuelve como diccionario."""
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        json_data = blob_client.download_blob().readall()
        print(json_data)
        return json.loads(json_data)
    except Exception as e:
        print(f"❌ Error al descargar JSON desde Blob Storage: {e}")
        return None

def store_menu_in_cosmos(menu_json):
    """Asegura que el JSON contenga la shard key antes de guardarlo en CosmosDB."""
    try:
        if not menu_json:
            print("⚠️ No hay datos para insertar en CosmosDB.")
            return

        # Obtener la fecha actual en formato YYYY-MM-DD
        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        # Obtener nombre del restaurante (clave de partición en CosmosDB)
        nombre_restaurante = menu_json.get("restaurante", "desconocido").replace(" ", "_")

        # Si la shard key es "plato", asegurar que cada documento tenga ese campo
        if "plato" not in menu_json:
            menu_json["plato"] = "N/A"  # Valor por defecto si falta

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
