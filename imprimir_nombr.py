# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:01:57 2024

@author: USUARIO
"""

def imprimir_nombre(nombre: str, apellido: str) -> None:
    """
    Imprime el nombre completo concatenando el nombre y el apellido.

    Parámetros:
    - nombre (str): El nombre de la persona.
    - apellido (str): El apellido de la persona.

    Resultado:
    - None: La función imprime el nombre completo en la consola.
    """
    print(nombre + " " + apellido)

# Ejemplos de uso:
imprimir_nombre("Juan", "Perez")  # Imprime "Juan Perez"
imprimir_nombre(nombre="Juan", apellido="Perez")  # Imprime "Juan Perez"
imprimir_nombre(apellido="Perez", nombre="Juan")  # Imprime "Juan Perez"
