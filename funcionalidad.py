"""Esta documentación explica cada ejemplo, describe la funcionalidad y cómo interactúa con el 
usuario para realizar operaciones matemáticas, manipulación de cadenas y manejo de entrada/salida.
"""
# Ejemplo 1: Valor absoluto
numero = -5
valor_absoluto = abs(numero)  # Devuelve el valor absoluto de -5
print(valor_absoluto)

# Ejemplo 2: Redondeo
decimal = 3.14159
redondeado = round(decimal, 2)  # Redondea a 2 decimales
print(redondeado)

# Ejemplo 3: Mínimo y Máximo
numeros = [5, 2, 8, 1, 9]
minimo = min(numeros)  # Devuelve el valor mínimo (1)
maximo = max(numeros)  # Devuelve el valor máximo (9)
print(minimo, maximo)

# Funciones de Cadenas:
# Ejemplo 4: Longitud de una cadena
texto = "Hola, Mundo"
longitud = len(texto)  # Devuelve la longitud de la cadena
print(longitud)

# Ejemplo 5: Convertir a Mayúsculas y Minúsculas
mayusculas = texto.upper()  # Convierte a mayúsculas
minusculas = texto.lower()  # Convierte a minúsculas
print(mayusculas, minusculas)

# Funciones de Entrada/Salida:
# Ejemplo 6: Entrada del usuario
nombre = input("¿Cuál es tu nombre? ")
print("Hola,", nombre)

# Ejemplo 7: Salida en consola
resultado = 42
print("El resultado es:", resultado)

# Ejemplo 8: Conversión de tipo
entrada = input("Ingresa un número: ")
numero = float(entrada)  # Convierte la entrada a un número decimal
print(numero * 2)  # Realiza una operación matemática

# Calculo del volumen de una esfera usando entrada y conversión de tipos
cadena = input("Teclee el radio de la esfera: ")
radio = float(cadena)
volumen = 4/3 * 3.1416 * radio ** 3
print("El volumen de la esfera es:", volumen)

# Versión más compacta usando directamente la conversión de tipos dentro de la fórmula
volumen = 4/3 * 3.1416 * float(input("¿Cuál es el radio?")) ** 3
print("El volumen de la esfera es:", volumen)
