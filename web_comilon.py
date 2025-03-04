import streamlit as st
from search_menu import search_menu, format_results

# Título de la aplicación
st.title("Búsqueda de Menús en Restaurantes")

# Campo de búsqueda
query = st.text_input("Busca por plato, ingrediente o restaurante:", "*")

# Botón para realizar la búsqueda
if st.button("Buscar"):
    # Realizar la búsqueda
    results = search_menu(query)

    # Formatear los resultados
    if results:
        formatted_results = format_results(results)

        # Mostrar los resultados en la aplicación
        st.subheader("Resultados encontrados:")
        for result in formatted_results:
            st.text(result)
    else:
        st.write("No se encontraron resultados.")
