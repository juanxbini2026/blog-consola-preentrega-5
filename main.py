"""Punto de entrada del blog por consola. Ejecutar con: python main.py"""

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos_posts

if __name__ == "__main__":

    print("\n" + "="*60)
    print("🎉 BIENVENIDO AL SISTEMA DE BLOG MODULAR")
    print("="*60)

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Ingresa el término a buscar: ")
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = pedir_texto("Ingresa el tag a filtrar: ")
            filtrar_por_tag(posts, tag)

        elif opcion == 4:
            validar_todos_posts(posts)

        elif opcion == 5:
            print("\n👋 ¡Hasta luego! Gracias por usar el sistema de blog.")
            print("="*60 + "\n")
            break