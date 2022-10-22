from turtle import *

tortuga = Turtle()
screen = Screen()
screen.setup(800, 800)
tortuga.speed(speed=0)

lados = int(input("Lados del polígono: "))
longitud = int(input("Longitud del lado: "))
radioDecor = int(input("Radio del decorado: "))

for x in range(lados):
    tortuga.forward(longitud)
    tortuga.backward
    tortuga.left(360 / lados)

tortuga.penup()
tortuga.right(90)
tortuga.forward(radioDecor * 2)
tortuga.left(90)
tortuga.pendown()

inicioX = tortuga.xcor()
inicioY = tortuga.ycor()

anguloInterno = 360 / lados
for i in range(lados):
    distancia = tortuga.distance(inicioX, inicioY)
    while longitud - distancia >= radioDecor:
        tortuga.circle(radioDecor)
        tortuga.forward(radioDecor)
        distancia = tortuga.distance(inicioX, inicioY)
    tortuga.forward(radioDecor * 2)
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
