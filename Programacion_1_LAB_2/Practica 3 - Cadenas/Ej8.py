print("Práctica 2 - Ejercicio 8")
print("")

n = int(input("Dime como de grande es la matriz (n x n): "))
M = []
for i in range(n):
	M.append([0] * n)
for i in range(n):
	M[i][i] = 0
	M[i][i] = 1

print(M)