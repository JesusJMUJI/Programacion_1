nom_fichero = input('Nombre del fichero: ')
fichero = open(nom_fichero, 'r')

caracteres = 0
linea = fichero.readline()
while linea != '':
    caracteres += len(linea)
    linea = fichero.readline()
fichero.close()
print('Numero de caracteres: {0}'.format(caracteres))