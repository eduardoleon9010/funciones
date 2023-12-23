"""
Esta función solicita al usuario dos números enteros, luego realiza operaciones 
matemáticas básicas con esos números ingresados. Calcula la suma, resta, multiplicación 
y división de estos números, mostrando cada resultado en la consola. Además, muestra la 
fecha actual antes de realizar las operaciones y finaliza con un mensaje "Fin" para 
indicar la conclusión del programa.
"""
from datetime import date
hoy = date.today()                #Fecha actual
print("Hoy es el dia: ", hoy)
n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
suma=n1+n2
resta=n1-n2
producto=n1*n2
division=n1/n2
print("La suma es = ",suma )
print("La resta es = ",resta )
print("La multiplicacion es = ",producto )
print("La division es = ",division)
print("Fin")
