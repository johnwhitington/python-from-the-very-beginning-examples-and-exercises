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
def grid(sx, sy, nx, ny)


#Question 5
gamut of colours

#Question 6
random walk

#Question 7
#filled circle x2


