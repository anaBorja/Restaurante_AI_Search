import os
import requests
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
AI_SEARCH_SERVICE = os.getenv("AI_SEARCH_SERVICE")
AI_SEARCH_ADMIN_KEY = os.getenv("AI_SEARCH_ADMIN_KEY")
INDEX_NAME = "menus-index"

url = f"https://{AI_SEARCH_SERVICE}.search.windows.net/indexes/{INDEX_NAME}?api-version=2023-07-31"
headers = {
    "Content-Type": "application/json",
    "api-key": AI_SEARCH_ADMIN_KEY
}

index_definition = {
    "name": INDEX_NAME,
    "fields": [
        {"name": "id", "type": "Edm.String", "key": True},
        {"name": "plato", "type": "Edm.String", "searchable": True},
        {"name": "ingredientes", "type": "Edm.String", "searchable": True},
        {"name": "precio", "type": "Edm.Double"}
    ]
}

response = requests.put(url, headers=headers, json=index_definition)
print("✅ AI Search configurado:", response.json())
import os
import requests
from dotenv import load_dotenv

# Cargar credenciales
load_dotenv()
AI_SEARCH_SERVICE = os.getenv("AI_SEARCH_SERVICE")
AI_SEARCH_ADMIN_KEY = os.getenv("AI_SEARCH_ADMIN_KEY")
INDEX_NAME = "menus-index"

url = f"https://{AI_SEARCH_SERVICE}.search.windows.net/indexes/{INDEX_NAME}?api-version=2023-07-31"
headers = {
    "Content-Type": "application/json",
    "api-key": AI_SEARCH_ADMIN_KEY
}

index_definition = {
    "name": INDEX_NAME,
    "fields": [
        {"name": "id", "type": "Edm.String", "key": True},
        {"name": "plato", "type": "Edm.String", "searchable": True},
        {"name": "ingredientes", "type": "Edm.String", "searchable": True},
        {"name": "precio", "type": "Edm.Double"}
    ]
}

response = requests.put(url, headers=headers, json=index_definition)
print("✅ AI Search configurado:", response.json())
