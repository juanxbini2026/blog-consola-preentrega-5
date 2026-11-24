"""Punto de entrada del blog por consola. Ejecutar con: python main.py"""

from blog.datos import cargar_posts, guardar_posts, RUTA_POSTS
from blog.modelos import Autor, Post, Blog
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.operaciones import listar_posts, mostrar_validacion, buscar_por_titulo, filtrar_por_tag


def guardar_blog(blog):
    """
    Guarda todos los posts del blog en posts.json y avisa cómo salió.

    - Entra: el objeto Blog con los posts actuales.
    - Sale: True si se guardó, False si no se pudo.
    Se usa desde la opción 6 (guardar) y la opción 7 (salir).
    """
    if guardar_posts(blog.a_lista_de_diccionarios(), RUTA_POSTS):
        print(f"✅ Posts guardados en {RUTA_POSTS}.")
        return True

    print("❌ No se pudieron guardar los posts.")
    return False


if __name__ == "__main__":

    print("\n" + "="*60)
    print("🎉 BIENVENIDO AL SISTEMA DE BLOG MODULAR")
    print("="*60)


    blog = Blog(cargar_posts(RUTA_POSTS))
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(blog.obtener_posts())

        elif opcion == 2:
            termino = pedir_texto("Ingresa el término a buscar: ")
            if termino == "":
                print("Ingresa un término para buscar.")
            else:
                resultados = blog.buscar_por_titulo(termino)
                if len(resultados) > 0:
                    listar_posts(resultados)
                else:
                    print(f"No se encontraron posts con '{termino}'.")

        elif opcion == 3:
            tag = pedir_texto("Ingresa el tag a filtrar: ")
            if tag == "":
                print("Ingresa un tag para filtrar.")
            else:
                resultados = blog.filtrar_por_tag(tag)
                if len(resultados) > 0:
                    listar_posts(resultados)
                else:
                    print(f"No se encontraron posts con el tag '{tag}'.")

        elif opcion == 4:
            datos = pedir_datos_post()
            autor = Autor(datos["nombre_autor"])
            nuevo_post = Post(blog.siguiente_id(), datos["titulo"], datos["contenido"],
                              autor, datos["tags"], datos["estado"])
            blog.agregar_post(nuevo_post)
            print(f"✅ Post creado: {nuevo_post}")
            print("   Se guarda al salir (opción 7) o cuando elijas la opción 6.")

        elif opcion == 5:
            mostrar_validacion(blog.validar_posts())

        elif opcion == 6:
            guardar_blog(blog)

        elif opcion == 7:
            guardar_blog(blog)
            print("\n👋 ¡Hasta luego! Gracias por usar el sistema de blog.")
            print("="*60 + "\n")
            break