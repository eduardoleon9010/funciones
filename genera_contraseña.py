"""Esta función genera contraseñas aleatorias con una longitud especificada por el usuario. Aquí está el detalle de cada paso:

import random, import string:
Importa dos módulos, random y string, necesarios para generar contraseñas aleatorias y trabajar con cadenas de caracteres respectivamente.

def generar_contrasena(longitud):
Esta función recibe un argumento longitud que determina cuántos caracteres tendrá la contraseña a generar. La variable caracteres contiene todos los caracteres posibles para la contraseña, incluyendo letras mayúsculas y minúsculas, dígitos y signos de puntuación. Luego, utilizando una comprensión de lista junto con random.choice, se eligen caracteres aleatorios de la cadena caracteres para formar la contraseña. La longitud de la contraseña generada será la misma que se pase como parámetro a la función. Finalmente, la función devuelve la contraseña generada.

Solicita la longitud de la contraseña al usuario:
Pide al usuario que ingrese la longitud deseada para la contraseña que se va a generar.

Genera la contraseña:
Utiliza la función generar_contrasena para obtener una contraseña aleatoria con la longitud ingresada por el usuario.

Muestra la contraseña generada:
Imprime por pantalla la contraseña recién generada para que el usuario pueda verla y usarla según sea necesario."""

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Solicita la longitud de la contraseña al usuario
longitud = int(input("Ingresa la longitud de la contraseña que deseas generar: "))

# Genera la contraseña
contrasena_generada = generar_contrasena(longitud)

# Muestra la contraseña generada
print("Contraseña generada:", contrasena_generada)
