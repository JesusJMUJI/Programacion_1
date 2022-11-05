m = int(input('Dime el numero de filas: '))
n = int(input('Dime el numero de columnas: '))

# Crear la matriz
M = []
for i in range(m):
    M.append([0] * n)

# Leer la matriz
for i in range(m):
    for j in range(n):
        M[i][j] = float(input('Dime el elemento ({0},{1}): '.format(i, j)))
