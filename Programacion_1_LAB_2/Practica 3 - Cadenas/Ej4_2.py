from random import randint
print("Práctica 3 - Ejercicio 4")
print("")

print("Juego de Toros y Vacas")
print("Dime un numero entre 1 a 9 y averigua el numero aleatorio")
inputCadena = input("¿Cual es tu intento?: ")
codigoRandom = ""
contadorIndice = 0
coincidenciasToros = 0
coincidenciasVacas = 0
ganador = False
x = 0
y = 0


for numero in range(0,4):
    codigoRandom = codigoRandom + str(randint(1,9))
print(codigoRandom)

for i in inputCadena:
    x+=1
    for j in codigoRandom:
        y += 1
        if i == j:
            if x == y:
                coincidenciasToros += 1
            else:
                coincidenciasVacas += 1

print("Toros: " + str(coincidenciasToros) + "Vacas: " + str(coincidenciasToros))
    




