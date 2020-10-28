#Live clock
import turtle
import time

def hand(length, thickness, angle):
    t.penup()
    t.home()
    t.setheading(90)
    t.pensize(thickness)
    t.pendown()
    t.rt(angle)
    t.fd(length)

def tickmarks():
    t.pensize(1)
    for a in range (0, 60):
        t.penup()
        t.home()
        t.setheading(90)
        t.rt(360 / 60 * a)
        t.fd(295)
        t.pendown()
        t.fd(5)

def clockface(h, m, s):
    t.penup()
    t.goto(0, -300)
    t.pensize(1)
    t.pendown()
    t.circle(300)
    tickmarks()
    hand(200, 3, 360 / 12 * (h % 12))
    hand(280, 3, 360 / 60 * m)
    hand(295, 1, 360 / 60 * s)

t = turtle.Turtle()
t.hideturtle()
turtle.Screen().tracer(0, 0)

while True:
    tm = time.localtime()
    t.home()
    t.clear()
    clockface(tm.tm_hour, tm.tm_min, tm.tm_sec)
    turtle.Screen().update()
    time.sleep(1)
