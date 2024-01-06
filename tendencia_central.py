import numpy as np

def calcular_estadisticas(datos):
    """
    Realiza cálculos estadísticos sobre un conjunto de datos utilizando la librería NumPy.

    Parámetros:
    datos (list): Un conjunto de datos numéricos.

    Proceso:
    - Calcula la mediana del conjunto de datos utilizando np.median(datos).
    - Calcula el primer cuartil (Q1) y el tercer cuartil (Q3) mediante np.percentile(datos, 25) y np.percentile(datos, 75) respectivamente.
    - Calcula el rango intercuartil (IQR) restando Q1 de Q3.

    Retorna:
    (float, float): Retorna la mediana y el rango intercuartil (IQR) calculados.

    Ejemplo:
    calcular_estadisticas([6, 10, 18, 11, 16, 17, 13, 4, 10, 0, 18, 18, 3, 13, 10, 1, 8, 0, 16, 2])
    Salida esperada: (10.0, 12.0)
    """
    # Calcular la mediana
    mediana = np.median(datos)

    # Calcular el primer cuartil (Q1) y el tercer cuartil (Q3)
    Q1 = np.percentile(datos, 25)
    Q3 = np.percentile(datos, 75)

    # Calcular el rango intercuartil (IQR)
    IQR = Q3 - Q1

    return mediana, IQR

# Ejemplo de uso
datos_ejemplo = [6, 10, 18, 11, 16, 17, 13, 4, 10, 0, 18, 18, 3, 13, 10, 1, 8, 0, 16, 2]
mediana_resultado, IQR_resultado = calcular_estadisticas(datos_ejemplo)
print(f"Mediana: {mediana_resultado}")
print(f"Rango Intercuartil (IQR): {IQR_resultado}")
