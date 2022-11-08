print("Práctica 3 - Ejercicio 7")
print("")

numInput = int(input("Dime un número entero: "))
numInputSumando = int(input('Dime otro numero para sumar: '))
numDivision = 0
lista = []
listaSuma = []
resto = 0
restoSuma = 0

suma = numInput + numInputSumando

while numInput > 0:
	resto = numInput % 10
	numInput = numInput // 10
	lista = [resto] + lista

while numInputSumando > 0:
	resto = numInputSumando % 10
	numInputSumando = numInputSumando // 10
	listaSuma = [resto] + listaSuma

listaTotal = []
for i in range(len(lista)):
	listaTotal.append(lista[i] + listaSuma[i])
print(listaTotal)
