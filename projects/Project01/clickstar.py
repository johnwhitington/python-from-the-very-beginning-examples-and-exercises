import turtle
import random

def star(x, y, l, n):
    t.penup()
    t.goto(x, y)
    t.setheading(random.randint(0, 359))
    t.pendown()
    for _ in range(n):
        t.fd(l)
        t.bk(l)
        t.rt(360.0 / n)

def drawstar(x, y):
    star(x, y, random.randint(10, 150), random.randint(3, 30))

t = turtle.Turtle()
turtle.Screen().tracer(0, 0)
t.hideturtle()
turtle.listen()
turtle.Screen().onscreenclick(drawstar)
turtle.mainloop()
