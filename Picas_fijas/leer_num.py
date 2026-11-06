# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:35:56 2026

@author: Serna
"""

def leer_num():
    while True:
        num_us = input("Ingrese un número de 4 dígitos no repetidos: ")
        
        if len(num_us) == 4 and num_us.isdigit() and len(set(num_us)) == 4:
            return num_us
        else:
            print("el número no es válido")
            
