from turtle import Turtle
from turtle import Screen
import math

tortuga = Turtle()
screen = Screen()
screen.setup(800,800)
#tortuga.speed(10)

lados = int(input("Lados del polígono: "))
longitud = int(input("Longitud del lado: "))
radioDecor = int(input("Radio del decorado: "))
anguloInterno = 360 / lados

for x in range(lados):
# Recoger punto inicial
    inicioX = tortuga.xcor()
    inicioY = tortuga.ycor()
# Crear el lado, recoger el punto final 
# y volver al punto inicial del lado
    tortuga.forward(longitud)
    finX = tortuga.xcor()
    finY = tortuga.ycor()
    tortuga.goto(inicioX,inicioY)
# Ir a la posición para el decorado
    tortuga.penup()
    tortuga.right(90)
    tortuga.forward(radioDecor * 2)
    tortuga.left(90)
    tortuga.pendown()
# Crear tantos circulos mientras la tortuga no supere
# finX y finY
    posX = [tortuga.xcor(),tortuga.ycor()]
    
    while math.dist(posX,) < (finX,finY):

        tortuga.circle(radioDecor)
        tortuga.forward(radioDecor)
    tortuga.penup()
    tortuga.goto(finX,finY)
    tortuga.left(anguloInterno)
    tortuga.pendown()