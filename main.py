"""Punto de entrada del blog por consola. Ejecutar con: python main.py"""

from blog.datos import cargar_posts, guardar_posts, RUTA_POSTS
from blog.modelos import Blog
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, mostrar_validacion, buscar_por_titulo, filtrar_por_tag


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
            pass

        elif opcion == 5:
            mostrar_validacion(blog.validar_posts())

        elif opcion == 6:
            pass

        elif opcion == 7:
            print("\n👋 ¡Hasta luego! Gracias por usar el sistema de blog.")
            print("="*60 + "\n")
            break