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

def many_stars():
    t.clear()
    for _ in range(20):
        star(random.randint(-300, 300),
             random.randint(-300, 300),
             random.randint(10, 150),
             random.randint(3, 30))

def stars_exit():
    sys.exit(0)

def save_stars():
    turtle.Screen().getcanvas().postscript(file='stars.ps')
    stars_exit()

t = turtle.Turtle()

t.hideturtle()
turtle.Screen().tracer(0, 0)
turtle.Screen().onkey(save_stars, 's')
turtle.Screen().onkey(many_stars, ' ')
turtle.Screen().onkey(stars_exit, 'x')
turtle.listen()

manystars()
turtle.mainloop()
