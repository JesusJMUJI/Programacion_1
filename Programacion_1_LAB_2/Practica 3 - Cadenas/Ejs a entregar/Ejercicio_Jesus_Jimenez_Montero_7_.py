print("Práctica 3 - Ejercicio 7")
print("")

numInput = int(input("Dime un número entero: "))
numInputSumando = int(input('Dime otro numero para sumar: '))

lista = []
resto = 0
while numInput > 0:
	resto = numInput % 10
	numInput = numInput // 10
	lista = [resto] + lista

listaSuma = []
restoSuma = 0
while numInputSumando > 0:
	resto = numInputSumando % 10
	numInputSumando = numInputSumando // 10
	listaSuma = [resto] + listaSuma

listaTotal = []
acarreo = 0
suma = 0
for i in range(len(lista), 0, -1):
	suma = lista[i - 1] + listaSuma[i - 1] + acarreo
	acarreo = suma // 10
	resto = suma % 10
	listaTotal = [resto] + listaTotal
if acarreo != 0:
	listaTotal = [acarreo] + listaTotal
print(listaTotal)
