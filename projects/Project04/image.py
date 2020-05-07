from PIL import Image
i = Image.open('image.png')

#greyscale, brightness, contrast, flip (Qs)
#1. Greyscale and similar effects, by processing pixels in place or from old to new
def grey(p):
    r, g, b = p
    gr = int((r + g + b) / 3)
    return (gr, gr, gr)

def process_pixels(f, i):
    p = i.load()
    i2 = i.copy()
    p2 = i2.load()
    sx, sy = i.size
    for x in range(sx):
        for y in range(sy):
            p2[x, y] = f(p[x, y])
    return i2

gr = process_pixels(grey, i)

def process_pixels_in_place(f, i):
   p = i.load()
   sx, sy = i.size
   for x in range(sx):
       for y in range(sy):
           p[x, y] = f(p[x, y])



#2. make an image from scratch. Use this to do blurring by copying over the original and then processing.
n = Image.new('RGB', (500, 500))

n.save('new.png')

box = [1, 1, 1, 1, 1, 1, 1, 1, 1]

def blur(i):
    p = i.load()
    i2 = i.copy()
    p2 = i.load()
    sx, sy = i.size
    for x in range(3, sx - 3):
        for y in range(3, sy - 3):
            sumr, sumg, sumb = 0, 0, 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    sourcer, sourceg, sourceb = p[x + dx, y + dy]
                    sumr = sumr + sourcer
                    sumg = sumg + sourceg
                    sumb = sumb + sourceb
            p2[x, y] = int (sumr / 9), int (sumg / 9), int (sumb / 9)
    return i2

#FIXME: Decide size / color of border. Make the new image with border.

#gradient, fractals, similar?
#from our turtle graphics?



#Subtitling: adding text on top with PostScript?



#An animated GIF. Reverse existing ones.

