from turtle import *

pantalla = Screen()
pantalla.setup(2000,2000)
tortuga = Turtle()

numPeldanos = int (input("Numero de peldaños: "))
longPeldanos = int (input("Longitud del peldaño: "))

tortuga.right(180)
tortuga.forward(longPeldanos * numPeldanos)
tortuga.right(90)
tortuga.forward(longPeldanos * numPeldanos)
tortuga.right(90)

for x in range(numPeldanos):
    tortuga.forward(longPeldanos)
    tortuga.right(90)
    tortuga.forward(longPeldanos)
    tortuga.left(90)

pantalla.exitonclick()