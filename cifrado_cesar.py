print('\nCodificación de palabra')

palabra = input('\nIngrese una palabra: ').lower()
salto = int(input('\nIngrese el número de saltos (menor a 26): '))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_nuevo = alfabeto[salto:] + alfabeto[:salto]
resultado = ''

for letra in palabra:
    posicion = 0

    while posicion < 26 and alfabeto[posicion] != letra:
        posicion = posicion + 1

    if posicion < 26:
        resultado = resultado + alfabeto_nuevo[posicion]
    else:
        resultado = resultado + letra

print('\nSalida:', resultado)
