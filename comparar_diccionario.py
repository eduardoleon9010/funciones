# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:09:07 2024

@author: USUARIO
"""
def comparar_diccionario(cadena1: str, cadena2: str) -> int:
    """
    Compara dos cadenas de caracteres que contienen solo letras mayúsculas y minúsculas.
    
    Parámetros:
    - cadena1 (str): La primera cadena a comparar.
    - cadena2 (str): La segunda cadena a comparar.

    Retorna:
    - int: -1 si cadena1 debería ir antes que cadena2, 1 si cadena2 debería ir antes que cadena1, 0 si son iguales.
    """

    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()

    if cadena1 < cadena2:
        return -1
    elif cadena1 > cadena2:
        return 1
    else:
        return 0

