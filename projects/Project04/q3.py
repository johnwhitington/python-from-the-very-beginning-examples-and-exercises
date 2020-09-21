from PIL import Image
i = Image.open('rabbit.png')

#Question 3
def border(i, width, colour):
    sx, sy = i.size
    p = i.load()
    i2 = Image.new('RGB', (sx + width * 2, sy + width * 2), colour)
    p2 = i2.load()
    for x in range(sx):
        for y in range(sy):
            p2[x + width, y + width] = p[x, y]
    return i2

def blur_in_place(i):
    p = i.load()
    sx, sy = i.size
    for x in range(1, sx - 1):
        for y in range(1, sy - 1):
            sumr, sumg, sumb = 0, 0, 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    sourcer, sourceg, sourceb = p[x + dx, y + dy]
                    sumr = sumr + sourcer
                    sumg = sumg + sourceg
                    sumb = sumb + sourceb
            p[x, y] = (int(sumr / 9), int(sumg / 9),int (sumb / 9))

white_bordered = border(i, 20, (255, 255, 255))

for x in range(3): blur_in_place(white_bordered)

white_bordered.save('blurredinplace.png')
