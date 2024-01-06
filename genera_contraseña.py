import random
import string

def generar_contrasena(longitud):
    """
    Genera una contraseña aleatoria con la longitud especificada.

    Parámetros:
    longitud (int): La longitud de la contraseña a generar.

    Retorna:
    (str): La contraseña aleatoria generada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Solicita la longitud de la contraseña al usuario
longitud = int(input("Ingresa la longitud de la contraseña que deseas generar: "))

# Genera la contraseña
contrasena_generada = generar_contrasena(longitud)

# Muestra la contraseña generada
print("Contraseña generada:", contrasena_generada)
