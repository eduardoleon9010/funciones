# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:14:27 2024

@author: USUARIO
"""

def contar_palabras(cadena: str) -> int:
    """
    Cuenta las palabras que aparecen en una cadena de caracteres.

    Parámetros:
    - cadena (str): La cadena de caracteres que se va a analizar.

    Retorna:
    - int: El número de palabras en la cadena.
    """

    palabras = cadena.split()
    return len(palabras)

# Uso de la funcion
cadena_ejemplo_1 = "Hola, esto es una prueba."
resultado_1 = contar_palabras(cadena_ejemplo_1)
print(f'Número de palabras en "{cadena_ejemplo_1}": {resultado_1}')

cadena_ejemplo_2 = "Python es un lenguaje de programación poderoso."
resultado_2 = contar_palabras(cadena_ejemplo_2)
print(f'Número de palabras en "{cadena_ejemplo_2}": {resultado_2}')
