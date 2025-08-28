import streamlit as st
import re

def find_words_with_substring(text, substring):
    """
    Encuentra todas las palabras únicas en un texto que contienen una subcadena.
    El proceso es insensible a mayúsculas y minúsculas y maneja varios idiomas.
    """
    if not text or not substring:
    # Retorna una lista vacía si no hay texto o subcadena
        return []

    # Se convierte el texto y la subcadena a minúsculas para una búsqueda insensible
    substring_lower = substring.lower()

    # Se utiliza una expresión regular para reemplazar los caracteres de puntuación por espacios
    # y luego se divide el texto en palabras.
    words = re.split(r'[\s,.!?;:()\'"“”‘’«»]+', text)

    found_words = set()
    for word in words:
        # Limpia la palabra de caracteres no deseados en los bordes
        cleaned_word = word.strip().strip("'").strip('"')
        if cleaned_word and substring_lower in cleaned_word.lower():
            found_words.add(cleaned_word)

    # Ordena las palabras encontradas alfabéticamente
    return sorted(list(found_words))

def main():
    """
    Función principal de la aplicación Streamlit.
    Configura la interfaz y maneja la lógica de la aplicación.
    """
    st.title("Buscador de palabras en archivo")
    st.markdown("---")

    st.write("Esta aplicación encuentra todas las palabras únicas que contienen una serie de letras que especifiques, **procesando el texto de un archivo subido**.")

    # Widget para la carga del archivo
    uploaded_file = st.file_uploader(
        "1. Sube un archivo de texto (por ejemplo, un archivo .txt):",
        type=['txt']
    )

    # Widget para la entrada de la subcadena a buscar
    search_term = st.text_input(
        "2. Ingresa la serie de letras (subcadena) a buscar:",
        placeholder="Ejemplo: casa"
    )

    st.markdown("---")

    # Botón para iniciar la búsqueda
    if st.button("3. Buscar palabras"):
        # Se verifica si se ha subido un archivo
        if uploaded_file is None:
            st.warning("Por favor, sube un archivo de texto para analizar.")
        elif not search_term:
            st.warning("Por favor, ingresa una serie de letras a buscar.")
        else:
            # Lee el contenido del archivo subido
            try:
                # Decodifica el archivo como una cadena de texto
                file_content = uploaded_file.read().decode("utf-8")
                
                # Llama a la función para encontrar las palabras
                result_words = find_words_with_substring(file_content, search_term)

                # Muestra los resultados
                if result_words:
                    st.subheader("Resultados:")
                    st.write(f"Se encontraron **{len(result_words)}** palabra(s) única(s) que contienen '{search_term}':")
                    st.write(", ".join(result_words))
                else:
                    st.warning(f"No se encontraron palabras que contengan '{search_term}' en el texto del archivo.")
            except Exception as e:
                st.error(f"Ocurrió un error al procesar el archivo: {e}")

# Se ejecuta la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
