# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:59:59 2024

@author: USUARIO
"""

def construir_diccionario_alturas():
    """
    Diccionario con las alturas sobre el nivel del mar de las capitales de los países suramericanos.

    Retorno:
    - dict: Un diccionario donde las llaves son los nombres de las ciudades y los valores son las alturas sobre el nivel del mar.
    """
    # Inicializar el diccionario vacío
    alturas_capitales = {}

    # Agregar las alturas para cada capital
    alturas_capitales['Bogotá'] = 2640  # Altura de Bogotá en metros
    alturas_capitales['Buenos Aires'] = 25  # Altura de Buenos Aires en metros
    alturas_capitales['Lima'] = 154  # Altura de Lima en metros
    alturas_capitales['Asunción'] = 43  # Altura de Asunción en metros
    alturas_capitales['Quito'] = 2850  # Altura de Quito en metros
    alturas_capitales['Montevideo'] = 43  # Altura de Montevideo en metros
    alturas_capitales['Caracas'] = 920  # Altura de Caracas en metros
    alturas_capitales['Brasilia'] = 1172  # Altura de Brasilia en metros
    alturas_capitales['Santiago'] = 520  # Altura de Santiago en metros
    alturas_capitales['Lisboa'] = 220  # Altura de Lisboa en metros (Nota: No es capital suramericana, solo ejemplo adicional)

    return alturas_capitales

# Uso de la función para obtener el diccionario de alturas
diccionario_alturas = construir_diccionario_alturas()

# Imprimir el diccionario resultante
print(diccionario_alturas)
