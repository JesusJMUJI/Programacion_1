print ("Programa para la resolución de la ecuación a x + b = 0")

a = float (input("Valor de a: "))
b = float(input("Valor de b: "))

if a != 0:
    x = -b/a
    print("Solucion: ", x)

if a == 0: 
    if b != 0:
        print("la ecuacion no tiene solucion")
    if b == 0:
        print("La ecuacion tiene infinitas soluciones")