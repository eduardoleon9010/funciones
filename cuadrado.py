"""Esta función, junto con los ejemplos proporcionados, demuestra el uso de funciones en Python.
cuadrado(x: float) -> float: Esta función calcula el cuadrado de un número dado. Toma un parámetro 
x y devuelve x ** 2, es decir, x elevado al cuadrado.
El programa principal (código que no está dentro de funciones) muestra cómo usar estas funciones:
print(cuadrado(2)): Calcula el cuadrado de 2 y muestra el resultado (4).
a = 1 + cuadrado(3): Calcula el cuadrado de 3, le suma 1 y asigna el resultado a a (10).
print(cuadrado(a*3)): Calcula el cuadrado de a multiplicado por 3 (100).
Luego, la función cubo(x: float) -> float calcula el cubo de un número dado y se demuestra su uso 
imprimiendo el resultado del cubo de 2.
La función area_rectangulo(altura: float, ancho: float) -> float calcula el área de un rectángulo 
dada su altura y ancho. Solicita al usuario que ingrese la altura y el ancho y luego imprime el 
área del rectángulo con esos valores.
Finalmente, la función leer_entero() -> int solicita al usuario que ingrese un número entero y 
devuelve ese número.
Estos ejemplos muestran cómo definir funciones, usar parámetros, invocar funciones con argumentos 
y manejar valores de retorno."""

def cuadrado(x: float)->float:
    return x**2

    """
        Calcula el cuadrado de un nuemero dado
    """
    return x ** 2

#Programa principal
print(cuadrado(2))   #Argumento es el valor que damos al parametro cuando llamamos la funcion
a = 1 + cuadrado(3)  #En este caso los argumentos de los parametros son 2, 3, y dado que a tiene el valor 10 el ultimo valor es 30
print(cuadrado(a*3))    

#Funciones diferentes son independientes
def cubo(x: float)->float: #Las dos funciones reciben un parametro cada una. Puede tener el mimo nombre, son parametros DIFERENTES porque estan en funciones diferentes
    return x*x*x
y = 2                   #y, es una variable que guarda el valor 2
print(cubo(y))

"""
El parametro de la funcion es (x), pero el argunmento con el que se invoca
es el valor de la variable (y). Lo que importa en el llamado es el VALOR 
"""

def area_rectangulo(altura: float, ancho: float)->float:
    return altura * ancho

x = float(input("Digita la altura: "))
y = float(input("Digite el ancho: "))
area = area_rectangulo(x, y)
print("El area del rectangulo es: ", area)


def area_rectangulo_2(altura: float, ancho: float)->float:
    area = altura * ancho
    return area


def leer_entero()->int:
    return int(input())

a = leer_entero()
print("El entero que tecleo es: ", str(a))
