import math

def star(x):
    i = math.floor(x * 50)
    if i == 50: i = 49
    print(' ' * (i - 1) + '*')

def plot(f, a, b, dy):
  pos = a
  while pos <= b:
      star(f(pos))
      pos += dy
