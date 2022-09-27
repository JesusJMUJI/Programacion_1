peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura: "))
imc = (peso / (altura) ** 2)

print(round(imc , 2))

if imc >= 40:
    print("Obesidad Mórbida")
elif imc >= 30:
    print("Obesidad")
elif imc >= 25:
    print("Sobrepeso")
elif imc > 18.5 and imc < 24.99:
    print("peso Normal")
elif imc < 18.5:
    print("Peso Bajo")