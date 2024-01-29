# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:27:55 2024

@author: USUARIO
"""

def modificar(entero: int, cadena: str) -> bool:
    """
    Modifica los parámetros enteros e imprime los valores modificados.

    Parámetros:
    - entero (int): Un número entero que se modifica dentro de la función.
    - cadena (str): Una cadena de texto que se modifica dentro de la función.

    Retorno:
    - bool: Siempre retorna True.
    """
    entero += 100
    cadena += '!!!!'
    print(entero, cadena)
    return True

# Solicitar datos por consola
numero = int(input('Ingrese un número entero: '))
texto = input('Ingrese una cadena de texto: ')

# Invocar la función con los datos ingresados por consola
resultado = modificar(numero, texto)

# Imprimir los datos después de invocar la función
print(numero, texto)
