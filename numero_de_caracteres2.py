"""Esta función intenta imprimir los números Unicode para cada carácter en la lista caracteres. 
Sin embargo, algunos elementos en la lista contienen más de un carácter.

El código recorre cada elemento en la lista caracteres. Luego, para cada carácter en ese elemento, 
intenta obtener su número Unicode utilizando la función ord(). Finalmente, imprime el número 
Unicode de cada 
carácter individual presente en los elementos de la lista."""

caracteres = ['😢', '🇨🇴', '木']  # Verifica que cada elemento sea un único carácter

for caracter in caracteres:
    for char in caracter:
        numero_unicode = ord(char)
        print(f"El número Unicode para '{char}' es: {numero_unicode}")
