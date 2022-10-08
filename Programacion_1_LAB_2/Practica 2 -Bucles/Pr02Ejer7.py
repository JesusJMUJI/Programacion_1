from turtle import *

pantalla = Screen()
pantalla.setup(400,400)
tortuga = Turtle()
tortuga.speed(speed=0)
distTortugas = int(input("Distancia entre tortugas: "))

while tortuga.pos() < (400,400):
    tortuga.forward(2+distTortugas/4)
    tortuga.left(30-distTortugas/12)

pantalla.exitonclick()

""" import turtle

a = turtle.Turtle()
for i in range(240):
    a.forward(2+i/4)
    a.left(30-i/12)

turtle.done() """