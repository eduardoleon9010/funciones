"""Hora de llegada de vuelo
Una agencia de viajes necesita informar a sus clientes la hora de llegada de 
sus vuelos. Se conoce la hora de partida del vuelo (en horas, minutos y 
                                                    segundos) y la duración 
del vuelo (en horas, minutos y segundos).

Cree una función que retorne la hora de llegada del vuelo en una cadena con
 el formato “HH:mm:ss” donde HH es la hora, mm los minutos y ss los segundos
 de la hora de llegada del vuelo. 

La hora está dada en formato de 24 horas. Si alguno de los 3 números de la 
respuesta es menor a 10, sólo se necesita un dígito ('7' en lugar de '07').

La solución tiene una función de acuerdo con la siguiente especificación:

Nombre de la función: calcular_horario_llegada

Descripción de parámetros:

Nombre               Tipo      Descripción
hora_salida           int      Hora de salida del vuelo (valor entre 0 y 23).
minuto_salida         int      Minuto de salida del vuelo (valor entre 0 y 59).
segundo_salida        int      Segundo de salida del vuelo (valor entre 0 y 59).
duracion_horas        int      Número de horas que dura el vuelo.
duracion_minutos      int      Número de minutos (adicionales al número de horas) que dura el vuelo.
duracion_segundos     int      Número de segundos (adicionales al número de horas y minutos) que dura el vuelo.

Descripción del retorno:

Tipo: str

Descripción:
Cadena que indica la hora de llegada del vuelo a su destino, la cadena debe 
estar en el formato “HH:mm:ss”.
"""

def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):
    # Convertir la hora de salida a segundos
    tiempo_salida = hora_salida * 3600 + minuto_salida * 60 + segundo_salida

    # Sumar la duración del vuelo en segundos
    tiempo_llegada = tiempo_salida + duracion_horas * 3600 + duracion_minutos * 60 + duracion_segundos

    # Ajustar la hora de llegada al formato de 24 horas
    horas_llegada = (tiempo_llegada // 3600) % 24
    minutos_llegada = (tiempo_llegada % 3600) // 60
    segundos_llegada = tiempo_llegada % 60

    # Formatear la cadena de la hora de llegada
    hora_llegada = f"{horas_llegada}:{minutos_llegada}:{segundos_llegada}"

    # Ajustar el formato de salida para eliminar ceros innecesarios
    hora_llegada = ':'.join([str(int(x)) if int(x) >= 10 else str(int(x)) for x in hora_llegada.split(':')])

    return hora_llegada

# Ejemplo de uso
hora_salida = 14
minuto_salida = 15
segundo_salida = 20
duracion_horas = 0
duracion_minutos = 52
duracion_segundos = 10

hora_llegada = calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos)
print(f"La hora de llegada del vuelo es: {hora_llegada}")
