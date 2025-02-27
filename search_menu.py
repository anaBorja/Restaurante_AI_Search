import requests
import os
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()

# Variables de configuración
search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")  # Reemplazar con tu endpoint de Azure AI Search
api_key = os.getenv("AZURE_SEARCH_API_KEY")  # Reemplazar con tu API Key de Azure AI Search
index_name = "cosmosdb3-index"  # El nombre del índice que creaste

# Parámetros de búsqueda
search_query = "agua"

# Encabezados para la solicitud
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Consulta de búsqueda
search_url = f"{search_endpoint}/indexes/{index_name}/docs/search?api-version=2021-04-30-Preview"
search_payload = {
    "search": search_query,
    "select": "restaurante, direccion, plato, bebida, precio",
    "top": 5  # Limitar a los 5 primeros resultados
}

# Realizar la solicitud de búsqueda
response = requests.post(search_url, json=search_payload, headers=headers)

# Mostrar los resultados
if response.status_code == 200:
    results = response.json()
    for doc in results['value']:
        print(f"Restaurante: {doc['restaurante']}")
        print(f"Dirección: {doc['direccion']}")
        print(f"Plato: {doc.get('plato', 'N/A')}")
        print(f"Bebida: {doc.get('bebida', 'N/A')}")
        print(f"Precio: {doc['precio']}")
        print("-" * 50)
else:
    print(f"Error en la búsqueda: {response.status_code}, {response.text}")
