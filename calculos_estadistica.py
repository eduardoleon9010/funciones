"""Esta función realiza varias operaciones estadísticas sobre un conjunto de datos:

Calcula la mediana del conjunto de datos utilizando la función np.median() de NumPy.
Calcula el primer cuartil (Q1) y el tercer cuartil (Q3) utilizando la función np.percentile() 
de NumPy con argumentos de 25 y 75, respectivamente, para obtener los percentiles correspondientes.
Calcula el rango intercuartil (IQR) restando el tercer cuartil (Q3) menos el primer cuartil (Q1).
Imprime los resultados, mostrando la mediana y el rango intercuartil (IQR) calculados."""

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
