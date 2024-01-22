# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:06:34 2024

@author: USUARIO
"""

def comparar_cadenas(cadena1: str, cadena2: str) -> int:
    """
    Compara dos cadenas de caracteres y retorna un valor según las diferencias.

    Parámetros:
    - cadena1 (str): La primera cadena a comparar.
    - cadena2 (str): La segunda cadena a comparar.

    Retorna:
    - int: 1 si las cadenas son idénticas, 2 si difieren solo en mayúsculas y minúsculas, 0 de lo contrario.
    """

    if cadena1 == cadena2:
        return 1
    elif cadena1.lower() == cadena2.lower():
        return 2
    else:
        return 0
