from turtle import *

tortuga = Turtle()
screen= Screen()
screen.setup(1000,1000)

lados = int(input("Lados del polígono: "))
longitud = int(input("Longitud del lado: "))

for x in range(lados):
    tortuga.forward(longitud)
    tortuga.right(360 / lados)

screen.exitonclick()