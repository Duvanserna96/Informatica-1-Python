# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:20:04 2026

@author: Serna
"""

import random


def generar():
    digitos = range(1, 10)

    while True:
        num_gen = ''

        for i in range(4):
            numero = random.choice(digitos)
            num_gen = num_gen + str(numero)

        if len(set(num_gen)) == 4:
            num_gen = int(num_gen)
            return num_gen
    