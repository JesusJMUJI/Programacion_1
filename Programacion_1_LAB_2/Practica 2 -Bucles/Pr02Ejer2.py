numero = int(input("Dime un numero: "))

for i in range (1, 100):
    if i ** 2 <= numero and (i + 1) ** 2 > numero:
        print('La raiz cuadrada del numero ' + str(numero) + ' es: ' + str(i))
    else:
        print('El numero introducido se encuentra fuera del rango asignado')