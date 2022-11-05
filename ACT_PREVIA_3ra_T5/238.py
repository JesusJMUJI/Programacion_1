M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
s = 0.0
for i in range(0,3):
    for j in range(0,3):
        s = s + M[i][j]
print(s / 9)

# Resultado = 0.3333333333333333
