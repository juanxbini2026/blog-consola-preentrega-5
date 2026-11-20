"""Operaciones del blog: listar, buscar por título y filtrar por tag."""


def listar_posts(lista_posts):
    """Muestra todos los posts en formato legible con ID, título, autor y estado."""

    if len(lista_posts) == 0:
        print("No hay posts disponibles.")
        return

    print("\n" + "="*60)
    print("📖 TODOS LOS POSTS")
    print("="*60)

    for post in lista_posts:
        post_id = post.get("id", "Sin ID")
        titulo = post.get("titulo", "Sin título")
        autor_nombre = post.get("autor", {}).get("nombre", "Sin autor")
        estado = post.get("estado", "Sin estado")

        print(f"[ID {post_id}] Título: {titulo}")
        print(f"           Autor: {autor_nombre}")
        print(f"           Estado: {estado}\n")

    print("="*60)


def buscar_por_titulo(lista_posts, termino_busqueda):
    """
    Busca posts cuyo título contenga el término (case-insensitive).
    Muestra los resultados y retorna la lista de posts encontrados.
    """

    if termino_busqueda.strip() == "":
        print("Ingresa un termino para buscarlo por titulo")
        return []

    termino_minusculas = termino_busqueda.lower()
    resultados = []

    for post in lista_posts:
        post_titulo = post.get("titulo", "")
        if termino_minusculas in post_titulo.lower():
            resultados.append(post)

    if len(resultados) > 0:
        listar_posts(resultados)
    else:
        print(f"No se encontraron resultados con {termino_busqueda}")

    return resultados


def filtrar_por_tag(lista_posts, tag_filtro):
    """
    Filtra posts que contengan un tag específico (case-insensitive).
    Muestra los resultados y retorna la lista de posts filtrados.
    """

    if tag_filtro.strip() == "":
        print("Ingresa un tag para filtrar")
        return []

    tag_minusculas = tag_filtro.lower()
    posts_filtrados = []

    for post in lista_posts:
        tags = post.get("tags", [])
        if not isinstance(tags, list):
            continue  # tags mal cargados: se saltea el post
        for tag in tags:
            if isinstance(tag, str) and tag_minusculas == tag.lower():
                posts_filtrados.append(post)
                break  # Evitar agregar el mismo post dos veces

    if len(posts_filtrados) > 0:
        listar_posts(posts_filtrados)
    else:
        print(f"No se encontraron posts con el tag '{tag_filtro}'.")

    return posts_filtrados
