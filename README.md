# Blog por consola — Pre-entrega 5

Sistema de blog por consola en Python, organizado en módulos y paquetes. Permite listar los posts, buscarlos por título, filtrarlos por tag y validar que estén bien cargados.

Es la continuación del blog de los módulos anteriores: se mantiene la misma estructura de datos (con el autor como diccionario anidado dentro de cada post), pero el código ahora está separado en archivos según su responsabilidad.

## Cómo ejecutarlo

Requisito: Python 3 instalado.

1. Abrí una terminal en la carpeta raíz del proyecto (donde está `main.py`).
2. Ejecutá:

```bash
python main.py
```

El archivo que se ejecuta es **`main.py`**. Si se ejecuta desde otra carpeta, Python no encuentra el paquete `blog` y aparece un error de importación.

## Estructura del proyecto

```
├── main.py              # Punto de entrada: muestra el menú y coordina el programa
├── README.md
└── blog/                # Paquete con la lógica del blog
    ├── __init__.py      # Indica que blog/ es un paquete (vacío)
    ├── datos.py         # Datos base: perfil_autor, estados_post, etiquetas_blog y posts
    ├── menu.py          # Menú e ingreso de datos del usuario (input)
    ├── operaciones.py   # Listar posts, buscar por título y filtrar por tag
    └── validaciones.py  # Reglas para validar la estructura de cada post
```

## Responsabilidad de cada módulo

- **`main.py`**: importa lo necesario desde el paquete `blog` y, dentro de `if __name__ == "__main__":`, repite el menú y llama a la función de cada opción. No contiene lógica propia.
- **`blog/datos.py`**: contiene solo los datos. Incluye un post incompleto a propósito (el 4) para probar las validaciones.
- **`blog/menu.py`**: `mostrar_menu()` muestra las opciones y retorna la elegida. Vuelve a pedir la opción si se ingresa texto o un número fuera de 1-5. `pedir_texto()` pide el término de búsqueda o el tag.
- **`blog/operaciones.py`**: `listar_posts()`, `buscar_por_titulo()` y `filtrar_por_tag()`. Reciben la lista de posts por parámetro, ignoran mayúsculas y minúsculas con `.lower()` y retornan la lista de resultados.
- **`blog/validaciones.py`**: `validar_post()` revisa que el post sea un diccionario y tenga todas las claves. También verifica que el título y el contenido no estén vacíos, que el autor sea un diccionario con nombre, que los tags sean una lista y que el estado sea válido. `validar_todos_posts()` muestra el resultado de cada post.

Los imports van en un solo sentido (`main.py` → `blog`, y `validaciones.py` → `datos.py`), así que no hay imports circulares.

## Menú

```
1. Ver todos los posts
2. Buscar por título
3. Filtrar por tag
4. Validar posts
5. Salir
```
