"""Datos base del blog: autor, estados, etiquetas y posts."""

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