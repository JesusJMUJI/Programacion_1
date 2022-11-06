cadena = input('Dame una cadena: ')
cadenaNueva = ''
contador = 0
palabra = ''
ant = ''
for caracter in cadena:
    if caracter == ' ':
        cadenaNueva = cadenaNueva + palabra
        if len(palabra) >= 2:
            cadenaNueva += palabra[-2:] + " "
        else:
            cadenaNueva = cadenaNueva + ' '
        contador += 1
        palabra = ''
    else:
        palabra += caracter
        ant = caracter

if len(palabra) >= 2:
    cadenaNueva += palabra + palabra[-2:]

if len(palabra) > 0:
    contador += 1
print('numero de palabras : ', contador)
print(cadenaNueva)
