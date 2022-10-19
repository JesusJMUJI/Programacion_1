cadena = input('')
contador = 0
palabra = ''
for character in cadena:
    if character == ' ':
        contador += 1
        palabra = ''
    else:
        palabra += character
        ant = character
if (len(palabra) > 0):
    contador+=1
print('numero de palabras : ', contador)

