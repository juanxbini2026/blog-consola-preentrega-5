"""Reglas de validación de los posts del blog."""

from blog.datos import estados_post
from blog.modelos import Autor, Post


def validar_post(post):
    """
    Valida que un post tenga datos correctos.

    - Entra: un objeto Post.
    - Sale: tupla (es_valido, mensaje). es_valido es True o False y
      el mensaje explica el primer problema encontrado.
    """

    if not isinstance(post, Post):
        return (False, "error - no es un objeto Post")

    if not isinstance(post.id, int):
        return (False, "error - el post no tiene un id numérico")

    if not isinstance(post.titulo, str) or post.titulo.strip() == "":
        return (False, "error - titulo no puede estar vacío")

    if not isinstance(post.contenido, str) or post.contenido.strip() == "":
        return (False, "error - contenido no puede estar vacío")

    if not isinstance(post.tags, list):
        return (False, "error - tags debe ser una lista")

    if not isinstance(post.autor, Autor):
        return (False, "error - el autor debe ser un objeto Autor")

    nombre_autor = post.autor.nombre
    if not isinstance(nombre_autor, str) or nombre_autor.strip() == "":
        return (False, "error - el autor debe tener un nombre no vacío")

    if post.estado not in estados_post:
        return (False, f"error - estado '{post.estado}' no está permitido")

    return (True, "Post válido")


def validar_todos_posts(lista_posts):
    """
    Valida cada post de una lista.

    - Entra: una lista de objetos Post.
    - Sale: una lista de tuplas (indice, es_valido, mensaje), una por post.
      No imprime nada: mostrar el resultado es trabajo del menú.
    """

    resultados = []

    for indice, post in enumerate(lista_posts, start=1):
        es_valido, mensaje = validar_post(post)
        resultados.append((indice, es_valido, mensaje))

    return resultados
