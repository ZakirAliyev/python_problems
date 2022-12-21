import turtle
import random

turtle.bgcolor("lightblue")
turtle.speed(0)
turtle.hideturtle()


def triangle_maker(i, j):
    lst = ["red", "green", "orange", "yellow", "pink", "brown", "green"]
    turtle.color("black")
    turtle.fillcolor(lst[random.randint(0, 6)])

    turtle.begin_fill()
    for iter in range(3):
        turtle.forward(i)
        turtle.left(j)
    turtle.end_fill()


def tents():
    for i in range(1):
        triangle_maker(random.randint(65, 125), 120)


for i in range(6):
    turtle.penup()
    turtle.setpos(random.randint(-300, 300), random.randint(-20, 0))
    turtle.pendown()
    tents()

turtle.exitonclick()