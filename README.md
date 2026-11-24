# Blog por consola — Pre-entrega 6

Sistema de blog por consola en Python. Permite listar los posts, buscarlos por título, filtrarlos por tag, crear posts nuevos, validarlos y guardarlos.

Es la continuación del blog modular de la pre-entrega 5, con dos cambios principales:

- **Programación orientada a objetos:** el autor, los posts y el blog ahora son clases (`Autor`, `Post` y `Blog`) en lugar de diccionarios sueltos.
- **Persistencia en JSON:** los posts viven en el archivo `posts.json`. Se cargan al iniciar el programa y se guardan al salir, así que lo que se crea no se pierde al cerrar.

## Cómo ejecutarlo

Requisito: Python 3 instalado. No hace falta instalar ninguna librería: solo se usa el módulo `json`, que viene con Python.

1. Abrí una terminal en la carpeta raíz del proyecto (donde está `main.py`).
2. Ejecutá:

```bash
python main.py
```

El archivo que se ejecuta es **`main.py`**. Si se ejecuta desde otra carpeta, Python no encuentra el paquete `blog` (y tampoco `posts.json`).

## Estructura del proyecto

```
├── main.py              # Punto de entrada: crea el Blog, muestra el menú y coordina
├── posts.json           # Los posts guardados (se crea solo si no existe)
├── README.md
└── blog/                # Paquete con la lógica del blog
    ├── __init__.py      # Indica que blog/ es un paquete (vacío)
    ├── modelos.py       # Clases Autor, Post y Blog
    ├── datos.py         # Persistencia: cargar y guardar posts.json
    ├── menu.py          # Menú e ingreso de datos del usuario (input)
    ├── operaciones.py   # Mostrar en pantalla posts y resultados de validación
    └── validaciones.py  # Reglas para validar cada post
```

## Las clases (`blog/modelos.py`)

### `Autor`
Representa a quien escribe un post.

- Atributos: `nombre` (obligatorio), `email`, `especialidad` y `bio` (opcionales, quedan en `""`).
- `__str__()` devuelve el nombre, para que `print(autor)` se lea bien.
- `a_diccionario()` lo convierte en un diccionario apto para JSON.

### `Post`
Representa una publicación.

- Atributos: `id`, `titulo`, `contenido`, `autor`, `tags` (lista) y `estado`.
- **Composición:** `autor` no es un texto, es un objeto `Autor`. Un post *tiene* un autor.
- `__str__()` devuelve `[id] Título - Autor (estado)`.
- `a_diccionario()` lo convierte en diccionario, con el autor anidado adentro (usa `autor.a_diccionario()`).
- No valida sus datos al crearse: así el post 4 de prueba, que tiene errores, puede existir para que "Validar posts" lo detecte.

### `Blog`
Representa el blog completo: guarda la lista de posts y centraliza la lógica.

| Método | Qué hace |
|---|---|
| `obtener_posts()` | Devuelve la lista de todos los posts |
| `buscar_por_titulo(termino)` | Devuelve los posts cuyo título contiene el término |
| `filtrar_por_tag(tag)` | Devuelve los posts que tienen ese tag |
| `agregar_post(post)` | Suma un post nuevo a la lista |
| `siguiente_id()` | Calcula el id del próximo post (el mayor + 1) |
| `validar_posts()` | Valida todos los posts con las reglas de `validaciones.py` |
| `a_lista_de_diccionarios()` | Convierte todos los posts en diccionarios para guardarlos |

La búsqueda y el filtrado ignoran mayúsculas y minúsculas. `Blog` **nunca imprime**: devuelve resultados, y mostrarlos es trabajo de `operaciones.py`. Así un mismo resultado se puede reusar (por ejemplo, `listar_posts()` muestra tanto todos los posts como los de una búsqueda).

### Funciones para reconstruir objetos
- `reconstruir_autor(datos)` arma un `Autor` desde un diccionario.
- `reconstruir_post(datos)` arma un `Post` (y su `Autor`) desde un diccionario.

Si los datos no sirven (no es un diccionario, o falta el autor o su nombre), avisan con un mensaje y devuelven `None`.

## Persistencia en JSON (`blog/datos.py`)

