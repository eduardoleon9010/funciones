# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:23:19 2024

@author: USUARIO
"""
def mostrar_contactos(contactos):
    """
    Muestra en pantalla los nombres de los contactos y sus respectivos números telefónicos.

    Args:
    - contactos (dict): Un diccionario que contiene los nombres de los contactos como llaves
                        y sus respectivos números telefónicos como valores.

    Returns:
    - None: La función imprime en pantalla los nombres de los contactos y sus números telefónicos.
    """
    for nombre, numero in contactos.items():
        print(f"Nombre: {nombre}, Número telefónico: {numero}")

# Ejemplo de diccionario de contactos
contactos = {
    "Juan": "123456789",
    "María": "987654321",
    "Carlos": "456789123"
}

# Llamada a la función para mostrar los contactos
mostrar_contactos(contactos)

