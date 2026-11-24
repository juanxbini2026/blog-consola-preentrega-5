"""Menú del blog e interacción con el usuario (input)."""

def mostrar_menu():
    """Muestra el menú principal y retorna la opción del usuario (1-5)."""

    while True:
        print("\n" + "="*50)
        print("  📚 --- MENÚ DEL BLOG ---")
        print("="*50)
        print("  1️⃣  Ver todos los posts")
        print("  2️⃣  Buscar por título")
        print("  3️⃣  Filtrar por tag")
        print("  4️⃣  Crear nuevo post")
        print("  5️⃣  Validar posts")
        print("  6️⃣  Guardar posts en JSON")
        print("  7️⃣  Salir")
        print("="*50)

        try:
            opcion = int(input("Ingresa una opción (1-7): "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Error: Ingresa un número del 1 al 7.")
        except ValueError:
            print("Error: Debes ingresar un número.")

def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios en los extremos."""
    return input(mensaje).strip()