# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:25:56 2024

@author: USUARIO
"""

def producto_mas_barato(catalogo):
    """
    Encuentra el artículo más barato en un catálogo y devuelve su nombre.

    Args:
    - catalogo (dict): Un diccionario que contiene los nombres de los productos como llaves
                       y sus respectivos precios como valores.

    Returns:
    - str: El nombre del artículo más barato en el catálogo. Si no hay ningún artículo que valga
           menos de 10.000, retorna None. Si el catálogo está vacío, retorna la cadena 
           "No hay productos para escoger".
    """
    # Verificar si el catálogo está vacío
    if not catalogo:
        return "No hay productos para escoger"
    
    # Inicializar variables para el precio mínimo y el nombre del producto más barato
    precio_minimo = float('inf')
    producto_mas_barato = None
    
    # Iterar sobre el catálogo para encontrar el producto más barato
    for producto, precio in catalogo.items():
        # Convertir el nombre del producto a minúsculas para comparar alfabéticamente
        producto_lower = producto.lower()
        
        # Actualizar el producto más barato si se encuentra un precio menor
        if precio < precio_minimo:
            precio_minimo = precio
            producto_mas_barato = producto
        # En caso de empate, comparar alfabéticamente
        elif precio == precio_minimo and producto_lower < producto_mas_barato.lower():
            producto_mas_barato = producto
    
    # Verificar si el precio del producto más barato es menor que 10,000
    if precio_minimo < 10000:
        return producto_mas_barato
    else:
        return None

# Ejemplo de catálogo de productos
catalogo = {
    "Camiseta": 8000,
    "Pantalón": 12000,
    "Zapatos": 7000,
    "Bufanda": 5000
}

# Llamada a la función para encontrar el producto más barato
producto_menor_precio = producto_mas_barato(catalogo)
print("El producto más barato es:", producto_menor_precio)