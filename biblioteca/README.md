# Biblioteca

Programa de consola desarrollado para Informática 1. Permite registrar libros y consultar información mediante un menú.

## Cómo funciona

Al iniciar, el programa crea una lista vacía llamada `libros`. Cada libro se guarda como un diccionario con identificador, título, autor, precio, género y estado de préstamo.

El menú se repite hasta elegir la opción **6. Salir**:

| Opción | Acción |
| --- | --- |
| 1. Agregar libro | Solicita los seis datos del libro y lo agrega a la lista. |
| 2. Información general | Muestra el título del libro más caro, el del más barato y el precio promedio. |
| 3. Buscar libros por autor | Muestra el título y precio de los libros del autor indicado. |
| 4. Mostrar libros prestados | Muestra el título y autor de los libros marcados como prestados. |
| 5. Mostrar los 3 más costosos | Muestra hasta tres libros, ordenados de mayor a menor precio. |
| 6. Salir | Finaliza el programa. |

La búsqueda por autor exige que el nombre coincida exactamente, incluidas mayúsculas y espacios. Para marcar un libro como prestado, escribe `Si` sin tilde; también se aceptan `si` y `SI`.

Para calcular los tres libros más costosos se ordena una copia de la lista mediante comparaciones e intercambios, conservando el orden original de los libros registrados.

**Los datos se guardan únicamente en memoria:** al cerrar el programa se pierden y la siguiente ejecución comienza con una lista vacía.

## Requisitos

- Python 3 instalado.
- Una terminal o consola.
- Los archivos `main.py` y `biblioteca.py` en la misma carpeta.

No se necesitan paquetes adicionales.

## Cómo ejecutarlo

Descarga el repositorio desde GitHub con **Code → Download ZIP** y extrae el archivo, o clónalo si utilizas Git.

Abre una terminal en la carpeta `biblioteca`. Si estás en la raíz del repositorio, entra con:

```sh
cd biblioteca
```

En Windows:

```sh
python main.py
```

Si tu instalación utiliza el lanzador de Python:

```sh
py main.py
```

En Linux o macOS:

```sh
python3 main.py
```

Ejecuta `main.py`, que contiene el menú e importa las funciones de `biblioteca.py`.

## Ejemplo de uso

1. Elige `1` para agregar un libro.
2. Completa los campos, por ejemplo:

```text
Identificador: L001
Titulo: Introduccion a Python
Autor: Ana Perez
Precio: 50000
Genero: Educativo
Prestado (Si/No): Si
```

3. Elige `2`: al existir un solo libro, será tanto el más caro como el más barato y el promedio será `50000.0`.
4. Elige `3` y escribe `Ana Perez` para consultar sus libros.
5. Elige `4` para ver el libro prestado, o `5` para consultar los más costosos.
6. Elige `6` para terminar.

## Formato de las entradas

- Para el menú, escribe un número entero del 1 al 6. Otros enteros muestran “Opcion incorrecta”.
- Para el precio, escribe un número sin separadores de miles ni símbolo de moneda. Usa punto para decimales, por ejemplo `25000.50`.
- El programa actual no maneja errores si se escribe texto en el menú o un precio no numérico; esas entradas interrumpen la ejecución.
- El identificador se almacena tal como se escribe; no se comprueba si está repetido.

## Archivos y funciones

| Archivo | Contenido |
| --- | --- |
| `main.py` | Lista de libros, menú y llamadas a las funciones. |
| `biblioteca.py` | Funciones para registrar y consultar los libros. |

Las cinco funciones de `biblioteca.py` son `add_book`, `get_information`, `get_books_author`, `get_information_loan` y `get_top_3`. Todas reciben la lista de libros como argumento.

El ejercicio utiliza listas, tuplas, diccionarios, funciones, condicionales y ciclos `for` y `while`.
