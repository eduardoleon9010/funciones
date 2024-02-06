# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:30:46 2024

@author: USUARIO
"""

def mismos_digitos(a, b):
    """
    Determina si en dos números enteros aparecen los mismos dígitos, sin tener en cuenta la frecuencia ni el orden.

    Parameters:
    - a (int): El primer número. Debe ser un entero positivo.
    - b (int): El segundo número. Debe ser un entero positivo.

    Returns:
    - bool: True si los dígitos que aparecen en ambos números son los mismos, False de lo contrario.
    """
    # Convertir los números a listas de dígitos únicos
    digitos_a = set(str(a))
    digitos_b = set(str(b))

    # Verificar si los conjuntos de dígitos son iguales
    return digitos_a == digitos_b

# Ejemplo de uso
numero1 = 998
numero2 = 89
resultado = mismos_digitos(numero1, numero2)
print(resultado)  # Debería imprimir True en este ejemplo
