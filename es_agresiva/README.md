# Es agresiva

Ejercicio de consola desarrollado en Python para Informática 1. Cuenta cuántas frases introducidas por el usuario coinciden con un archivo de frases consideradas agresivas.

## Cómo funciona

La clasificación depende de un diccionario de texto: cada línea contiene una frase.

La función `es_agresiva(archivo, frase)`:

1. Abre el archivo indicado en modo lectura.
2. Recorre sus líneas con `readline()` y un ciclo `while`.
3. Aplica `strip()` a cada línea para quitar los espacios y saltos de línea de sus extremos.
4. Compara la línea completa con la frase del usuario.
5. Devuelve `True` si encuentra una coincidencia o `False` si llega al final sin encontrarla, y cierra el archivo.

El programa principal solicita el nombre del archivo y luego recibe frases una por una. Cada coincidencia aumenta el contador en uno. Al escribir **`X` mayúscula**, termina y muestra el total.

El archivo se abre y consulta de nuevo para cada frase. Si introduces varias veces una frase que está en el diccionario, cada repetición suma uno. Las líneas duplicadas en el diccionario no multiplican el conteo de una misma consulta.

## Requisitos

- Python 3 instalado.
- Una terminal o consola.
- Un archivo de texto con una frase por línea.

No necesitas instalar paquetes adicionales.

## Preparar el diccionario

El archivo `diccionario.txt` incluido está **vacío**. Antes de probar coincidencias, ábrelo en un editor de texto, agrega las frases y guarda los cambios.

Por ejemplo:

```text
eres insoportable
no te soporto
```

Usa una frase completa por línea y evita líneas vacías. También puedes usar otro archivo de texto e indicar su nombre o ruta al iniciar el programa.

Con el diccionario vacío, el total siempre será cero.

## Cómo ejecutarlo

Descarga y extrae el repositorio desde **Code → Download ZIP**, o clónalo si utilizas Git.

Abre una terminal en la carpeta `es_agresiva`. Si estás en la raíz del repositorio, entra con:

```sh
cd es_agresiva
```

En Windows:

```sh
python es_agresiva_final.py
```

Si tu instalación utiliza el lanzador de Python:

```sh
py es_agresiva_final.py
```

En Linux o macOS:

```sh
python3 es_agresiva_final.py
```

Cuando se solicite el archivo, escribe `diccionario.txt`. Al ejecutar desde esta carpeta, el programa podrá encontrarlo por su nombre. Si utilizas otra ubicación, indica una ruta válida; el archivo debe existir.

## Ejemplo de uso

Después de guardar las dos frases del ejemplo en `diccionario.txt`:

```text
Ingrese el nombre del archivo: diccionario.txt
Ingrese una frase (X para terminar): hola
Ingrese una frase (X para terminar): no te soporto
Ingrese una frase (X para terminar): X
Total de frases agresivas: 1
```

Solo `no te soporto` coincide con una línea del diccionario. El resultado se muestra como un total al terminar.

## Detalles de la comparación

- La coincidencia es de **frase completa**: una frase que solo contiene parte de una línea no coincide.
- Se distinguen mayúsculas, minúsculas, tildes y signos de puntuación.
- Los espacios de la entrada del usuario se conservan. Por ejemplo, `no te soporto ` con un espacio al final no coincide con la línea `no te soporto`.
- Solo la entrada exacta `X` finaliza el programa; `x` o `X ` se procesan como frases.
- La frase de salida `X` no se cuenta.

## Archivos del proyecto

| Archivo | Función |
| --- | --- |
| `es_agresiva_final.py` | Contiene la función de búsqueda y el programa que solicita frases y muestra el total. |
| `diccionario.txt` | Almacena las frases de referencia, una por línea; inicialmente está vacío. |
