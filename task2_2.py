import turtle
from math import sqrt


def curve(t, order, size):
    if order == 0:
        return

    position = t.position()
    heading = t.heading()

    t.left(45)
    t.forward(size)
    curve(t, order - 1, size * sqrt(0.5))

    t.up()
    t.setposition(position)
    t.setheading(heading)
    t.right(45)
    t.down()
    t.forward(size)

    curve(t, order - 1, size * sqrt(0.5))

    t.up()
    t.setposition(position)
    t.setheading(heading)
    t.down()


def draw_tree(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    t.left(90)
    t.forward(size)
    curve(t, order, size * sqrt(0.5))

    window.mainloop()

# Виклик функції
draw_tree(7)
