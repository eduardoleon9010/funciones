"""Esta función, está diseñada para calcular la diferencia de edad entre dos fechas proporcionadas 
en términos de días, meses y años.

El método utiliza la diferencia entre las fechas de nacimiento y la fecha actual para calcular la 
edad en días. Luego, convierte esta diferencia en años, meses y días, devolviendo estos valores en 
formato de cadena "aa,MM,dd", donde "aa" representa años, "MM" representa meses y "dd" representa días.

Para hacer esto, la función sigue estos pasos:

Calcula la cantidad total de días transcurridos desde la fecha de nacimiento y la fecha actual.
Determina la cantidad de años completos contando la cantidad de días en un año.
Usa el resto de los días para calcular la cantidad de meses completos y los días restantes después 
de los años y meses completos.
Luego, se devuelve la edad en el formato mencionado anteriormente.

Los casos de prueba que se incluyen en el código permiten verificar si la función produce los resultados
esperados cuando se ingresan fechas específicas. Estos casos de prueba incluyen fechas de nacimiento y 
fechas actuales diferentes para validar la precisión de la función."""

def calcular_edad(dia_nacio, mes_nacio, anio_nacio, dia_actual, mes_actual, anio_actual):
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
print(calcular_edad(28, 12, 2004, 28, 3, 2005))  # Esperado: 0,3,0
print(calcular_edad(25, 10, 1993, 4, 8, 2019))   # Esperado: 25,9,9



