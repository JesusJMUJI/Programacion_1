from modulo_test import test

def crear_lista_digitos (n):
	# El código de la función debe ir aquí
	numInput = n
	lista = []
	while numInput > 0:
		resto = numInput % 10
		numInput = numInput // 10
		lista = [resto] + lista
	return lista
# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__== '__main__':
	# El código del programa principal debe ir aquí
	numInput = int(input("Dime un números entero: "))
	print(crear_lista_digitos(numInput))
