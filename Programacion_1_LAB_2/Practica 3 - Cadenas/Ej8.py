print("Práctica 2 - Ejercicio 8")
print("")

n = int(input("Dime como de grande es la matriz (n x n): "))
M = []
for i in range(n):
	M.append([0] * n)

for i in range(n):
	for j in range(n):
		if i == j:
			M[i][j] = 0
		if i != j:
			M[i][j] = 1
			if i < j:
				M[i][j] = 2
				if i == j + 1:
					M[i][j] = -1
			if i > j:
				M[i][j] = -2
				if i == j + 1:
					M[i][j] = -1


for i in range(n):
	for j in range(n):
		print(M[i][j], end=' ')
	print()

print(M)
