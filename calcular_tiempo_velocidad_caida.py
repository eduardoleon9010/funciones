# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:34:04 2024

@author: USUARIO
"""

import math

def calcular_tiempo_velocidad_caida():
    """
    Calcula el tiempo de caída y la velocidad de un objeto que cae desde un edificio.

    Retorna:
    Una cadena de caracteres que describe el tiempo de caída y la velocidad del objeto.

    Ejemplo de uso:
    resultado = calcular_tiempo_velocidad_caida()
    print(resultado)
    """
    # Solicita al usuario ingresar la altura del edificio
    try:
        edificio_altura = float(input("Ingrese la altura del edificio en metros: "))
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        return

    # Aceleración de la gravedad en metros por segundo al cuadrado
    gravedad = 9.8

    # Calcula el tiempo de caída utilizando la fórmula t = sqrt(2h/g)
    tiempo_caida = math.sqrt(2 * edificio_altura / gravedad)

    # Calcula la velocidad alcanzada utilizando la fórmula v = gt
    velocidad_alcanzada = gravedad * tiempo_caida

    # Formatea la cadena de resultado
    resultado = (
        f"Un objeto que cae de un edificio de {edificio_altura} metros tarda "
        f"{tiempo_caida:.2f} segundos en llegar al piso y alcanza una velocidad de "
        f"{velocidad_alcanzada:.2f} metros por segundo."
    )

    return resultado

# Ejemplo de uso:
resultado = calcular_tiempo_velocidad_caida()
if resultado:
    print(resultado)
