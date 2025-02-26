<<<<<<< HEAD
import os
import requests
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
AI_SEARCH_SERVICE = os.getenv("AI_SEARCH_SERVICE")
AI_SEARCH_QUERY_KEY = os.getenv("AI_SEARCH_QUERY_KEY")
INDEX_NAME = "menus-index"

def search_plato(plato):
    url = f"https://{AI_SEARCH_SERVICE}.search.windows.net/indexes/{INDEX_NAME}/docs?api-version=2023-07-31&search={plato}"
    headers = {
        "api-key": AI_SEARCH_QUERY_KEY,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    results = response.json()

    print(f"🔍 Resultados para '{plato}':")
    for item in results["value"]:
        print(f"🍽 {item['plato']} - ${item['precio']}")

# Prueba
search_plato("pollo")
=======
import os
import requests
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
AI_SEARCH_SERVICE = os.getenv("AI_SEARCH_SERVICE")
AI_SEARCH_QUERY_KEY = os.getenv("AI_SEARCH_QUERY_KEY")
INDEX_NAME = "menus-index"

def search_plato(plato):
    url = f"https://{AI_SEARCH_SERVICE}.search.windows.net/indexes/{INDEX_NAME}/docs?api-version=2023-07-31&search={plato}"
    headers = {
        "api-key": AI_SEARCH_QUERY_KEY,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    results = response.json()

    print(f"🔍 Resultados para '{plato}':")
    for item in results["value"]:
        print(f"🍽 {item['plato']} - ${item['precio']}")

# Prueba
search_plato("pollo")
>>>>>>> 50a6ce4ff93ae97f1d760f2a7d8a12f964322346
