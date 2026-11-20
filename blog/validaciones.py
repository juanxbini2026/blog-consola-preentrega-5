"""Reglas de validación de los posts del blog."""

from blog.datos import estados_post

def validar_post(post):
    """
    Valida que un post cumpla con la estructura y datos requeridos.
    Retorna tupla (bool, mensaje).
    """

    if not isinstance(post, dict):
        return (False, "error - el post no es un diccionario")

    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    for clave in claves_obligatorias:
        if clave not in post:
            return (False, f"error - falta la clave '{clave}'")

    titulo = post.get("titulo", "").strip()
    if titulo == "":
        return (False, "error - titulo no puede estar vacío")

    contenido = post.get("contenido", "").strip()
    if contenido == "":
        return (False, "error - contenido no puede estar vacío")

    if not isinstance(post.get("tags"), list):
        return (False, "error - tags debe ser una lista")

    if not isinstance(post.get("autor"), dict):
        return (False, "error - autor debe ser un diccionario")

    nombre_autor = post["autor"].get("nombre", "")
    if not isinstance(nombre_autor, str) or nombre_autor.strip() == "":
        return (False, "error - el autor debe tener un nombre no vacío")

    estado = post.get("estado", "")
    if estado not in estados_post:
        return (False, f"error - estado '{estado}' no está permitido")

    return (True, "Post válido")

def validar_todos_posts(lista_posts):
    """
    Valida todos los posts y muestra un resumen de cada uno.
    Retorna una lista de tuplas (indice, es_valido, mensaje).
    """

    resultados = []

    print("\n" + "="*60)
    print("🔍 VALIDACIÓN DE POSTS")
    print("="*60)

    for indice, post in enumerate(lista_posts, start=1):
        es_valido, mensaje = validar_post(post)
        resultados.append((indice, es_valido, mensaje))
        if es_valido:
            print(f"Post {indice}: ✓ {mensaje}")
        else:
            print(f"Post {indice}: ✗ {mensaje}")

    print("="*60)
    return resultados
