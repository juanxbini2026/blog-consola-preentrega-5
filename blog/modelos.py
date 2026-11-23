""" Clase de dominio del blog: Autor, Post  y Blog """

class Autor:
    """Representa a una persona que escribe posts en el blog."""

    def __init__(self, nombre, email="", especialidad="", bio=""):
        """
        Crea un autor nuevo con sus datos.

        - Entra: el nombre (obligatorio) y, opcionalmente, email, especialidad y bio.
          Los opcionales que no se pasan quedan como texto vacío ("").
        - Sale: nada; guarda los datos como atributos del objeto (self).
        """
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad
        self.bio = bio

    def __str__(self):
        """Retorna el nombre del autor para mostrarlo con print()."""
        return self.nombre

    def a_diccionario(self):
        """
        Retorna los atributos del objeto en un diccionario apto JSON

        - Entra: Objeto, es el propio autor.
        - Sale: Diccionario con los datos del Objeto.
        """
        return {
            "nombre": self.nombre,
            "email": self.email,
            "especialidad": self.especialidad,
            "bio": self.bio
        }

def reconstruir_autor(datos):
    """
    Arma un objeto Autor a partir de un diccionario leído del JSON.

    - Entra: Diccionario con los datos traídos del JSON
    - Sale: un objeto Autor con los datos del diccionario
    - Si los datos son inválidos sale: None
    """

    if not isinstance(datos, dict):
        print("Los datos del autor no son un diccionario")
        return None
    
    nombre_autor = datos.get("nombre", "")
    if not isinstance(nombre_autor, str) or nombre_autor.strip() == "":
        print("Error, el autor debe tener un nombre no vacío")
        return None
    
    return Autor(nombre_autor, datos.get("email",""), datos.get("especialidad",""), datos.get("bio",""))


class Post:
    """Representa una publicación del blog, escrita por un Autor."""

    def __init__(self, id, titulo, contenido, autor, tags, estado):
        """
        Crea un post nuevo con sus datos.

        - Entra: id (número), titulo, contenido, autor (un objeto Autor),
          tags (lista de textos) y estado.
        - Sale: nada; guarda los datos como atributos del objeto (self).
          No valida los datos: eso lo hace validaciones.py.
        """
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def __str__(self):
        """Retorna datos del post para mostrarlo con print()."""
        return f"[{self.id}] {self.titulo} - {self.autor} ({self.estado})"
        
    def a_diccionario(self):
        """ Retorna los atributos del objeto en un diccionario apto JSON"""
        return {
            "id" : self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

def reconstruir_post(datos):
    """Arma un objeto Post con los datos del diccionario leído del JSON

    - Entra: Diccionario con los datos traídos del JSON.
    - Sale si no valida: None
    - Sale: un objeto Post y sus atributos son datos del diccionario 
    """
    if not isinstance(datos, dict):
        print("'datos' no es un diccionario")
        return None

    if "autor" not in datos:
        print("'autor' no esta incluido en datos.")
        return None

    autor_diccionario = datos.get("autor")
    if not isinstance(autor_diccionario, dict):
        print("el valor 'autor' de 'datos' no es un diccionario")
        return None

    autor_objeto = reconstruir_autor(autor_diccionario)
    if autor_objeto is None:
        print("'autor' no es un objeto de Autor")
        return None
    
    return Post(datos.get("id", None),datos.get("titulo", ""), datos.get("contenido", ""), autor_objeto , datos.get("tags", []), datos.get("estado", ""))


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
    