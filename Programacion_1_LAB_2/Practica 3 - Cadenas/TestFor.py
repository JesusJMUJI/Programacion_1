print("Práctica 3 - Ejercicio 9")
print("")

# n = int(input("Dime como de grande es la matriz (n x n): "))
M = []
n=4
for z in range(n):
	M.append([0] * n)

M[0][0] = 7
M[0][1] = 12
M[0][2] = 5
M[0][3] = 3

M[1][0] = 0
M[1][1] = 8
M[1][2] = 10
M[1][3] = 0

M[2][0] = 0
M[2][1] = 0
M[2][2] = 9
M[2][3] = 1

M[3][0] = 0
M[3][1] = 0
M[3][2] = 0
M[3][3] = 3
# for i in range(n):
# 	for j in range(n):
# 		M[i][j] = int(input("Dime el elemento ({0},{1}): ".format(i, j)))

es_triangular = True
for x in range(1, n):  # Recorrido bucle de filas , desde fila 1 a fila n - 1
	#print("Estoy en fila, ", x)
	for y in range(0, x):
		#print("Estoy en columna: ", y)
		if M[x][y] != 0:
			es_triangular = False
			print("No triangular")
if es_triangular:
	print("triangular")