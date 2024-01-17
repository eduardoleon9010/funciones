# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:11:13 2024

@author: USUARIO
"""

def calcular_valor_peaje(tipo_vehiculo, cantidad_ejes, descuento_especial=False):
    """
    Calcula el valor del peaje según el tipo de vehículo y la cantidad de ejes.

    Parameters:
    - tipo_vehiculo (str): Tipo de vehículo ('AUTO', 'BUS' o 'CAMION').
    - cantidad_ejes (int): Cantidad de ejes del vehículo.
    - descuento_especial (bool): Indica si el vehículo tiene descuento especial (por paso frecuente).

    Returns:
    - int: Valor a pagar en el peaje.
    """
    if tipo_vehiculo == 'AUTO':
        valor_peaje = 10000
    elif tipo_vehiculo == 'BUS':
        valor_peaje = 14300
    elif tipo_vehiculo == 'CAMION':
        if cantidad_ejes == 2:
            valor_peaje = 16000
        elif 3 <= cantidad_ejes <= 4:
            valor_peaje = 28100
        elif cantidad_ejes == 5:
            valor_peaje = 37700
        else:
            valor_peaje = 41400
    else:
        # Tipo de vehículo no válido
        return "Tipo de vehículo no válido"

    # Aplicar descuento especial si es True
    if descuento_especial:
        valor_peaje -= valor_peaje * 0.15

    return int(valor_peaje)

# Ejemplo de uso
tipo_vehiculo = input("Ingrese el tipo de vehículo ('AUTO', 'BUS' o 'CAMION'): ")
cantidad_ejes = int(input("Ingrese la cantidad de ejes del vehículo: "))
descuento_especial = input("¿El vehículo tiene descuento especial? (True/False): ").lower() == 'true'

# Calcular y mostrar el valor del peaje
valor_peaje = calcular_valor_peaje(tipo_vehiculo, cantidad_ejes, descuento_especial)
print(f"El vehículo debe pagar {valor_peaje} en el peaje.")
