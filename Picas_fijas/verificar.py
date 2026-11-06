# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:33:45 2026

@author: Serna
"""

def verificar(num_u, num_m):
    num_u = str(num_u)
    num_m = str(num_m)

    fijas = 0
    picas = 0

    for i in range(4):
        if num_u[i] == num_m[i]:
            fijas = fijas + 1

        elif num_u[i] in num_m:
            picas = picas + 1

    return fijas, picas