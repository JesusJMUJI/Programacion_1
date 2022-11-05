print("Ejercicio 240")
print("")
n = int(input("Dime como de grande es la matriz (n x n): "))
M = []
for i in range(n):
    M.append([0] * n)
    M[i][i] = 1
print(M)
