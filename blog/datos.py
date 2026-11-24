"""Persistencia del blog: carga y guarda los posts en posts.json, y los estados válidos."""

import json
from blog.modelos import reconstruir_post

RUTA_POSTS = "posts.json"

estados_post = ("borrador", "publicado", "archivado")

def cargar_posts(ruta):
    """Lee el archivo JSON y devuelve la lista de posts guardados."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontró '{ruta}'. Se arranca con el blog vacío.")
        return []
    except json.JSONDecodeError:
        print(f"'{ruta}' está vacío o mal escrito. Se arranca con el blog vacío.")
        return []

    if not isinstance(datos, list):
        print(f"'{ruta}' no contiene una lista de posts. Se arranca con el blog vacío.")
        return []

    posts_cargados = []
    for diccionario in datos:
        post = reconstruir_post(diccionario)
        if post is not None:
            posts_cargados.append(post)

    return posts_cargados

def guardar_posts(lista_de_dicts, ruta):
    """
    Guarda la lista de posts en el archivo JSON.

    - Entra: la lista de posts ya convertidos a diccionario y la ruta del archivo.
    - Sale: True si se guardó, False si algo falló (avisa con un mensaje).
    Primero arma el texto y después escribe, así si falla no deja el archivo a medias.
    """
    try:
        texto = json.dumps(lista_de_dicts, ensure_ascii=False, indent=4)
    except TypeError:
        print("Error: hay datos que no se pueden convertir a JSON (¿un objeto sin pasar a diccionario?).")
        return False
    
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError:
        # OSError surgió de investigar qué tipos de errores puede dar un archivo:
        # agrupa los problemas al escribir (falta de permisos, una carpeta que
        # no existe, disco lleno), así no se cae el programa por ninguno.
        print(f"Error: no se pudo escribir '{ruta}'.")
        return False

    return True
        