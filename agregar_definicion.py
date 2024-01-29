# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:15:46 2024

@author: USUARIO
"""

def agregar_definicion(diccionario: dict, palabra: str, definicion: str) -> None:
    """
    Agrega o reemplaza una llave y su definición en un diccionario.

    Parámetros:
    - diccionario (dict): El diccionario al que se le agregará o modificará una llave.
    - palabra (str): La llave que se agregará o reemplazará en el diccionario.
    - definicion (str): La definición asociada a la llave que se agregará o reemplazará.

    Retorno:
    - None: La función no retorna nada, ya que modifica el diccionario directamente.
    """
    diccionario[palabra] = definicion

# Crear un diccionario vacío
palabras = {}

# Agregar definiciones usando la función
agregar_definicion(palabras, 'palabra1', 'definicion1')
print(f'Diccionario después de agregar palabra1: {palabras}')  # {'palabra1': 'definicion1'}

agregar_definicion(palabras, 'palabra2', 'definicion2')
print(f'Diccionario después de agregar palabra2: {palabras}')  # {'palabra1': 'definicion1', 'palabra2': 'definicion2'}

# Solicitar datos por consola
nueva_palabra = input('Ingrese una nueva palabra: ')
nueva_definicion = input(f'Ingrese la definición de {nueva_palabra}: ')

# Agregar la nueva palabra y definición al diccionario
agregar_definicion(palabras, nueva_palabra, nueva_definicion)

# Mostrar el diccionario actualizado
print(f'Diccionario después de agregar {nueva_palabra}: {palabras}')
