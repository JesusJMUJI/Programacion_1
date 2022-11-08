print("Práctica 3 - Ejercicio 5")
print("")

numInput = int(input("Dime un números entero: "))
numDivision = 0
lista = []
resto = 0

while numInput > 0:
	resto = numInput % 10
	numInput = numInput // 10
	lista = [resto] + lista
print(lista)
