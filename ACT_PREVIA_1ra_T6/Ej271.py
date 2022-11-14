num_for_lista = int(input("Ingrese la cantidad de números que desea ingresar: "))
lista = []
for i in range(num_for_lista):
	num = int(input("Ingrese un número: "))
	lista.append(num)


def media(lista):
	suma = 0
	for i in lista:
		suma += i
	return suma / len(lista)


print("La media de la lista es {0}".format(media(lista)))
