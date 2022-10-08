from random import *
from turtle import *
pantalla = Screen()
pantalla.setup(800,800)
tortuga = Turtle()
tortuga.speed(speed=10)

numDibujos = int(input("Numero de dibujos: "))
grosor = randint(1,20)
redvar = random()
greenvar = random()
bluevar = random()

for x in range(numDibujos):
    tortuga.pensize(grosor)
    tortuga.pencolor(redvar,greenvar,bluevar)
    tortuga.forward(randint(1,100))
    tortuga.left(randint(1,360))
    redvar = random()
    greenvar = random()
    bluevar = random()
    grosor = randint(1,20)

pantalla.exitonclick()