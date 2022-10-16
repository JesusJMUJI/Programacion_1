cadenaInput = input("Introduce una frase: ")

for caracter in range(len(cadenaInput)):
    if   cadenaInput[caracter] == 'a':
        cadenaInput = cadenaInput.replace('a', '.')
    elif cadenaInput[caracter] == 'e':
        cadenaInput = cadenaInput.replace('e', '.')
    elif cadenaInput[caracter] == 'i':
        cadenaInput = cadenaInput.replace('i', '.')
    elif cadenaInput[caracter] == 'o':
        cadenaInput = cadenaInput.replace('o', '.')
    elif cadenaInput[caracter] == 'u':
        cadenaInput = cadenaInput.replace('u', '.')

print(cadenaInput)