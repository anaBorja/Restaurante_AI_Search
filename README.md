# 🥘 Restaurante AI Search 🍽️
Este proyecto es una aplicación web que permite a varios restaurantes gestionar sus menús de manera automatizada. Los restaurantes suben un archivo PDF con el menú del día a Azure Blob Storage, y un modelo entrenado con **Document Intelligence** extrae la información clave de esos menús. Luego, los datos extraídos se guardan en un formato JSON en otro Blob Storage y, finalmente, se almacenan en **Azure CosmosDB**. Los clientes pueden buscar restaurantes y menús específicos utilizando un sistema de búsqueda a través de **Azure AI Search**.

## 📝 Descripción

El sistema tiene dos interfaces principales:

1. **Interfaz para Restaurantes**: Los restaurantes pueden subir el PDF de su menú del día. El PDF se guarda en Azure Blob Storage llamado "menús". La aplicación utiliza el modelo de **Document Intelligence** de Azure para extraer la información relevante del menú (nombre del restaurante, dirección, primer plato, segundo plato, postre, bebida, precio, etc.) y genera un archivo JSON que se almacena en otro Blob Storage. Posteriormente, los datos se guardan en **CosmosDB**.

2. **Interfaz para Clientes**: Los clientes pueden buscar restaurantes o menús específicos utilizando **Azure AI Search**, que consulta los datos almacenados en CosmosDB. Los clientes pueden buscar por platos, ingredientes o menús específicos.

### Funcionalidades
- Subida de PDFs con menús de restaurantes.
- Extracción de datos clave del menú usando **Azure Document Intelligence**.
- Almacenamiento de datos en **Azure Blob Storage** y **Azure CosmosDB**.
- Búsqueda de menús y platos utilizando **Azure AI Search**.

## 🔄 Flujo de Trabajo

1. **Subida de Menús**: Los restaurantes suben sus menús diarios en formato PDF a un Blob Storage llamado `menús`.
2. **Extracción de Datos**: El modelo entrenado de **Document Intelligence** extrae la información clave del menú (nombre del restaurante, dirección, platos, bebidas, precios, etc.) y genera un archivo JSON.
3. **Almacenamiento**: El archivo JSON generado se guarda en un Blob Storage diferente y se carga en **Azure CosmosDB** para almacenamiento.
4. **Búsqueda de Menús**: Los clientes pueden realizar consultas sobre platos o ingredientes a través de la aplicación de búsqueda. La búsqueda se realiza utilizando **Azure AI Search** en los datos almacenados en **CosmosDB**.

## Interfaces

### 1. 🍽️ **Interfaz para Restaurantes** 

Los restaurantes pueden acceder a la interfaz para subir los PDFs con los menús. Puedes acceder a esta interfaz desde el siguiente enlace:

- [🍔 Interfaz para Restaurantes](https://restaurante.streamlit.app/)

### 2. 🛒 **Interfaz para Clientes**  

Los clientes pueden buscar platos específicos a través de la interfaz del cliente. Pueden ingresar ingredientes o nombres de platos y ver qué restaurantes ofrecen esos menús. Accede a esta interfaz desde el siguiente enlace:

- [🍕 Interfaz para Clientes](https://comilon.streamlit.app/)

## 🏗️ Arquitectura

1. **Azure Blob Storage**: Almacena los PDFs con los menús de los restaurantes.
2. **Azure Document Intelligence**: Extrae los datos relevantes de los PDFs y los convierte en archivos JSON.
3. **Azure CosmosDB**: Almacena los datos estructurados extraídos de los menús.
4. **Azure AI Search**: Realiza búsquedas sobre los datos almacenados en CosmosDB, permitiendo a los clientes encontrar menús y platos específicos.

## 🛠️ Tecnologías Usadas

- **Streamlit**: Para crear las interfaces web para los restaurantes y clientes.
- **Azure Blob Storage**: Para el almacenamiento de archivos PDF y JSON.
- **Azure Document Intelligence**: Para la extracción de datos desde los PDFs.
- **Azure CosmosDB**: Para el almacenamiento de datos estructurados.
- **Azure AI Search**: Para la búsqueda de menús y platos.

## 📥 Instrucciones de Uso

### Configuración del Entorno
1. Clona este repositorio en tu máquina local.
```bash
git clone https://github.com/anaBorja/Restaurante_AI_Search.git
cd repositorio
````
2. Instala las dependencias necesarias:
 ```bash
 pip install -r requirements.txt
```
## 🚀 Ejecutar Ambas Aplicaciones de Streamlit

Para ejecutar ambas interfaces de Streamlit (la del restaurante y la del cliente), sigue estos pasos:

1. ejecutar la parte del restaurante.
   ```bash
   streamlit run web_restaurante.py
   
2. ejecutar la paete del cliente.
   ```bash
   streamlit run web_comilon.py

# ⚠️ **ADVERTENCIA**: Antes de ejecutar la aplicación, asegúrate de rellenar las siguientes variables
## con tus credenciales de Azure correspondientes. 
### Estas son necesarias para que las aplicaciones puedan acceder a los recursos de Azure.
```bash
AZURE_FORM_RECOGNIZER_ENDPOINT=<YOUR AZURE_FORM_RECOGNIZER_ENDPOINT>
AZURE_FORM_RECOGNIZER_KEY=<YOUR AZURE_FORM_RECOGNIZER_KEY>
MODEL_ID=<YOUR MODEL_ID>
AZURE_STORAGE_CONNECTION_STRING=<YOUR AZURE_STORAGE_CONNECTION_STRING>
COSMOSDB_CONNECTION_STRING=<YOUR COSMOSDB_CONNECTION_STRING>
AZURE_SEARCH_ENDPOINT=<YOUR AZURE_SEARCH_ENDPOINT>
AZURE_SEARCH_API_KEY=<YOUR AZURE_SEARCH_API_KEY>

