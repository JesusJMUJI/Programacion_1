from turtle import *
from math import *

screen = Screen()
screen.setup(800, 600)

tortuga = Turtle()
square = int(input("Ingrese el tamaño del cuadrado: "))
#squareTest = 90
cateto = sqrt(square ** 2 + square ** 2)
print(cateto)

tortuga.forward(square)
tortuga.left(90)

tortuga.forward(square)
tortuga.left(90)

tortuga.forward(square)
tortuga.left(90)

tortuga.forward(square)
tortuga.left(90)

tortuga.left(45)
tortuga.forward(cateto)

tortuga.left(135)
tortuga.forward(square)

tortuga.left(135)
tortuga.forward(cateto)

tortuga.left(135)
tortuga.forward(square)

tortuga.left(45)
tortuga.forward(cateto / 2)

tortuga.left(90)
tortuga.forward(cateto / 2)

screen.exitonclick()