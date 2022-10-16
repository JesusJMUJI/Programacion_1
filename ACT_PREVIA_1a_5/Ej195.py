input = str(input("Introduce una frase: "))
cadena = ''

for character in range(len(input)):
    cadena += input[character]
    print(cadena)