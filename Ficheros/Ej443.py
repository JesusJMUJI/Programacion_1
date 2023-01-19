# nom_fichero = input('Nombre del fichero: ')
nom_test = 'test.txt'
palabra_input = input('Que palabra quieres encontrar: ')
fichero = open(nom_test, 'r')

palabra_encontrada = False
palabra_formada = ''
palabra = ''
linea = fichero.readline()
while palabra_encontrada is False:
    for palabra in linea:
        if palabra == ' ' and palabra_formada == palabra_input:
            if palabra_formada == palabra_input:
                palabra_encontrada = True
            else:
                palabra_formada = ''
        palabra_formada += palabra

print(palabra_encontrada)
