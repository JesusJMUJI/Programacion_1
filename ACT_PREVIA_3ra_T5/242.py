print("Ejercicio 242")
print("")
filas = int(input("Dime el numero de filas: "))
column = int(input("Dime el numero de columnas: "))
producto = int(input("¿Por cuanto quires multiplicar cada componente?: "))

# Crear la matriz vacías
A = []
for i in range(filas):
    A.append([0] * column)

matrizProducto = []
for i in range(filas):
    matrizProducto.append([producto])

# Leer la matriz
for i in range(filas):
    for j in range(column):
        A[i][j] = float(input("Dime el elemento ({0},{1}): ".format(i, j)))

# Creacion de la matriz nula de C
C = []
for i in range(filas):
    C.append([0] * column)

# Cálculo de producto de la matriz
for i in range(filas):
    for j in range(column):
        C[i][j] = A[i][j] * matrizProducto[i][j]

# Mostrar la matriz de C
for i in range(filas):
    for j in range(column):
        print(C[i][j], end="")
    print()
