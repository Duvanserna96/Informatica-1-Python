# Informatica-1-Python

Ejercicios y proyectos de Informática 1 - Universidad de Antioquia.

## Trabajos

- **[Biblioteca](biblioteca/):** programa con menú para registrar libros, consultar precios, buscar por autor y mostrar préstamos y los tres libros más costosos. Consulta el **[README de biblioteca](biblioteca/README.md)** para conocer su funcionamiento y cómo ejecutarlo.
- **[Picas y Fijas](Picas_fijas/):** juego de consola para adivinar un número de cuatro dígitos distintos usando pistas de picas y fijas. Consulta el **[README de Picas y Fijas](Picas_fijas/README.md)** para ver las reglas y los pasos de ejecución.
- **[Es agresiva](es_agresiva/):** ejercicio que cuenta las frases introducidas que coinciden con un diccionario de frases agresivas. Consulta el **[README de Es agresiva](es_agresiva/README.md)** para preparar el diccionario y ejecutarlo.
- **[Cifrado César](cifrado_cesar.py):** ejercicio de cifrado César en Python.
- **[Palíndromos](palindromos.py):** ejercicio sobre palíndromos en Python.

## Ejecución

Los ejercicios requieren **Python 3** y no necesitan paquetes adicionales. Para Biblioteca, Picas y Fijas y Es agresiva, sigue las instrucciones del README correspondiente.

Para Cifrado César y Palíndromos, descarga y extrae el repositorio o clónalo con Git. Abre una terminal en la **carpeta principal del repositorio**, donde están `cifrado_cesar.py` y `palindromos.py`.

Ejecuta el archivo del ejercicio que quieras usar:

| Ejercicio | Windows | Linux o macOS |
| --- | --- | --- |
| Cifrado César | `python cifrado_cesar.py` | `python3 cifrado_cesar.py` |
| Palíndromos | `python palindromos.py` | `python3 palindromos.py` |

Si tu instalación de Windows utiliza el lanzador de Python, puedes usar `py cifrado_cesar.py` o `py palindromos.py`.

## Cifrado César

### Cómo funciona

El programa solicita una palabra y un número de saltos. Convierte la palabra a minúsculas y desplaza cada letra esa cantidad de posiciones en el alfabeto `abcdefghijklmnopqrstuvwxyz`, volviendo al inicio cuando llega al final.

Por ejemplo, con **3 saltos**, `a` se convierte en `d` y `z` en `c`.

Para construir el alfabeto desplazado, une dos partes del alfabeto original. Después recorre la palabra con un ciclo `for` y busca la posición de cada letra con un ciclo `while`.

### Cómo usarlo

1. Ejecuta `cifrado_cesar.py` con el comando correspondiente.
2. Escribe la palabra que deseas codificar.
3. Escribe un número entero de saltos **entre 0 y 25**. Con 0, las letras quedan iguales.
4. Lee la palabra codificada en la salida.

Ejemplo:

```text
Ingrese una palabra: hola
Ingrese el número de saltos (menor a 26): 3

Salida: krod
```

Solo se desplazan las letras de la `a` a la `z`. La `ñ`, las letras con tilde, los espacios y otros símbolos se conservan después de convertir el texto a minúsculas.

El programa no valida el rango de saltos. Si escribes texto en lugar de un entero, la ejecución se interrumpe.

## Palíndromos

### Cómo funciona

Una palabra es palíndroma si se lee igual de izquierda a derecha y de derecha a izquierda, como `reconocer`.

El programa solicita una palabra y la convierte a minúsculas. Luego construye su versión invertida: recorre cada letra con un ciclo `for` y la agrega al principio de una nueva cadena. Finalmente compara ambas cadenas e indica si son iguales.

### Cómo usarlo

1. Ejecuta `palindromos.py` con el comando correspondiente.
2. Escribe la palabra que quieras comprobar.
3. Lee el resultado: `Es palíndroma` o `No es palíndroma`.

Ejemplo:

```text
Ingrese una palabra: Ana
Es palíndroma
```

Con `Python`, el resultado es `No es palíndroma`.

La comparación ignora las mayúsculas, pero **no elimina espacios, tildes ni signos de puntuación**. Para probar frases, ten en cuenta que esos caracteres también forman parte de la comparación.
