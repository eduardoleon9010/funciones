def calcular_edad(dia_nacio, mes_nacio, anio_nacio, dia_actual, mes_actual, anio_actual):
    """
    Calcula la diferencia de edad entre dos fechas proporcionadas en días, meses y años.

    Args:
    dia_nacio (int): Día de nacimiento.
    mes_nacio (int): Mes de nacimiento.
    anio_nacio (int): Año de nacimiento.
    dia_actual (int): Día actual.
    mes_actual (int): Mes actual.
    anio_actual (int): Año actual.

    Returns:
    str: Diferencia de edad en formato "aa,MM,dd", donde "aa" representa años,
    "MM" representa meses y "dd" representa días.
    """

    # Calcular la diferencia entre las fechas
    dias_nac = dia_nacio + (mes_nacio - 1) * 30 + (anio_nacio - 1) * 365
    dias_act = dia_actual + (mes_actual - 1) * 30 + (anio_actual - 1) * 365

    # Calcular la edad en días
    edad_en_dias = dias_act - dias_nac

    # Calcular años, meses y días
    anos = edad_en_dias // 365
    meses = (edad_en_dias % 365) // 30
    dias = (edad_en_dias % 365) % 30

    # Retornar la edad en formato "aa,MM,dd"
    return f"{anos},{meses},{dias}"

# Casos de prueba
print(calcular_edad(28, 12, 2004, 28, 3, 2005))  # Esperado: 0,3,5
print(calcular_edad(25, 10, 1993, 4, 8, 2019))   # Esperado: 25,9,14



