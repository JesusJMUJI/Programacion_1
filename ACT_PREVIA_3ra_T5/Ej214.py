print("Ejercicio 214")
print("")

filas = int(input('Dime el numero de filas: '))
column = int(input('Dime el numero de columnas: '))

# Crear las matrices vacías
A = []
for i in range(filas):
    A.append([0] * column)

B = []
for i in range(filas):
    B.append([0] * column)

# Leer la matriz A y B
print("Matriz A")
for i in range(filas):
    for j in range(column):
        A[i][j] = float(input('Dime el elemento ({0},{1}): '.format(i, j)))

print("Matriz B")
for i in range(filas):
    for j in range(column):
        B[i][j] = float(input('Dime el elemento ({0},{1}): '.format(i, j)))

# Primero se crea la matriz nula de C
C = []
for i in range(filas):
    C.append([0] * column)

# Se calcula la suma de A y B
for i in range(filas):
    for j in range(column):
        C[i][j] = A[i][j] - B[i][j]

# Se muestra la matriz C
print("La suma de las matrices A y B es:")
for i in range(filas):
    for j in range(column):
        print(C[i][j], end=' ')
    print()
