import turtle
import random
import sys

def star(x, y, l, n):
    t.penup()
    t.goto(x, y)
    t.setheading(random.randint(0, 359))
    t.pendown()
    for _ in range(n):
        t.fd(l)
        t.bk(l)
        t.rt(360.0 / n)

def manystars():
    t.clear()
    for _ in range(20):
        star(random.randint(-300, 300),
             random.randint(-300, 300),
             random.randint(10, 150),
             random.randint(3, 30))

def exit():
    sys.exit(0)

def savestars():
    turtle.Screen().getcanvas().postscript(file='stars.ps')
    exit()

t = turtle.Turtle()
turtle.Screen().tracer(0, 0)
t.hideturtle()

turtle.Screen().onkey(savestars, 's')
turtle.Screen().onkey(manystars, ' ')
turtle.Screen().onkey(exit, 'x')

turtle.listen()
manystars()
turtle.mainloop()

