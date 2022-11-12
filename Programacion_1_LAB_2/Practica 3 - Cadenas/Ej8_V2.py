print("Práctica 2 - Ejercicio 8")
print("")

numInput = int(input("Dime como de grande es la matriz (n x n): "))
M = []

# Creación de matriz
for f in range(numInput):
	M.append([0] * numInput)

# Adición de números
for fila in range(numInput):
	for columna in range(numInput):
		M[fila][columna] = columna - fila

# Mostrar la matriz
for fila in range(numInput):
	for columna in range(numInput):
		print(M[fila][columna], end=' ')
	print()
