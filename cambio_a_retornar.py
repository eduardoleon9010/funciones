def calcular_cambio(cambio):
    """
    Calcula la cantidad mínima de monedas para entregar un cambio dado.

    Pasos:
    1. Inicializa las denominaciones de monedas y una lista para registrar la cantidad de monedas a entregar.
    2. Itera a través de cada denominación para calcular la cantidad necesaria de esa denominación para cubrir el cambio.
    3. Genera un mensaje de salida con la cantidad de monedas de cada denominación en el formato solicitado.
    4. Retorna el mensaje que contiene la cantidad de monedas de cada denominación requerida para el cambio.

    Parámetros:
    cambio (int): El valor del cambio para el que se debe calcular la cantidad mínima de monedas.

    Retorna:
    (str): Un mensaje que indica la cantidad de monedas de cada denominación necesaria para el cambio dado, separadas por comas.

    Ejemplo de uso:
    >>> cambio = 950
    >>> resultado = calcular_cambio(cambio)
    >>> print(f"El cambio a entregar es: {resultado}")
    El cambio a entregar es: 1,2,0,1
    """
    denominaciones = [500, 200, 100, 50]
    cantidades = [0, 0, 0, 0]

    for i, denominacion in enumerate(denominaciones):
        cantidades[i] = cambio // denominacion
        cambio %= denominacion

    mensaje = ','.join(map(str, cantidades))
    
    return mensaje

# Ejemplo de uso
cambio = 950
resultado = calcular_cambio(cambio)
print(f"El cambio a entregar es: {resultado}")

