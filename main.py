from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.shape('turtle')
tim.color('blue')
# tim.colormode(255)

tim.penup()
tim.left(90)
tim.forward(50)
tim.right(90)
tim.pendown()


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


def random_step(turtle):
    turtle.pensize(5)
    turtle.pencolor(get_random_numbers())
    random_angle = (random.randint(1, 4)) * 90
    turtle.right(random_angle)
    turtle.forward(10)


tim.speed('fastest')
for _ in range(200):
    random_step(tim)

# for x in range(3, 7):
#     tim.pencolor(get_random_numbers())
#     angle = 360 / x
#     for _ in range(x):
#         tim.right(angle)
#         tim.forward(100)

screen.exitonclick()
