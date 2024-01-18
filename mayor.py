# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:00:57 2024

@author: USUARIO
"""

def mayor(a: int, b: int, c: int, d: int) -> int:
    """
    Devuelve el mayor de cuatro números enteros.

    Parameters:
    - a (int): Primer número entero.
    - b (int): Segundo número entero.
    - c (int): Tercer número entero.
    - d (int): Cuarto número entero.

    Returns:
    - int: El número entero más grande de los cuatro.
    """
    maximo = a

    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    if d > maximo:
        maximo = d

    return maximo

resultado = mayor(5, 8, 3, 7)
print(resultado)  # Salida esperada: 8