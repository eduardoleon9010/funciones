# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:17:48 2024

@author: USUARIO
"""

def calcular_nota_final(examen1: float, examen2: float, examen_final: float) -> float:
    """
    Calcula la nota final del estudiante en un curso según reglas específicas.

    Parámetros:
    - examen1 (float): La nota del primer examen.
    - examen2 (float): La nota del segundo examen.
    - examen_final (float): La nota del examen final.

    Retorna:
    - float: La nota final del estudiante en el curso, redondeada a dos decimales.
    """
    # Verificar si el estudiante sacó más de 4.0 en el examen final
    if examen_final > 4.0:
        nota_final = round(examen_final, 2)
    # Verificar si el estudiante sacó menos de 2.0 en el examen final
    elif examen_final < 2.0:
        nota_final = round((examen1 + examen2 + (examen_final * 0.5)) / 2, 2)
    # En cualquier otro caso, los exámenes pesarán lo mismo
    else:
        nota_final = round((examen1 + examen2 + examen_final) / 3, 2)

    return nota_final

# Ejemplo de uso:
examen1 = float(input("Ingrese la nota del primer examen: "))
examen2 = float(input("Ingrese la nota del segundo examen: "))
examen_final = float(input("Ingrese la nota del examen final: "))

nota_final = calcular_nota_final(examen1, examen2, examen_final)
print(f"La nota final del estudiante es: {nota_final}")
