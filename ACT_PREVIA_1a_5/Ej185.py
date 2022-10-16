from re import A


cadenaInput = input("Introduce una frase: ")

encriptador = ''
for caracter in cadenaInput:
    if caracter == 'a':
        caracter.replace('a', '.')

print(cadenaInput)