lista_num = ["uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez"]
num = (input('Dame un numero: '))


def num_letras(lista_num, num):
	lista_nueva = []
	for palabra in lista_num:
		for character in palabra:
			if character == num:
				lista_nueva.append(palabra)
	return lista_nueva


print("Es:{0}".format(num_letras(lista_num, num)))
