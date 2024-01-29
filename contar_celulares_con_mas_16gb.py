# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:12:30 2024

@author: USUARIO
"""

def contar_celulares_con_mas_16gb(celular1: dict, celular2: dict, celular3: dict, celular4: dict) -> int:
    """
    Cuenta cuántos de los 4 celulares tienen más de 16 GB de memoria.

    Parámetros:
    - celular1 (dict): Diccionario que representa las especificaciones del primer celular.
    - celular2 (dict): Diccionario que representa las especificaciones del segundo celular.
    - celular3 (dict): Diccionario que representa las especificaciones del tercer celular.
    - celular4 (dict): Diccionario que representa las especificaciones del cuarto celular.

    Retorno:
    - int: La cantidad de celulares que tienen más de 16 GB de memoria.
    """
    # Función auxiliar para determinar si un celular tiene más de 16 GB de memoria
    def tiene_mas_16gb(celular):
        return celular.get('memoria', 0) > 16

    # Contador de celulares con más de 16 GB de memoria
    cantidad_celulares_mas_16gb = 0

    # Verificar cada celular
    if tiene_mas_16gb(celular1):
        cantidad_celulares_mas_16gb += 1
    if tiene_mas_16gb(celular2):
        cantidad_celulares_mas_16gb += 1
    if tiene_mas_16gb(celular3):
        cantidad_celulares_mas_16gb += 1
    if tiene_mas_16gb(celular4):
        cantidad_celulares_mas_16gb += 1

    return cantidad_celulares_mas_16gb

# Ejemplo de uso
celular1 = {'modelo': 'A1', 'memoria': 32, 'precio': 300}
celular2 = {'modelo': 'B2', 'memoria': 16, 'precio': 250}
celular3 = {'modelo': 'C3', 'memoria': 64, 'precio': 400}
celular4 = {'modelo': 'D4', 'memoria': 8, 'precio': 200}

cantidad_celulares_mas_16gb = contar_celulares_con_mas_16gb(celular1, celular2, celular3, celular4)

# Imprimir el resultado
print(f"La cantidad de celulares con más de 16 GB de memoria es: {cantidad_celulares_mas_16gb}")
