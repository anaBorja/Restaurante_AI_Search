import os
import requests
import json
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
DOCUMENT_INTELLIGENCE_KEY = os.getenv("DOCUMENT_INTELLIGENCE_KEY")
MODEL_ID = os.getenv("DOCUMENT_INTELLIGENCE_MODEL_ID")
BLOB_PDF_URL = os.getenv("BLOB_PDF_URL")  # URL del PDF en Azure Blob

print("Endpoint:", DOCUMENT_INTELLIGENCE_ENDPOINT)
print("Modelo ID:", MODEL_ID)

def extract_menu():
    url = f"{DOCUMENT_INTELLIGENCE_ENDPOINT}/formrecognizer/documentModels/{MODEL_ID}:analyze?api-version=2022-08-31"

    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": DOCUMENT_INTELLIGENCE_KEY
    }
    body = {"urlSource": BLOB_PDF_URL}

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 202:
        # Si la solicitud fue aceptada, espera el análisis
        result = response.json()
        print("✅ Extracción realizada:")
        print(json.dumps(result, indent=2))
        return result
    elif response.status_code == 400:
        print("❌ Error en la solicitud: Solicitud incorrecta")
        print(response.json())
    elif response.status_code == 401:
        print("❌ Error en la solicitud: No autorizado (verifica las credenciales)")
        print(response.json())
    elif response.status_code == 404:
        print("❌ Error en la solicitud: No se encontró el recurso (verifica el endpoint y el modelo)")
        print(response.json())
    else:
        print(f"❌ Error desconocido: {response.status_code}")
        print(response.json())

# Prueba
menu_json = extract_menu()