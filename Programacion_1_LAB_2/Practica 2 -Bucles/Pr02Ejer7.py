from turtle import *

pantalla = Screen()
tortuga = Turtle()
tortuga.speed(speed=10)
tortuga.shape("turtle")
tortuga.penup()

pantallaX = int(input('Introduce el ancho de la pantalla: '))
pantallaY = int(input('Introduce el alto de la pantalla: '))

anguloGiroInput = int(input("Angulo de giro: "))
separacionInput = int(input("Separacion de tortugas: "))

forwardGiro = 0
pantalla.setup(pantallaX,pantallaY)
while abs(tortuga.xcor())<= (pantallaX / 2) and abs(tortuga.ycor()) <= (pantallaY / 2):
    tortuga.forward(forwardGiro)
    tortuga.stamp()
    forwardGiro = forwardGiro + separacionInput
    tortuga.left(anguloGiroInput)
    print(tortuga.pos())
pantalla.exitonclick()