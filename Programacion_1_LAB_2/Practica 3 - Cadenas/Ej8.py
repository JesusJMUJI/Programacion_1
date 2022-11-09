print("Práctica 2 - Ejercicio 8")
print("")

numInput = int(input("Dime como de grande es la matriz (n x n): "))
M = []
contador = 0
for fila in range(numInput):
	M.append([0] * numInput)

for fila in range(numInput):
	contador = 0
	for columna in range(numInput):
		if fila == columna:
			M[fila][columna] = 0
		elif fila < columna:
			if contador < 0:
				contador = 0
			contador += 1
			M[fila][columna] = contador
		elif fila > columna:
			contador -= 1
			M[fila][columna] = contador


for fila in range(numInput):
	for columna in range(numInput):
		print(M[fila][columna], end=' ')
	print()

print(M)
