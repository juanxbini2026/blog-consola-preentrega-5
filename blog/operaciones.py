"""Funciones que muestran en pantalla los resultados que calcula Blog."""


def listar_posts(lista_posts):
    """
    Muestra en pantalla una lista de posts con su ID, título, autor y estado.

    - Entra: una lista de objetos Post (por ejemplo, lo que devuelve
      blog.obtener_posts() o blog.buscar_por_titulo(...)).
    - Sale: nada; solo imprime.
    """

    if len(lista_posts) == 0:
        print("No hay posts disponibles.")
        return

    print("\n" + "="*60)
    print("📖 POSTS")
    print("="*60)

    for post in lista_posts:
        titulo = post.titulo if post.titulo else "(sin título)"

        print(f"[ID {post.id}] Título: {titulo}")
        print(f"           Autor: {post.autor}")
        print(f"           Estado: {post.estado}\n")

    print("="*60)


def mostrar_validacion(resultados):
    """
    Muestra en pantalla el resultado de validar los posts.

    - Entra: la lista de tuplas (indice, es_valido, mensaje) que devuelve
      blog.validar_posts().
    - Sale: nada; solo imprime.
    """

    print("\n" + "="*60)
    print("🔍 VALIDACIÓN DE POSTS")
    print("="*60)

    for indice, es_valido, mensaje in resultados:
        if es_valido:
            print(f"Post {indice}: ✓ {mensaje}")
        else:
            print(f"Post {indice}: ✗ {mensaje}")

    print("="*60)
