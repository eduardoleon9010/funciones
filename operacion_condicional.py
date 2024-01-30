# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:22:19 2024

@author: USUARIO
"""

import sys

def operacion_condicional(num1: int, num2: int) -> int:
    """
    Realiza una operación condicional en base al primer número:
    - Si el primer número es par, retorna la suma de los dos números.
    - Si el primer número es impar, retorna la multiplicación de los dos números.

    Parámetros:
    - num1 (int): El primer número entero.
    - num2 (int): El segundo número entero.

    Resultado:
    - int: El resultado de la operación condicional.
    """
    if num1 % 2 == 0:  # Verifica si el primer número es par
        return num1 + num2  # Retorna la suma de los dos números si es par
    else:
        return num1 * num2  # Retorna la multiplicación de los dos números si es impar

if __name__ == "__main__":
    # Solicitar los números al usuario desde la línea de comandos
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
    except ValueError:
        print("Error: Debes ingresar números enteros.")
        sys.exit(1)

    # Llamar a la función con los números proporcionados por el usuario
    resultado = operacion_condicional(num1, num2)

    # Imprimir el resultado
    print(f"Resultado de la operación condicional: {resultado}")
