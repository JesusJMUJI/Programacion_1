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

for numero in range(0, 4):
    codigoRandom = codigoRandom + str(randint(1, 9))
print("Pista para probar: {0}, es el código aleatorio. Este numero es solo para hacer pruebas.".format(codigoRandom))

print("")
while not ganador:
    for i in inputCadena:
        x += 1
        for j in codigoRandom:
            y += 1
            if i == j and x == y:
                coincidenciasToros += 1
            elif i == j and x != y:
                coincidenciasVacas += 1
        y = 0
    if coincidenciasToros == 4:
        ganador = True
    else:
        print("HAS FALLADO: Toros: {0} y Vacas {1}".format(coincidenciasToros, coincidenciasVacas))
        coincidenciasToros = 0
        coincidenciasVacas = 0
        x = 0
        y = 0
        inputCadena = input("¿Cual es tu intento?: ")

print("Enhorabuena! Has acertado, el numero era: {0}".format(codigoRandom))