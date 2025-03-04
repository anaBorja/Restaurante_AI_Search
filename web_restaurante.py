import streamlit as st
from upload_pdf import * # Importamos la función de upload_pdf
from extract_menu import * # Importamos las funciones de extraction_menu
from store_in_cosmosdb import *  # Importamos las funciones de store_cosmodb

# Interfaz de usuario de Streamlit
st.title("Sistema de Gestión de Menús de Restaurantes")

# Subir archivo PDF
uploaded_file = st.file_uploader("Sube un archivo PDF de menú", type="pdf")

if uploaded_file is not None:
    # Guardar archivo localmente en el directorio temporal de Streamlit
    with open(f"./{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"El archivo {uploaded_file.name} ha sido subido exitosamente.")

    # Subir el PDF a Azure Blob Storage
    st.write("Subiendo el archivo a Azure Blob Storage...")
    upload_pdf(f"./{uploaded_file.name}")
    st.success(f"Archivo {uploaded_file.name} subido correctamente.")

    # Procesar el PDF y extraer la información
    st.write("Procesando el PDF...")
    blob_url = obtener_blob_url(uploaded_file.name)

    if blob_url:
        resultado = procesar_pdf(blob_url)
        if resultado:
            st.write("Información extraída del menú:")
            st.json(resultado)
            
            # Subir el JSON a Azure Blob Storage
            st.write("Subiendo JSON extraído a Azure Blob Storage...")
            nombre_json = f"{resultado['restaurante'].replace(' ', '_').lower()}.json"
            subir_json_a_blob(resultado, nombre_json)
            st.success(f"JSON subido correctamente: {nombre_json}")

            # Descargar el JSON y almacenarlo en CosmosDB
            st.write("Guardando el menú en CosmosDB...")
            menu_json = download_json_from_blob(nombre_json)
            if menu_json:
                store_menu_in_cosmos(menu_json)
                st.success("Menú guardado en CosmosDB exitosamente.")
        else:
            st.error("No se pudo procesar el archivo PDF correctamente.")
    else:
        st.error("No se pudo obtener la URL del archivo en Blob Storage.")
