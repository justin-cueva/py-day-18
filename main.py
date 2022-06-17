from turtle import Turtle, Screen
import random


def get_random_numbers():
    r = 0
    g = 0
    b = 0
    for _ in range(3):
        if _ == 1:
            r = random.randint(1, 255)
        if _ == 2:
            g = random.randint(1, 255)
        if _ == 3:
            b = random.randint(1, 255)
    return r, g, b


tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.shape('turtle')
tim.color('blue')
# tim.colormode(255)

tim.penup()
tim.left(90)
tim.forward(250)
tim.right(90)
tim.pendown()

for x in range(3, 7):
    tim.pencolor(get_random_numbers())
    angle = 360 / x
    for _ in range(x):
        tim.right(angle)
        tim.forward(100)

screen.exitonclick()
