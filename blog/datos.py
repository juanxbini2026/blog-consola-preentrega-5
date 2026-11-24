"""Datos base del blog: autor, estados, etiquetas y posts."""

import json
from blog.modelos import reconstruir_post
RUTA_POSTS = "posts.json"

perfil_autor = {
    "nombre": "Juan Pérez",
    "email": "juan@blog.com",
    "especialidad": "Python"
}

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"python", "desarrollo", "tutorial", "web", "bases_datos"}

posts = [
    {
        "id": 1,
        "titulo": "Introducción a Python",
        "contenido": "Python es un lenguaje versátil y fácil de aprender...",
        "autor": perfil_autor,
        "tags": ["python", "tutorial"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Funciones en Python",
        "contenido": "Las funciones nos permiten reutilizar código...",
        "autor": perfil_autor,
        "tags": ["python", "desarrollo"],
        "estado": "publicado"
    },
    {
        "id": 3,
        "titulo": "Bases de datos con Python",
        "contenido": "Aprenderemos a conectar Python con SQL...",
        "autor": perfil_autor,
        "tags": ["python", "bases_datos"],
        "estado": "publicado"
    },
    {
        "id": 4,
        "titulo": "",  # Post incompleto para probar validaciones
        "autor": perfil_autor,
        "tags": "python",  # ERROR: debe ser lista, no string
        "estado": "en_revisión"  # ERROR: estado no válido
    }
]
def cargar_posts(ruta):
    """Lee el archivo JSON y devuelve la lista de posts guardados."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
            print(f"No se encontró '{ruta}'. Se arranca con el blog vacío")
            return []
    posts_cargados = []
    for diccionario in datos:
        post = reconstruir_post(diccionario)
        if post is not None:
            posts_cargados.append(post)

    return posts_cargados

def guardar_posts(lista_de_dicts, ruta):
    try:
        texto = json.dumps(lista_de_dicts, ensure_ascii=False, indent=4)
    except TypeError:
        print("Error: hay datos que no se pueden convertir a JSON (¿un objeto sin pasar a diccionario?).")
        return False
    
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError:
        print(f"Error: no se pudo escribir '{ruta}'.")
        return False

    return True
        