JSON no sabe guardar objetos de Python, solo diccionarios, listas, textos, números y booleanos. Por eso los datos hacen un viaje de ida y vuelta:

```
Guardar:  objetos Post ──a_diccionario()──▶ diccionarios ──json──▶ posts.json
Cargar:   posts.json ──json──▶ diccionarios ──reconstruir_post()──▶ objetos Post
```

### `cargar_posts(ruta)`
Lee el archivo y devuelve una lista de objetos `Post`. Nunca hace caer al programa:

| Situación | Qué pasa |
|---|---|
| El archivo no existe | Avisa y arranca con el blog vacío |
| El archivo está vacío o mal escrito | Avisa y arranca con el blog vacío |
| El JSON no es una lista | Avisa y arranca con el blog vacío |
| Un post está roto (por ejemplo, sin autor) | Lo saltea, avisa y carga los demás |

### `guardar_posts(lista_de_dicts, ruta)`
Escribe la lista de diccionarios en el archivo y devuelve `True` o `False`. Trabaja en dos pasos:

1. Convierte la lista a texto con `json.dumps`. Si encuentra un objeto sin convertir, avisa y devuelve `False` **sin tocar el archivo**.
2. Recién después abre el archivo y escribe ese texto. Si no se puede escribir, avisa y devuelve `False`.

Se hace así porque `json.dump` escribe de a pedazos: si fallara a mitad de camino, dejaría `posts.json` cortado y se perderían los posts.

### Cuándo se guarda
- **Al salir** con la opción 7, automáticamente.
- **Cuando se elige** la opción 6, sin cerrar el programa.

Si el programa se corta de golpe (por ejemplo con Ctrl+C), lo que no se haya guardado se pierde.

## Responsabilidad de cada módulo

- **`main.py`**: crea el `Blog` con los posts de `posts.json` y, dentro de `if __name__ == "__main__":`, repite el menú. En cada opción le pide el dato a `blog` y se lo pasa a `operaciones.py` para mostrarlo. Coordina, pero no tiene la lógica.
- **`blog/modelos.py`**: las clases y las funciones de reconstrucción. Es la parte central y no pide datos al usuario ni lee archivos.
- **`blog/datos.py`**: la única parte que sabe que existe `posts.json`. También guarda `estados_post`, los estados válidos de un post.
- **`blog/menu.py`**: todo lo que se le pide al usuario. `mostrar_menu()` vuelve a preguntar si se ingresa texto o un número fuera de 1-7. `pedir_datos_post()` pide los datos de un post nuevo: no acepta título, contenido ni autor vacíos, y el estado tiene que ser uno de los válidos.
- **`blog/operaciones.py`**: muestra en pantalla. `listar_posts()` muestra una lista de posts y `mostrar_validacion()` muestra el resultado de validar.
- **`blog/validaciones.py`**: `validar_post()` revisa que el post tenga id numérico, título y contenido no vacíos, tags como lista, un autor con nombre y un estado válido. `validar_todos_posts()` devuelve el resultado de cada post, sin imprimir.

`Blog.validar_posts()` importa `validaciones.py` adentro del método (y no arriba del archivo) para evitar un import circular, porque `validaciones.py` ya importa las clases de `modelos.py`.

## Menú

```
1. Ver todos los posts
2. Buscar por título
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir
```

`posts.json` incluye un post incompleto a propósito (el 4: sin título, con los tags como texto y un estado inválido) para probar la opción 5.

## Pruebas realizadas

- Ejecutar con `posts.json` existente, sin `posts.json`, y con el archivo vacío, mal escrito o con algo que no es una lista.
- Ingresar letras, nada, o números fuera de rango (0, -1, 8, 100) en el menú.
- Buscar y filtrar mezclando mayúsculas y minúsculas, sin resultados y con el texto vacío.
- Crear un post dejando campos vacíos y con un estado inválido.
- Crear un post, guardar, cerrar y volver a abrir el programa: el post sigue estando.
- Intentar guardar objetos sin convertirlos a diccionario: avisa y `posts.json` queda intacto.
- Reconstruir objetos desde diccionarios incompletos.
- Validar posts sin nombre de autor, sin contenido, con tags que no son lista o con un estado inválido.
- Cargar un `posts.json` con tipos inesperados (por ejemplo, un título `null`): ninguna opción se cae.
