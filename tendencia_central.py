
""" Esta función utiliza la librería numpy de Python para realizar cálculos estadísticos sobre un conjunto de datos.

Define un conjunto de datos llamado datos.
Calcula la mediana de este conjunto usando np.median(datos).
Calcula el primer cuartil (Q1) y el tercer cuartil (Q3) mediante np.percentile(datos, 25) y np.percentile(datos, 75) 
respectivamente, que representan los valores que dividen al conjunto de datos en el 25% inferior y el 25% superior.
Calcula el rango intercuartil (IQR) restando Q1 de Q3.
Imprime los resultados, mostrando la mediana y el rango intercuartil.
En resumen, esta función realiza análisis estadístico básico sobre el conjunto de datos, incluyendo cálculos como la 
mediana y el rango intercuartil."""

import numpy as np

# Definir el conjunto de datos
datos = [6, 10, 18, 11, 16, 17, 13, 4, 10, 0, 18, 18, 3, 13, 10, 1, 8, 0, 16, 2]

# Calcular la mediana
mediana = np.median(datos)

# Calcular el primer cuartil (Q1) y el tercer cuartil (Q3)
Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)

# Calcular el rango intercuartil (IQR)
IQR = Q3 - Q1

# Imprimir los resultados
print(f"Mediana: {mediana}")
print(f"Rango Intercuartil (IQR): {IQR}")
