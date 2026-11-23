""" Clase de dominio del blog: Autor, Post  y Blog """

class Autor:
    def __init__(self, nombre, email="", especialidad="", bio=""):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad
        self.bio = bio

    def __str__(self):
        return self.nombre

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "especialidad": self.especialidad,
            "bio": self.bio
        }

def reconstruir_autor(datos):
    """ Entra: Diccionario con los datos traidos del JSON 
    Sale: un objeto Autor con los datos del diccionario """
    
    return Autor(datos["nombre"], datos["email"], datos["especialidad"], datos["bio"])


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def __str__(self):
        pass

    def a_diccionario(self):
        pass


def reconstruir_post(datos):
    """..."""
    pass


class Blog:
    def __init__(self, posts):
        self.posts = posts

    def obtener_posts(self):
        """..."""
        pass

    def buscar_por_titulo(self, termino):
        """..."""
        pass

    def filtrar_por_tag(self, tag):
        """..."""
        pass

    def agregar_post(self, post):
        """..."""
        pass

    def siguiente_id(self):
        """..."""
        pass

    def validar_posts(self):
        """..."""
        pass

    def a_lista_de_diccionarios(self):
        """..."""
        pass
    