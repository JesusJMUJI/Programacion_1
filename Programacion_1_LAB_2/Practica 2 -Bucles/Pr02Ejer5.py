from turtle import *
pantalla = Screen()
pantalla.setup(800,800)
tortuga = Turtle()

radio = int(input("Radio: "))
numPuntos = int(input("Numero de puntos: "))

tortuga.dot()
tortuga.penup()
tortuga.right(90)
tortuga.forward(radio)
tortuga.left(90)
tortuga.pendown()

tortuga.circle(radio)

for x in range(numPuntos):
    coordX = int(input('Coordenada X: '))
    coordY = int(input("Coordenada Y: "))
    tortuga.penup()
    tortuga.goto (coordX, coordY)
    tortuga.pendown()
    tortuga.dot()

pantalla.exitonclick()