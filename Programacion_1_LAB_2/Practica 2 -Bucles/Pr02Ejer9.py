from random import *
from turtle import *
pantalla = Screen()
pantalla.setup(800,800)
tortuga = Turtle()
tortuga.speed(speed=10)

grosor = randint(1,20)
redvar = random()
greenvar = random()
bluevar = random()

userInput = True

while userInput:
    numDibujos = int(input("Numero de dibujos: "))
    for x in range(numDibujos):
        tortuga.pensize(grosor)
        tortuga.pencolor(redvar,greenvar,bluevar)
        tortuga.forward(randint(1,100))
        tortuga.left(randint(1,360))
        redvar = random()
        greenvar = random()
        bluevar = random()
        grosor = randint(1,20)
    userInput = input("Desea continuar? (y/n): ")
    if userInput == "n":
        pantalla.exitonclick()
pantalla.exitonclick()