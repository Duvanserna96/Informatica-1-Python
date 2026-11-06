# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 09:32:00 2026

@author: Serna
"""

def es_agresiva(archivo, frase):

    archivo = open(archivo, 'r')
    encontrada = False

    linea = archivo.readline()

    while linea != '' and encontrada == False:
        if linea.strip() == frase:
            encontrada = True
        else:
            linea = archivo.readline()

    archivo.close()
    return encontrada


if __name__ == '__main__':
    archivo = input('Ingrese el nombre del archivo: ')
    total = 0

    frase = input('Ingrese una frase (X para terminar): ')

    while frase != 'X':
        if es_agresiva(archivo, frase):
            total = total + 1

        frase = input('Ingrese una frase (X para terminar): ')

    print('Total de frases agresivas:', total)
