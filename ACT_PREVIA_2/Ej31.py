from math import sqrt

print("Actividad Previa 2 - Programacion 1")

print("Calculadora de area y perimetro de un cuadrado")

numInput1 = float(input("Dime un lado: "))
numInput2 = float(input("Dime otro lado: "))
numInput3 = float(input("Dime un ultimo lado: "))

p = (numInput1 + numInput2 + numInput3)
print('Perímetro del triángulo: ' + str(p))

pDiv = (p /2)

a = sqrt(pDiv*(pDiv - numInput1)*(pDiv - numInput2)*(pDiv - numInput3))
print('Area del triangulo: '+str(a))