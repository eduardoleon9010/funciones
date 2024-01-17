# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:17:38 2024

@author: USUARIO
"""

import random

def lanzar_moneda():
    """
    Simula el lanzamiento de una moneda.

    Returns:
    - str: Resultado del lanzamiento ('cara' o 'sello').
    """
    opciones = ['cara', 'sello']
    return random.choice(opciones)

def determinar_ganador(pedido_cara, pedido_sello, resultado_lanzamiento):
    """
    Determina quién ganó en el lanzamiento de la moneda.

    Parameters:
    - pedido_cara (str): Nombre de la persona que pidió 'cara'.
    - pedido_sello (str): Nombre de la persona que pidió 'sello'.
    - resultado_lanzamiento (str): Resultado del lanzamiento ('cara' o 'sello').

    Returns:
    - str: Nombre de la persona que acertó, o mensaje indicando que no hubo aciertos.
    """
    if resultado_lanzamiento.lower() == 'cara':
        return pedido_cara
    elif resultado_lanzamiento.lower() == 'sello':
        return pedido_sello
    else:
        return "Ninguno, el resultado no es válido."

# Registro de usuarios
nombre_persona_cara = input("Ingrese el nombre de la persona que pidió 'cara': ")
nombre_persona_sello = input("Ingrese el nombre de la persona que pidió 'sello': ")

# Lanzamiento de la moneda
resultado_aleatorio = lanzar_moneda()
print(f"El resultado del lanzamiento es: {resultado_aleatorio}")

# Determinar el ganador
ganador = determinar_ganador(nombre_persona_cara, nombre_persona_sello, resultado_aleatorio)

# Imprimir el resultado
print(f"El ganador es: {ganador}")
