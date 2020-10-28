import math

#1
def round(x):
    c = math.ceil(x)
    f = math.floor(x)
    if c - x <= x - f:
        return c
    else:
        return f

#2
def between(a, b):
    x0, y0 = a
    x1, y1 = b
    return ((x0 + x1) / 2, (y0 + y1) / 2)

#3
def parts(x):
    if x < 0:
        a, b = parts(-x)
        return (-a, b)
    else:
        return (math.floor(x), x - math.floor(x))

#4
def star(x):
    i = math.floor(x * 50)
    if i == 50: i = 49
    print(' ' * (i - 1) + '*')


#5
def plot(f, a, b, dy):
    pos = a
    while pos <= b:
        star(f(pos))
        pos += dy
