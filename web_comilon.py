import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Cargar credenciales desde .env
load_dotenv()
search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
api_key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = "cosmosdb3-index"

# Encabezados para la solicitud
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Interfaz en Streamlit
st.title("Buscador de Menús de Restaurantes 🍽️")
search_query = st.text_input("¿Qué plato estás buscando?", "")

if st.button("Buscar"):
    if search_query:
        search_url = f"{search_endpoint}/indexes/{index_name}/docs/search?api-version=2021-04-30-Preview"
        search_payload = {
            "search": search_query,
            "select": "restaurante, direccion, plato, bebida, precio",
            "top": 5
        }
        response = requests.post(search_url, json=search_payload, headers=headers)

        if response.status_code == 200:
            results = response.json()
            if results["value"]:
                for doc in results["value"]:
                    st.subheader(f"🍴 {doc['restaurante']}")
                    st.write(f"📍 Dirección: {doc['direccion']}")
                    st.write(f"🥘 Plato: {doc.get('plato', 'N/A')}")
                    st.write(f"🍹 Bebida: {doc.get('bebida', 'N/A')}")
                    st.write(f"💰 Precio: {doc['precio']} €")
                    st.markdown("---")
            else:
                st.warning("No se encontraron resultados.")
        else:
            st.error(f"Error en la búsqueda: {response.status_code}, {response.text}")
    else:
        st.warning("Por favor, ingresa un término de búsqueda.")
