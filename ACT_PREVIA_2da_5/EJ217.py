lista = []

while len(lista) < 3:
    userInput = int(input("Enter a number: "))
    lista.append(userInput)

for i in range(len(lista)):
    if  lista[i] < 0:
        lista[i] = 0

print(lista)