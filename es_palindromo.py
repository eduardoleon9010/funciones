# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:42:57 2024

@author: USUARIO
"""


def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo.

    Parameters:
    - cadena (str): La cadena que se desea verificar.

    Returns:
    - bool: True si la cadena es un palíndromo, False de lo contrario.
    """
    # Convertir la cadena a minúsculas y mantener los espacios en blanco
    cadena = cadena.lower()
    
    # Eliminar los espacios en blanco antes de comparar
    cadena_sin_espacios = ''.join(c for c in cadena if c.isalnum())
    
    # Comparar la cadena original con su versión invertida
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

# Solicitar la cadena al usuario
cadena_usuario = input("Ingrese una cadena para verificar si es un palíndromo: ")

# Verificar si la cadena es un palíndromo
resultado = es_palindromo(cadena_usuario)

# Mostrar el resultado
print(f"¿'{cadena_usuario}' es un palíndromo? {resultado}")
