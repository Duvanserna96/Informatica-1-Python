# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:35:41 2026

@author: Serna
"""

from gen_num import generar
from leer_num import leer_num
from verificar import verificar
from bienvenida import bienvenida

def pricipal():
    
    bienvenida()

    jugar = 's'

    while jugar == 's':

        num_gen = generar()

        while True:
            n = input("¿Cuántos intentos desea tener?: ")

            if n.isdigit() and int(n) > 0:
                n = int(n)
                break
            else:
                print("Ingrese una cantidad válida")

        gano = False

        for i in range(n):
            print("Intento:", i + 1)

            num_us = leer_num()

            fijas, picas = verificar(num_us, num_gen)

            print(picas, "picas", fijas, "fijas")

            if fijas == 4:
                print("¡Felicitaciones! ha adivinado el numero")
                gano = True
                break

        if gano == False:
            print("Se acabaron sus intentos. El numero era:", num_gen)

        jugar = input("¿Desea jugar nuevamente? (s/n): ").lower()

    print("Gracias por jugar")
    
pricipal()