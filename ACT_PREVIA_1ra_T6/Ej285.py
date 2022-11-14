numero_DNI = int(input("Ingrese el numero de DNI: "))
letra_DNI = input("Ingrese la letra de DNI: ")


def es_dni(numero_dni, letra_dni):
	letras = "TRWAGMYFPDXBNJZSQVHLCKE"
	return letras[numero_dni % 23] == letra_dni

print(es_dni(numero_DNI, letra_DNI))