#aparcar.py

día = int(input('Dime que dia es hoy: '))

if 0 < día <= 15:
    print ( 'Puedes aparcar en el lado izquierdo de la calle' )
else:
    if día < 32:
        print ( 'Puedes aparcar en el lado derecho de la calle' )
    else:
        print ('Ningun mes tiene {0} días'.format(día))

""" 
Este programa siempre se ejecuta la línea 1 para pedir e dato al usuario. 
Una vez tiene este dato, se ejecuta la línea 5 y comprueba el día introducido
según los valores entre 0 y 15. 
Si el valor introducido esta fuera de este rango se 

"""


#estaciones.py

mes = int(input('Dime un mes: '))

if 1 <= mes <= 3:
    print('invierno.')
else:
    if mes == 4 or mes == 5 or mes == 6:
        print('Primavera')
    else:
        if not (mes < 7 or 9 < mes):
            print('verano')
        else:
            if not (mes != 10 and mes != 11 and mes != 12):
                print('Otoño')
            else:
                print('Ningun año tiene {0} meses'.format(mes))

#identificador.py

car = input('Dame un carácter: ')

if 'a' <= car.lower() <= 'z' or car == ' ':
    print ('Este carácter es válido en un identificador en Python 2.')
else:
    if not (car < '0' or '9' < car):
        print(' Un dígito es válido en un identificador en Python2,', end= '')
        print (' siempre que no sea el primer carácter')
    else:
        print ('Carácter no válido para formar un identificador en Python 2.')

# bisiesto.py

año = int(input('Dame un año: '))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print('El año {0} es bisiesto'.format(año))
else:
    print ('El año {0} es bisiesto'. format(año))