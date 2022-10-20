lista = []
isPositive = False

while len(lista) < 10:
    userInput = int(input("Enter 10 numbers: "))
    if userInput > 0:
        lista.append(userInput)
        print(lista)
    else:
        print("Enter positive numbers only")