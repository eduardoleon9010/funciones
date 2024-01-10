# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:21:23 2024

@author: USUARIO
"""
def calcular_iva_propina_total_factura(costo_factura: int) -> str:
    """Calcula el IVA, la propina y el total de la factura en un restaurante.
    
    Parámetros:
    costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina.
    
    Retorna:
    str: Cadena con el IVA, la propina y el total de la factura, separados por coma.
    """
    IVA = round(costo_factura * 0.19)
    propina = round(costo_factura * 0.10)
    total = costo_factura + propina + IVA

    resultado = f"X: {IVA}, Propina: {propina}, Total: {total}"
    return resultado

# Solicitar al usuario el costo de la factura
costo = int(input("Ingrese el costo de la factura: "))
resultado = calcular_iva_propina_total_factura(costo)
print(resultado)

