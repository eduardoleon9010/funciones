from datetime import date

def operaciones_basicas():
    """
    Realiza operaciones matemáticas básicas con dos números ingresados por el usuario.
    Calcula la suma, resta, multiplicación y división de estos números, mostrando cada resultado en la consola.
    Muestra la fecha actual antes de realizar las operaciones y finaliza con un mensaje "Fin".

    El usuario ingresa dos números enteros para llevar a cabo las operaciones.

    No recibe parámetros ni devuelve valores explícitos, muestra resultados en la consola.
    """
    hoy = date.today()  # Fecha actual
    print("Hoy es el día:", hoy)

    n1 = int(input("Digite el primer número: "))
    n2 = int(input("Digite el segundo número: "))

    suma = n1 + n2
    resta = n1 - n2
    producto = n1 * n2
    division = n1 / n2

    print("La suma es =", suma)
    print("La resta es =", resta)
    print("La multiplicación es =", producto)
    print("La división es =", division)
    print("Fin")

# Llamada a la función principal para realizar operaciones básicas
operaciones_basicas()
