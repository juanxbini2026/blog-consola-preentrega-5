"""Menú del blog e interacción con el usuario (input)."""

from blog.datos import estados_post


def mostrar_menu():
    """Muestra el menú principal y retorna la opción del usuario (1-7)."""

    while True:
        print("\n" + "="*50)
        print("  📚 --- MENÚ DEL BLOG ---")
        print("="*50)
        print("  1️⃣  Ver todos los posts")
        print("  2️⃣  Buscar por título")
        print("  3️⃣  Filtrar por tag")
        print("  4️⃣  Crear nuevo post")
        print("  5️⃣  Validar posts")
        print("  6️⃣  Guardar posts en JSON")
        print("  7️⃣  Salir")
        print("="*50)

        try:
            opcion = int(input("Ingresa una opción (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Error: Ingresa un número del 1 al 7.")
        except ValueError:
            print("Error: Debes ingresar un número.")

def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios en los extremos."""
    return input(mensaje).strip()


def pedir_texto_obligatorio(mensaje):
    """
    Pide un texto y vuelve a preguntar hasta que el usuario escriba algo.

    - Entra: el mensaje que se muestra al pedir el dato.
    - Sale: el texto ingresado, sin espacios en los extremos y nunca vacío.
    """
    while True:
        texto = pedir_texto(mensaje)
        if texto != "":
            return texto
        print("Error: este campo no puede quedar vacío.")


def pedir_tags():
    """
    Pide los tags separados por coma y los devuelve como lista.

    - Sale: una lista de textos en minúscula, sin repetidos ni vacíos.
      Si el usuario no escribe nada, devuelve una lista vacía.
    """
    texto = pedir_texto("Tags separados por coma (opcional): ")
    tags = []
    for tag in texto.split(","):
        tag_limpio = tag.strip().lower()
        if tag_limpio != "" and tag_limpio not in tags:
            tags.append(tag_limpio)
    return tags


def pedir_estado():
    """
    Pide el estado del post y vuelve a preguntar hasta que sea uno válido.

    - Sale: uno de los estados de estados_post. Si el usuario no escribe
      nada, devuelve "borrador".
    """
    opciones = ", ".join(estados_post)
    while True:
        estado = pedir_texto(f"Estado ({opciones}) [borrador]: ").lower()
        if estado == "":
            return "borrador"
        if estado in estados_post:
            return estado
        print(f"Error: el estado debe ser uno de: {opciones}.")


def pedir_datos_post():
    """
    Pide por consola todos los datos de un post nuevo.

    - Sale: un diccionario con titulo, contenido, nombre_autor, tags y estado.
      Título, contenido y autor nunca quedan vacíos. No crea el Post:
      eso lo hace main.py con estos datos.
    """
    print("\n✍️  NUEVO POST")
    return {
        "titulo": pedir_texto_obligatorio("Título: "),
        "contenido": pedir_texto_obligatorio("Contenido: "),
        "nombre_autor": pedir_texto_obligatorio("Nombre del autor: "),
        "tags": pedir_tags(),
        "estado": pedir_estado()
    }