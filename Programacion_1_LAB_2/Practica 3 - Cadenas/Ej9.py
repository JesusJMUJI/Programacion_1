print("Práctica 3 - Ejercicio 9")
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

# Bucle para comprobar si es triangular
es_triangular = True
for x in range(1, n):  # Recorrido bucle de filas , desde fila 1 a fila n
	for y in range(0, x):  # Recorrido de columnas, desde 0 a x
		if M[x][y] != 0:
			es_triangular = False

# Mostrar la matriz y si es triangular superior o no
if es_triangular:
	print("La matriz : ")
	for i in range(n):
		for j in range(n):
			print(M[i][j], end=' ')
		print()
	print('')
	print("Es triangular superior")
else:
	print("La matriz : ")
	for i in range(n):
		for j in range(n):
			print(M[i][j], end=' ')
		print()
	print('')
	print("No es triangular superior")
