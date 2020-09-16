import math

def make_vector(a, b):
    x0, y0 = a
    x1, y1 = b
    return (x1 - x0, y1 - y0)

def vector_length(v):
    x, y = v
    return math.sqrt(x * x + y * y)

def offset_point(pt, off):
    x, y = pt
    px, py = off
    return (px + x, py + y)

def scale_to_length(l, v):
    currentlength = vector_length(v)
    if currentlength == 0.:
        return v
    else:
        factor = l / currentlength
        x, y = v
        return (x * factor, y * factor)
