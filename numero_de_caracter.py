"""La función recorre una lista de caracteres y para cada carácter en la lista, 
encuentra su número correspondiente en el sistema Unicode utilizando la función
ord(). Luego, imprime cada carácter junto con su número Unicode."""

caracteres = ['z', 'G', '0', '1', '2', '$', '\\']

for caracter in caracteres:
    numero_unicode = ord(caracter)
    print(f"El número Unicode para '{caracter}' es: {numero_unicode}")

