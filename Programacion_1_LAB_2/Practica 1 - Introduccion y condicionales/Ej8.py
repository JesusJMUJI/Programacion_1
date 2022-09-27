from turtle import *

screen = Screen()
screen.setup(800, 600)

coordenadaX = int(input("Ingrese la coordenada X: "))
coordenadaY = int(input("Ingrese la coordenada Y: "))

radio = int(input("Ingrese el radio: "))
tortuga = Turtle()

tortuga.penup()
tortuga.goto(coordenadaX, coordenadaY)
tortuga.write((coordenadaX, coordenadaY) , True, align="center")
tortuga.dot(5, "black")

tortuga.pendown()
tortuga.forward(radio)
tortuga.write("radio =" + str(radio), align="right")

tortuga.left(90)
tortuga.circle(radio)

tortuga.right(90)
tortuga.backward(radio)

#tortuga.goto(coordenadaX, coordenadaY)

screen.exitonclick()