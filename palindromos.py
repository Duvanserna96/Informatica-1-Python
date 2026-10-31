print('\nSe verifica si la palabra es palíndroma')

palabra = input('Ingrese una palabra: ').lower()

invertida = ''

for letra in palabra:
    invertida = letra + invertida

if palabra == invertida:
    print('Es palíndroma')
else:
    print('No es palíndroma')
