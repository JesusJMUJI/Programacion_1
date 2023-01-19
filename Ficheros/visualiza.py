import os

try:
    fichero = open('ejemplo.txt', 'r')
    for linea in fichero:
        if linea [-1] == '\n':
            linea = linea[:-1]
        print(linea)
    fichero.close()
except IOError:
    print('El fichero no existe')
