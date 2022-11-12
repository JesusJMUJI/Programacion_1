dni = int(input("Pon los numeros de tu DNI: "))


def letra_dni(dni):
	letras = "TRWAGMYFPDXBNJZSQVHLCKE"
	letra = letras[dni % 23]
	return letra


print("Tu DNI completo es: {0}-{1}".format(dni, letra_dni(dni)))
