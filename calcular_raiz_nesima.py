# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:57:15 2024

@author: USUARIO
"""

import math

def calcular_raiz_nesima():
    """
    Solicita al usuario un número y un valor para n, luego calcula la raíz n-ésima del número.
    El programa verifica que el número ingresado esté en el rango de 2 a 100 para n.

    Args:
        None

    Returns:
        None
    """
    try:
        # Solicitar un número al usuario
        numero = float(input("Ingrese un número: "))

        # Solicitar el valor de n para la raíz n-ésima
        n = int(input("Ingrese el valor de n para la raíz  (entre 2 y 100): "))

        # Verificar que n esté en el rango permitido
        if 2 <= n <= 100:
            # Calcular la raíz n-ésima del número
            raiz_nesima = math.pow(numero, 1/n)

            # Mostrar el resultado
            print(f"La raíz {n} de {numero} es: {raiz_nesima:.4f}")
        else:
            print("Error: El valor de n debe estar entre 2 y 100.")
    except ValueError:
        print("Error: Ingrese un número válido.")

# Llamar a la función principal
calcular_raiz_nesima()
