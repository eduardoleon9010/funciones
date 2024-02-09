# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:08:33 2024

@author: USUARIO
"""

def sumar_vectores(vector1: tuple, vector2: tuple) -> tuple:
    """
    Calcula la suma de dos vectores representados como tuplas.

    Args:
    vector1 (tuple): Una tupla con dos valores flotantes representando el primer vector.
    vector2 (tuple): Una tupla con dos valores flotantes representando el segundo vector.

    Returns:
    tuple: Una tupla con dos valores flotantes representando el vector resultante de la suma.
    """
    # Extraer las componentes x e y de cada vector
    x1, y1 = vector1
    x2, y2 = vector2
    
    # Calcular la suma de las componentes x e y
    suma_x = x1 + x2
    suma_y = y1 + y2
    
    # Retornar el vector resultante como una tupla
    return (suma_x, suma_y)

# Ejemplo de uso
# Definir dos vectores como tuplas de dos valores flotantes
vector_a = (2.5, 3.0)
vector_b = (1.0, -1.5)

# Calcular la suma de los dos vectores
resultado = sumar_vectores(vector_a, vector_b)

# Imprimir el resultado
print("El resultado de sumar los vectores", vector_a, "y", vector_b, "es:", resultado)
