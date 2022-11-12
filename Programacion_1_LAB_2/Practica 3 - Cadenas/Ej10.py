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

numero_celda = 0
anterior = 0
es_latino = True
for fila in range(0, n):
	anterior = 0
	for columna in range(0, n):
		numero_celda = M[fila][columna]
		if numero_celda == anterior:
			es_latino = False
		anterior = numero_celda

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