cadena = input("Introduce una cadena: ")

def es_repeticion(cadena):
	for i in range(1, len(cadena)):
		if cadena[i] != cadena[0]:
			return False
	return True

if es_repeticion(cadena):
	print("La cadena es una repeticion")
else:
	print("La cadena no es una repeticion")
