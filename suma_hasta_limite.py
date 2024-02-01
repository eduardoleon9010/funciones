# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:29:23 2024

@author: USUARIO
"""
def suma_hasta_limite(limite):
    """
    Calcula la suma de los números desde 1 hasta el límite especificado, 1+2+3 ... n.

    Parameters:
    - limite (int): Límite superior hasta el cual se realizará la suma.

    Returns:
    int: Suma de los números desde 1 hasta el límite.
    """
    suma_total = 0
    numero_actual = 1

    while numero_actual <= limite:
        suma_total += numero_actual
        numero_actual += 1

    return suma_total

# Solicitar al usuario que ingrese el límite hasta que se ingrese un valor válido
while True:
    try:
        limite_ingresado = int(input("Ingrese el límite para la suma: "))
        break  # Salir del bucle si la conversión es exitosa
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Calcular la suma utilizando la función y el límite proporcionado
resultado_suma = suma_hasta_limite(limite_ingresado)

# Imprimir el resultado
print(f"La suma de los números hasta {limite_ingresado} es: {resultado_suma}")
