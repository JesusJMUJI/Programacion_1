nombre = input('Nombre del fichero: ')
fichero = open(nombre, 'r')

contador = 0
for linea in fichero:
    contador += 1

fichero.close()
print(contador)
