# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:39:54 2024

@author: USUARIO
"""

def funcion(p1: str, p2: str, p3: dict, p4: dict) -> None:
    print("--> Valores recibidos:", p1, p2, p3, p4)
    print("--> Comparar las cadenas:", p1 == p2)
    print("--> Comparar los diccionarios:", p3 == p4, p3 is p4)

p1 = "cadena inicial"
p2 = {"inicial": 0}

print("Antes de llamar a la función: ", p1, p2)
funcion(p1, p1, p2, p2)
print("Después de llamar a la función: ", p1, p2)
