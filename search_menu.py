import requests
import os
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()

# Variables de configuración
search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")  # Reemplazar con tu endpoint de Azure AI Search
api_key = os.getenv("AZURE_SEARCH_API_KEY")  # Reemplazar con tu API Key de Azure AI Search
index_name = "cosmosdb-index"  # El nombre del índice que creaste

# Función para realizar la búsqueda
def search_menu(query="*"):
    # Encabezados para la solicitud
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    # Consulta de búsqueda
    search_url = f"{search_endpoint}/indexes/{index_name}/docs/search?api-version=2021-04-30-Preview"
    search_payload = {
        "search": query,
        "select": "restaurante, direccion, bebida, precio, menu_del_dia",
        "top": 5  # Limitar a los 5 primeros resultados
    }

    # Realizar la solicitud de búsqueda
    response = requests.post(search_url, json=search_payload, headers=headers)

    # Comprobar y devolver los resultados
    if response.status_code == 200:
        return response.json().get('value', [])
    else:
        print(f"Error en la búsqueda: {response.status_code}, {response.text}")
        return []

# Función para mostrar los resultados de búsqueda de manera más amigable
def format_results(results):
    formatted = []
    for doc in results:
        restaurant_info = f"Restaurante: {doc['restaurante']}\n"
        restaurant_info += f"Dirección: {doc['direccion']}\n"
        restaurant_info += f"Bebida: {doc['bebida']}\n"
        restaurant_info += f"Precio: {doc['precio']}\n"
        
        # Mostrar los platos del menú del día
        menu_info = ""
        if 'menu_del_dia' in doc:
            for menu in doc['menu_del_dia']:
                menu_info += f"Plato: {menu['plato']} - Nombre: {menu['nombre']}\n"
        
        formatted.append(restaurant_info + menu_info + "-"*50)
    
    return formatted
