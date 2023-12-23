"""Esta función está destinada a calcular la cantidad mínima de monedas para entregar un cambio dado.

Aquí hay una descripción paso a paso de cómo funciona:

Inicialización de las denominaciones de monedas: La función comienza con una lista de denominaciones de monedas (500, 200, 100, 50) 
y una lista vacía para registrar la cantidad de monedas a entregar.

Iteración para calcular la cantidad de monedas: Utilizando un bucle, la función itera a través de cada denominación de moneda y 
calcula la cantidad necesaria de esa denominación para cubrir el cambio. Usa la división entera para obtener la cantidad de monedas 
de una denominación específica y ajusta el valor del cambio restante.

Generación del mensaje de salida: Se crea una cadena de texto que contiene la cantidad de monedas de cada denominación en el 
formato solicitado, separadas por comas.

Retorno del resultado: Finalmente, la función devuelve este mensaje que contiene la cantidad de monedas de cada denominación 
requerida para el cambio.

El ejemplo de uso al final muestra cómo utilizar esta función con un valor de cambio de 950. La función luego imprimirá un 
mensaje indicando la cantidad de monedas de cada denominación que se necesitan para ese cambio específico."""

def calcular_cambio(cambio):
    # Inicializamos las denominaciones de monedas y sus cantidades a entregar
    denominaciones = [500, 200, 100, 50]
    cantidades = [0, 0, 0, 0]
    mensaje = ""

    # Iteramos a través de cada denominación para calcular la cantidad de monedas a entregar
    for i, denominacion in enumerate(denominaciones):
        cantidades[i] = cambio // denominacion
        cambio %= denominacion

    # Creamos un string con la cantidad de monedas de cada denominación en el formato solicitado
    mensaje = ','.join(map(str, cantidades))
    
    return mensaje

# Ejemplo de uso
cambio = 950
resultado = calcular_cambio(cambio)
print(f"El cambio a entregar es: {resultado}")
