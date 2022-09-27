from turtle import *

screen = Screen()

l = int(input("Ingrese el lado del cuadrado: "))
tortuga = Turtle()

tortuga.penup()
tortuga.write(tortuga.position(), True, align="center")
tortuga.right(90)
tortuga.forward(l)

tortuga.left(90)
tortuga.pendown()
tortuga.circle(l)

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

tortuga.penup()
tortuga.forward(l)


screen.exitonclick()