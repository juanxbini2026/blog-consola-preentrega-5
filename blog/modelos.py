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
    """Representa el blog completo: guarda los posts y centraliza las operaciones sobre ellos."""

    def __init__(self, posts):
        """
        Crea el blog con su lista de posts.

        - Entra: posts, una lista de objetos Post (puede estar vacía).
        - Sale: nada; guarda la lista en self.posts.
        """
        self.posts = posts

    def obtener_posts(self):
        """Devuelve la lista de todos los post del blog"""
        return self.posts
        

    def buscar_por_titulo(self, termino):
        """
        Busca los posts cuyo título contiene el término, sin importar mayúsculas.

        - Entra: el término de búsqueda como string.
        - Sale: una lista con los posts encontrados; vacía si no hay
          resultados o si el término está vacío.
        """
        if termino.strip() == "":
            return []   
        termino_minusculas = termino.lower()
        resultados = []

        for post in self.posts:
           post_titulo = post.titulo
           if termino_minusculas in post_titulo.lower():
                resultados.append(post)

        if len(resultados) > 0:
            return resultados     
        
        return []
        

    def filtrar_por_tag(self, tag):
        """
        Filtra los posts que tienen el tag indicado, sin importar mayúsculas.

        - Entra: el tag a buscar como string.
        - Sale: una lista con los posts que tienen ese tag; vacía si no hay
          resultados o si el tag está vacío. Los posts cuyos tags no son
          una lista se saltean.
        """
        if tag.strip() == "":
            return []

        tag_minusculas = tag.lower()
        posts_filtrados = []

        for post in self.posts:
            tags = post.tags
            if not isinstance(tags, list):
                continue  # tags mal cargados: se saltea el post

            for tag_post in tags:
                if isinstance(tag_post, str) and tag_post.lower() == tag_minusculas:
                    posts_filtrados.append(post)
                    break  # evita agregar el mismo post dos veces

        return posts_filtrados

    def agregar_post(self, post):
        """
        Suma un post nuevo al final de la lista de posts del blog.

        - Entra: un objeto Post ya armado.
        - Sale: nada; la lista self.posts crece en uno.
        """
        self.posts.append(post)

    def siguiente_id(self):
        """
        Calcula el id que le toca a un post nuevo: el mayor id actual + 1.

        - Sale: un número entero. Si el blog está vacío o ningún post tiene
          id numérico, devuelve 1. Los ids que no son int se ignoran.
        """
        mayor = 0
        for post in self.posts:
            if isinstance(post.id, int) and post.id > mayor:
                mayor = post.id
        return mayor + 1
        

    def validar_posts(self):
        """
        Valida todos los posts del blog con las reglas de validaciones.py.

        - Sale: una lista de tuplas (indice, es_valido, mensaje), una por post.
        """
        # Se importa acá adentro y no arriba del archivo para evitar un
        # import circular: validaciones.py ya importa Autor y Post de este módulo.
        from blog.validaciones import validar_todos_posts

        return validar_todos_posts(self.posts)

    def a_lista_de_diccionarios(self):
        """
        Convierte todos los posts del blog en diccionarios para guardarlos en el JSON.

        - Sale: una lista nueva con un diccionario por post (cada uno con su
          autor adentro). La lista self.posts no cambia.
        """
        lista_diccionario = []
        for post in self.posts:
            lista_diccionario.append(post.a_diccionario())

        return lista_diccionario

    