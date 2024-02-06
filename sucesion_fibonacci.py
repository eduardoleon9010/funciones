# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:01:08 2024

@author: USUARIO
"""
def sucesion_fibonacci(cantidad_numeros):
    """
    Calcula la sucesión de Fibonacci hasta el número especificado.

    Parameters:
    - cantidad_numeros (int): Cantidad de números de la sucesión que se quieren encontrar.

    Returns:
    - str: Cadena que contiene los números de la sucesión de Fibonacci hasta la cantidad indicada,
           separados por coma y sin espacios intermedios.
           Si la cantidad de números es menor o igual a 0, retorna un mensaje de error.
    """
    # Validar que la cantidad de números sea un entero positivo
    if not isinstance(cantidad_numeros, int) or cantidad_numeros <= 0:
        return "Por favor, ingrese un número entero positivo mayor que 0."

    # Inicializar los primeros dos términos de la sucesión
    fib_sequence = [0]

    # Calcular la sucesión de Fibonacci hasta la cantidad indicada
    while len(fib_sequence) < cantidad_numeros:
        if len(fib_sequence) == 1:
            fib_sequence.append(1)
        else:
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)

    # Convertir la lista de números en una cadena separada por comas
    result_string = ','.join(map(str, fib_sequence))

    return result_string

# Ejemplo de uso
try:
    cantidad_numeros = int(input("Ingrese la cantidad de números de la sucesión de Fibonacci que desea encontrar: "))
    resultado = sucesion_fibonacci(cantidad_numeros)
    print(resultado)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
