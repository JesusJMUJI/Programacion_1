from turtle import *
from math import *

screen = Screen()
screen.setup(800, 600)

tortuga = Turtle()
##square = int(input("Ingrese el tamaño del cuadrado: "))
squareTest = 90
cateto = sqrt(squareTest ** 2 + squareTest ** 2)
print(cateto)
tortuga.forward(squareTest)
tortuga.left(90)

tortuga.forward(squareTest)
tortuga.left(90)

tortuga.forward(squareTest)
tortuga.left(90)

tortuga.forward(squareTest)
tortuga.left(90)

tortuga.left(45)
tortuga.forward(cateto)

tortuga.left(135)
tortuga.forward(squareTest)

tortuga.left(135)
tortuga.forward(cateto)

tortuga.left(135)
tortuga.forward(squareTest)

tortuga.left(45)
tortuga.forward(squareTest)

tortuga.left(90)
tortuga.forward(squareTest)


screen.exitonclick()