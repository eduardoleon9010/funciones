# Calculadora de áreas

Este repositorio contiene funciones para calcular áreas de figuras geométricas simples y obtener la diferencia entre estas áreas.

## Funciones:

import math

def calcular_area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado dado el valor de un lado.

    Args:
    lado (float): Longitud del lado del cuadrado.

    Returns:
    float: Área del cuadrado.
    """
    return lado * lado

def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado el valor del radio.

    Args:
    radio (float): Radio del círculo.

    Returns:
    float: Área del círculo.
    """
    return math.pi * radio ** 2

def calcular_diferencia(lado: float) -> float:
    """
    Calcula la diferencia entre el área de un cuadrado y un círculo, 
    donde el cuadrado tiene el lado proporcionado y el círculo tiene la mitad de ese lado como radio.

    Args:
    lado (float): Longitud del lado del cuadrado.

    Returns:
    float: Diferencia entre el área del cuadrado y el círculo.
    """
    area_cuadrado = calcular_area_cuadrado(lado)
    radio_circulo = lado / 2
    area_circulo = calcular_area_circulo(radio_circulo)
    return abs(area_cuadrado - area_circulo)
