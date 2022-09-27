from turtle import *

screen = Screen()
screen.setup(800, 600)
coordenadaX = int(input("Ingrese la coordenada X: "))
coordenadaY = int(input("Ingrese la coordenada Y: "))
""" coordenadaX = 100
testCoordenadaY = 100 """

radio = int(input("Ingrese el radio: "))
""" testR = 90 """

tortuga = Turtle()
tortuga.penup()
tortuga.goto(coordenadaX, coordenadaY)
tortuga.write(coordenadaX, coordenadaY)

tortuga.pendown()
tortuga.forward(radio)


tortuga.left(90)
tortuga.circle(radio)

tortuga.goto(coordenadaX, coordenadaY)

screen.exitonclick()