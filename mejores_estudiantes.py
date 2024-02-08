# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:19:42 2024

@author: USUARIO
"""

import pandas as pd

def mejores_estudiantes(estudiantes: pd.DataFrame) -> pd.DataFrame:
    """
    Construye un DataFrame con información sobre los mejores estudiantes en base a sus promedios de calificaciones.

    Args:
    estudiantes (DataFrame): DataFrame con las columnas 'nombre', 'matematicas', 'ingles', 'ciencias',
                             'literatura' y 'arte', donde aparecen las calificaciones de los estudiantes en cada
                             una de esas materias.

    Returns:
    DataFrame: DataFrame con las columnas 'nombre' y 'promedio', ordenado de forma descendente con respecto al
               promedio. En este DataFrame, aparecerá el 25% de los estudiantes del DataFrame original, que son
               considerados los mejores estudiantes.
    """
    # Calcula el promedio de calificaciones para cada estudiante
    estudiantes['promedio'] = estudiantes[['matematicas', 'ingles', 'ciencias', 'literatura', 'arte']].mean(axis=1).round(2)

    # Ordena los estudiantes por promedio de mayor a menor
    estudiantes_ordenados = estudiantes.sort_values(by='promedio', ascending=False)

    # Calcula el número de estudiantes que forman parte del 25% superior
    num_mejores_estudiantes = int(len(estudiantes) * 0.25)

    # Selecciona los mejores estudiantes
    mejores_estudiantes = estudiantes_ordenados.head(num_mejores_estudiantes)

    # Selecciona solo las columnas 'nombre' y 'promedio' y reindexa el DataFrame
    mejores_estudiantes = mejores_estudiantes[['nombre', 'promedio']].reset_index(drop=True)

    return mejores_estudiantes

# Ejemplo de uso
# Creamos un DataFrame de ejemplo
datos = {
    'nombre': ['Estudiante1', 'Estudiante2', 'Estudiante3', 'Estudiante4', 'Estudiante5'],
    'matematicas': [4.5, 5.0, 3.8, 4.2, 4.7],
    'ingles': [3.9, 4.8, 4.5, 4.1, 4.3],
    'ciencias': [4.2, 4.9, 3.7, 4.0, 4.5],
    'literatura': [4.3, 4.7, 4.1, 3.9, 4.6],
    'arte': [4.1, 4.5, 3.9, 3.8, 4.4]
}
estudiantes_df = pd.DataFrame(datos)

# Aplicamos la función para encontrar los mejores estudiantes
mejores_estudiantes_df = mejores_estudiantes(estudiantes_df)

# Mostramos el resultado
print("Mejores estudiantes:")
print(mejores_estudiantes_df)
