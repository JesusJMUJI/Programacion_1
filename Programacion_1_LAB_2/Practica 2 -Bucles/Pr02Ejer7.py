from turtle import *

pantalla = Screen()
pantalla.setup(400,400)
tortuga = Turtle()

distTortugas = int(input("Distancia entre tortugas: "))

while tortuga.pos() != (pantalla):
    tortuga.circle(distTortugas + 5)
    tortuga.left(15)