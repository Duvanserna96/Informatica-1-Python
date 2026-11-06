# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:33:47 2026

@author: Serna
"""

def bienvenida():
   b = open('bienvenida.MD', 'r')
   
   linea_t= b.readlines()
   
   for linea in linea_t[1:50]:
       print(linea.strip())
       
   b.close()