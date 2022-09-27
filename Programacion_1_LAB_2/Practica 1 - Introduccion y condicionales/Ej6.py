from turtle import *

screen = Screen()
screen.setup(800, 600)

tortuga = Turtle()
tortuga.goto (90,0)
tortuga.write(tortuga.position())
tortuga.goto (90,90)
tortuga.write(tortuga.position())
tortuga.goto (0,90)
tortuga.write(tortuga.position())
tortuga.goto (0,0)
tortuga.write(tortuga.position())

screen.exitonclick()