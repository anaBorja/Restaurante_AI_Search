import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "menus"

def upload_pdf(file_path):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=os.path.basename(file_path))

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"✅ {file_path} subido correctamente.")

# Prueba
upload_pdf("El Buen Sabor 1.pdf")
