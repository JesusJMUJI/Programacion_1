print("Práctica 3 - Ejercicio 10")
print("")

# Datos
n = int(input("Dime como de grande es la matriz (n x n): "))
M = []

# Creación matriz nula
for z in range(n):
	M.append([0] * n)

# Lectura por teclado de matriz
for i in range(n):
	for j in range(n):
		M[i][j] = int(input("Dime el elemento ({0},{1}): ".format(i, j)))


es_latino = True
for fila in range(0, n):
	for col_comparador in range(0, n-1):
		comparador = M[fila][col_comparador]
		for columna in range(col_comparador + 1, n):
			if comparador == M[fila][columna]:
				es_latino = False

for columna in range(0, n):
	for fila_comparador in range(0, n-1):
		comparador = M[fila_comparador][columna]
		for fila in range(fila_comparador + 1, n):
			if comparador == M[fila][columna]:
				es_latino = False

if es_latino:
	print("La matriz : ")
	for i in range(n):
		for j in range(n):
			print(M[i][j], ",", end=' ')
		print()
	print('')
	print("Latino")
else:
	print("La matriz : ")
	for i in range(n):
		for j in range(n):
			print(M[i][j], ",", end=' ')
		print()
	print('')
	print("No latino")
