cadena = input('Dame una cadena: ')
cadenaNueva = ''
contador = 0
palabra = ''
for character in cadena:
    if character == ' ':
        cadenaNueva += palabra
        if len(palabra) >= 2:
            cadenaNueva = palabra + cadena[-2:]
        contador += 1
        palabra = ''
    else:
        palabra += character
        ant = character
if len(palabra) > 0:
    contador += 1
print('numero de palabras : ', contador)
print(cadenaNueva)
