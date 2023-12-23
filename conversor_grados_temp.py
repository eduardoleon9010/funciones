
"""Funcion que convierte graods Fahrenheit a grados centigrados.
Funcion que convirte grados centigrados a Fahtenheit.
Funcion que convierte radianes en grados. 360 grados son 2pi radianes
Funcion que convierte grados en radianes.
Funcion que recibe un numero entero positivo de cifras (4) y devuelve el numero invertido
"""

def fahrenheit_a_centigrados(grados_f:float)->float:
    grados_cent = (grados_f - 32)*(5/9)
    return grados_cent

def centtigrados_a_fahrenheit(grados_c:float)->float:
    grados_f = (grados_c*9/5) + 32
    return grados_f

def radianes_grados(radianes:float)->float:
    pi = 3.14159
    return(360*radianes)/(2*pi)

def grados_a_radianes(grados:float)->float:
    pi = 3.14159
    rad = (2*pi*grados)/360
    return rad

def invertir_numero(numero:int)->int:
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    millares = numero % 10
    
    #inverso = (unidades*1000)+(decenas*100)+(centenas*10)+(millares*1)
    inverso = str(unidades)+str(decenas)+str(centenas)+str(millares)
    return int(inverso)
    
    #return inverso
