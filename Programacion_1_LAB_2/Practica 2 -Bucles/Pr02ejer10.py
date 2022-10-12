from functools import total_ordering
from turtle import *

tortuga = Turtle()
screen= Screen()
screen.setup(800,800)
tortuga.speed(speed=10)

lados = int(input("Lados del polígono: "))
longitud = int(input("Longitud del lado: "))
radioDecor = int(input("Radio del decorado: "))
""" conteoLados = 0
maxCirculos= 0 """

for x in range(lados):
    tortuga.forward(longitud)
    tortuga.left(360 / lados)
    tortuga.write(tortuga.pos())
    print(tortuga.pos())

tortuga.penup()
tortuga.right(90)
tortuga.forward(radioDecor*2)
tortuga.left(90)
tortuga.pendown()

anguloInterno = 360 / lados
print(anguloInterno)
for i in range(lados):
    inicioX = tortuga.xcor()
    inicioY = tortuga.ycor()
    distancia = tortuga.distance(inicioX,inicioY)
    while longitud - distancia >= radioDecor:
        tortuga.circle(radioDecor)
        tortuga.forward(radioDecor)
        distancia = tortuga.distance(inicioX,inicioY)
        print(distancia)
    tortuga.left(anguloInterno)

""" while maxCirculos < lados:
    print('Multiplicacion de lados ' + str(multipliLados))
    print('MaxCiruclos '+ str(maxCirculos))
    maxCirculos += 1
    while conteoLados < lados:
        conteoLados += 1
        tortuga.circle(radioDecor)
        tortuga.forward(radioDecor * 2)
        print(conteoLados)
    conteoLados -= (lados)
    tortuga.backward(radioDecor)
    tortuga.left(360 / lados)
    tortuga.forward(radioDecor)
    print(conteoLados) """

screen.exitonclick()