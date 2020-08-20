from PIL import Image
i = Image.open('rabbit.png')

#Question 2
def hflip(i):
    p = i.load()
    sx, sy = i.size
    for x in range(sx // 2):
        for y in range(sy):
           r = p[x, y]
           p[x, y] = p[sx - x - 1, y]
           p[sx - x - 1, y] = r

def vflip(i):
    p = i.load()
    sx, sy = i.size
    for y in range(sy // 2):
        for x in range(sx):
           r = p[x, y]
           p[x, y] = p[x, sy - y - 1]
           p[x, sy - y - 1] = r

def rotate180(i):
    hflip(i)
    vflip(i)

rotate180(i)

i.save('rotated.png')

