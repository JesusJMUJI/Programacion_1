def leer_matriz_enteros():
	# El código de la función debe ir aquí
	filas = int(input("Dime el número de filas: "))
	columnas = int(input("Dime el número de columnas: "))
	matriz = []
	for i in range(filas):
		matriz.append([])
		for j in range(columnas):
			matriz[i].append(int(input("Dime el valor de la fila " + str(i) + " y la columna " + str(j) + ": ")))
	return matriz


def mostrar_matriz_enteros(matriz):
	# El código de la función debe ir aquí
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print(matriz[i][j], end=" ")
		print()


# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__ == '__main__':
	# El código del programa principal debe ir aquí
	matriz = leer_matriz_enteros()
	mostrar_matriz_enteros(matriz)
