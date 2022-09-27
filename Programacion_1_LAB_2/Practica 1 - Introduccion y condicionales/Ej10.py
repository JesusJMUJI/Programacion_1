from turtle import *
from math import *

# Valores
screen = Screen()
screen.setup(1024, 1024)
tortuga = Turtle()

l = int(input("Ingrese el lado del cuadrado: "))
cateto = sqrt(l ** 2 + l ** 2)
x = int(input("Ingrese la coordenada X: "))
y = int(input("Ingrese la coordenada Y: "))

# Codigo Tortuga
tortuga.penup()
tortuga.dot(5, "black")

# Centrar cuadrado
tortuga.right(90)
tortuga.forward(l)
tortuga.left(90)

# Dibujar cuadrado
tortuga.pencolor("red")
tortuga.pendown()
tortuga.forward(l)
tortuga.left(90)
tortuga.forward(l * 2)
tortuga.left(90)
tortuga.forward(l * 2)
tortuga.left(90)
tortuga.forward(l * 2)
tortuga.left(90)
tortuga.forward(l)
tortuga.left(90)

# Dibujar circulo
tortuga.pencolor("blue")
tortuga.penup()
tortuga.forward(l)
tortuga.right(90 + 45)
tortuga.forward(cateto)
tortuga.pendown()
tortuga.left(45 + 45)
tortuga.circle(cateto)

# Dibujar puntos con if's
tortuga.penup()
tortuga.goto(x, y)

if x < l and y < l:
    tortuga.dot(10, "red")
elif x > l and y > l:
    tortuga.dot(10, "green")
else:
    tortuga.dot(10, "blue")


screen.exitonclick()