from random import random
from turtle import *

pantalla = Screen()
pantalla.setup(400,400)
tortuga = Turtle()

radPerimetro = int(input("Radio del perímetro: "))
numPasos = int(input("Número máximo de pasos: "))

while tortuga.pos() != (pantalla):
    tortuga.forward(20)
    tortuga.left(random)