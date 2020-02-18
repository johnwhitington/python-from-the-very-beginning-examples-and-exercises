#Question 1
def square(x):
    for _ in range(4):
       t.fd(x)
       t.rt(90)

def many_squares(n, l):
    for _ in range(n):
        square(l)
        t.rt(360.0 / n)

#Question 2
def poly(n, l):
    for _ in range(n):
        t.fd(l)
        t.rt(360.0 / n)

def many_poly(sides, number, side_length):
    for _ in range(number):
        poly(sides, side_length)
        t.rt(360.0 / number)

#Question 3
import math

def circle(r):
    circumference = 2.0 * math.pi * r
    poly(int(circumference), 1.0)

#Question 4
#Grid of circles starting with top-left at (sx, sy), size 50, nx wide, ny tall. 
def grid(sx, sy, nx, ny):
    for x in range(nx):
        for y in range(ny):
            t.penup()
            t.goto(sx + x * 50, sy + y * 50)
            t.pendown()
            t.circle(25)

#Question 5
#We need eleven big squares, one for each 0, 0.1, ... 1.0 in red
#Then each big square has side 11, for green vs blue.
def filled_square(x, y, l):
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.setheading(90)
    for _ in range(4):
        t.fd(l)
        t.rt(90)
    t.end_fill()

def red_gamut(x, y, r):
    for b in range(11):
        for g in range(11):
            t.color(r, g * 0.1, b * 0.1)
            filled_square(x + b * 5, y + g * 5, 5)

def whole_gamut():
    for r in range(11):
        red_gamut(-300 + 55 * r, 0, r * 0.1)

#Question 6
import random

def walk():
    px = 0
    py = 0
    while px > -300 and px < 300 and py > -300 and py < 300:
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        px = px + dx
        py = py + dy
        t.goto(px, py)

#Question 7
import math

def filled_circle(r):
    circumference = 2.0 * math.pi * r
    t.penup()
    t.begin_fill()
    poly(int(circumference), 1.0)
    t.end_fill()

