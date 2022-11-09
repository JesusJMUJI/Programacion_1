print("Práctica 3 - Ejercicio 6")
print("")

num = int(input('Dime un numero [-1 para acabar]: '))
lista = []

# Leer los dígitos de la lista
while num > 0:
    lista.append(num)
    num = int(input('Dime otro numero [-1 para acabar]: '))

# Calcular el numero
print(lista)
exponente = len(lista) - 1
numero = 0
for i in lista:
    numero = (i * (10 ** exponente)) + numero
    exponente -= 1

print(numero)
