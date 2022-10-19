from random import randint, random
from turtle import *

tortuga = Turtle()
tortuga.speed(speed=0)

pantalla = Screen()
pantallaX = int(input('Introduce el ancho de la pantalla: '))
pantallaY = int(input('Introduce el alto de la pantalla: '))

radPerimetro = int(input("Radio del perímetro: "))
numPasos = int(input("Número máximo de pasos: "))
pasosDados = 0

tortuga.penup()
tortuga.right(90)
tortuga.forward(radPerimetro)
tortuga.pendown()
tortuga.left(90)
tortuga.pencolor("green")
tortuga.circle(radPerimetro)
tortuga.penup()
tortuga.home()
tortuga.pendown()
tortuga.pencolor("blue")

while pasosDados < numPasos:
    pasosDados += 1
    print(pasosDados)
    if abs(tortuga.xcor())<= (pantallaX) and abs(tortuga.ycor()) <= (pantallaY):
        if tortuga.distance(0,0) <= radPerimetro:
            tortuga.forward(20)
            tortuga.left(randint(0, 180))
            tortuga.right(randint(0, 180))
        else:
            print("Fuera de perimetro")
            print(tortuga.pos())
            pantalla.exitonclick()
    else:
        print("Fuera de pantalla")
        print(tortuga.pos())
        pantalla.exitonclick()
else:
    print("Condicion cumplida")
    print(tortuga.pos())
    pantalla.exitonclick()