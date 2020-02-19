import sys
import turtle
import math

t = turtle.Turtle()

if len(sys.argv) < 2:
    print('No formula supplied')
    sys.exit(0)

def plot(f):
    t.penup()
    t.goto(-300, f(-300))
    t.pendown()
    for x in range(-300, 300, 1):
        t.goto(x, f(x))

def farg(arg):
    def f(x):
      return(eval(arg))
    return f

def key(n, formula_text, color):
    t.color(color)
    t.penup()
    t.goto(-300, -200 - 20 * n)
    t.pendown()
    t.write(formula_text, font = ("Arial", 16, "normal"))

def line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

def axes():
    t.color("black")
    line(-300, 0, 300, 0)
    line(0, -300, 0, 300)
    for x in range(-300, 301, 50):
        if x != 0:
            t.penup()
            t.goto(x, -20)
            t.pendown()
            t.write(str(x), font = ("Arial", 12, "normal"))
            line(x, -5, x, 5)
    for y in range(-300, 301, 50):
        if y != 0:
            t.penup()
            t.goto(-20, y)
            t.pendown()
            t.write(str(y), font = ("Arial", 12, "normal"))
            line(-5, y, 5, y)

colors = ["black", "red", "green", "blue"]

t.speed(0)

axes()

for n, arg in enumerate(sys.argv[1:]):
    t.pencolor(colors[n % 4])
    plot(farg(arg))
    key(n, arg, colors[n % 4])

turtle.mainloop()

