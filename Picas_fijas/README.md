# Picas y Fijas

Juego de consola desarrollado en Python para Informática 1.

## Objetivo y reglas

Adivina el número secreto antes de agotar tus intentos. El programa genera un número de **cuatro dígitos distintos, del 1 al 9**.

Después de cada intento recibes dos pistas:

- **Fija:** un dígito correcto en la posición correcta.
- **Pica:** un dígito que pertenece al número secreto, pero está en otra posición.

Por ejemplo, si el secreto fuera **1234** y escribieras **1325**, obtendrías **2 picas y 1 fija**: el 1 está bien ubicado; el 3 y el 2 están en otras posiciones; el 5 no pertenece al secreto.

## Cómo jugar

1. Elige cuántos intentos quieres tener: escribe un entero mayor que cero.
2. Ingresa cuatro dígitos distintos, sin espacios ni signos. Por ejemplo: `1234`.
3. Usa las picas y fijas para ajustar tu siguiente intento.
4. Ganas cuando consigues **4 fijas**. Si agotas los intentos, el programa revela el número secreto.
5. Al terminar, escribe `s` para jugar otra partida o `n` para salir.

Las entradas que no tengan cuatro dígitos distintos se vuelven a solicitar sin consumir otro intento. Aunque la entrada permite el 0, el número secreto nunca lo incluye.

## Requisitos

- Python 3 instalado.
- Una terminal o consola.
- Todos los archivos de esta carpeta juntos.

No necesitas instalar paquetes adicionales: el programa utiliza la biblioteca estándar de Python.

## Cómo ejecutarlo

Descarga el repositorio desde GitHub con **Code → Download ZIP** y extrae el archivo. También puedes clonarlo si utilizas Git.

Abre una terminal dentro de la carpeta `Picas_fijas`. Si estás en la raíz del repositorio, entra con:

```sh
cd Picas_fijas
```

En Windows, ejecuta:

```sh
python principal.py
```

Si tu instalación utiliza el lanzador de Python, puedes usar:

```sh
py principal.py
```

En Linux o macOS:

```sh
python3 principal.py
```

Ejecuta el comando desde esta carpeta porque la bienvenida se lee usando una ruta relativa.

### Si no se encuentra el archivo de bienvenida

El código actual busca `bienvenida.MD`, mientras que el archivo guardado se llama `bienvenida.md`. En sistemas que distinguen mayúsculas y minúsculas, como Linux, cambia esa referencia en `bienvenida.py` a `bienvenida.md` antes de ejecutar.

El dibujo de bienvenida utiliza caracteres Unicode. Si no se muestran correctamente, utiliza una terminal compatible con UTF-8.

## Archivos del proyecto

| Archivo | Función |
| --- | --- |
| `principal.py` | Inicia el juego, controla los intentos y permite volver a jugar. |
| `gen_num.py` | Genera el número secreto sin dígitos repetidos. |
| `leer_num.py` | Solicita y valida el intento del jugador. |
| `verificar.py` | Calcula las picas y fijas. |
| `bienvenida.py` | Lee y muestra el dibujo de bienvenida. |
| `bienvenida.md` | Contiene el dibujo de bienvenida. |
