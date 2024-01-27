# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:33:31 2024

@author: USUARIO
"""

import math

def solucionar_cuadratica(a: int, b: int, c: int) -> tuple:
    """ 
    Encuentra las soluciones reales de una ecuación cuadrática de la forma y = ax^2 + bx + c
    Parámetros:
    a (int): El coeficiente del término de orden 2
    b (int): El coeficiente del término de orden 1
    c (int): El coeficiente del término de orden 0
    Retorna:
    (tuple): Una tupla con las soluciones reales de la ecuación.
    Retorna None si la ecuación no tiene solución real.
    """
    soluciones = None
    determinante = (b**2) - (4*a*c)
    if determinante >= 0:
        sol1 = (-b + math.sqrt(determinante)) / (2*a)
        sol2 = (-b - math.sqrt(determinante)) / (2*a)
        soluciones = (sol1, sol2)
    return soluciones

def imprimir_soluciones(soluciones: tuple) -> None:
    """ 
    Imprime las soluciones de una ecuación cuadrática o imprime un mensaje indicando que no había soluciones.
    Parámetros:
    soluciones (tuple): Una tupla con dos elementos que son las soluciones de la ecuación.
    Si no hay soluciones reales, 'soluciones' debe tener el valor None.
    """
    if soluciones is None:
        print("La ecuación no tenía soluciones reales")
    else:
        print("Las soluciones son", soluciones[0], "y", soluciones[1])

# Solicitar al usuario que ingrese los coeficientes
a = int(input("Ingrese el coeficiente a: "))
b = int(input("Ingrese el coeficiente b: "))
c = int(input("Ingrese el coeficiente c: "))

# Calcular e imprimir las soluciones
soluciones = solucionar_cuadratica(a, b, c)
imprimir_soluciones(soluciones)
