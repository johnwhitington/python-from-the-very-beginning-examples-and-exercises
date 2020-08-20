from PIL import Image
i = Image.open('rabbit.png')

p = i.load()
sx, sy = i.size
for x in range(sx):
    for y in range(sy):
        r, g, b = p[x, y]
        gr = int ((r + g + b) / 3)
        p[x, y] = (gr, gr, gr)

i.save('greyrabbit.png')

def grey(p):
    r, g, b = p
    gr = int((r + g + b) / 3)
    return (gr, gr, gr)

def process_pixels_in_place(f, i):
   p = i.load()
   sx, sy = i.size
   for x in range(sx):
       for y in range(sy):
           p[x, y] = f(p[x, y])

process_pixels_in_place(grey, i)

def border(i, width, colour):
    sx, sy = i.size
    p = i.load()
    i2 = Image.new('RGB', (sx + width * 2, sy + width * 2), colour)
    p2 = i2.load()
    for x in range(sx):
        for y in range(sy):
            p2[x + width, y + width] = p[x, y]
    return i2

bordered = border(i, 20, (150, 150, 150))

bordered.save('rabbit_border.png')

i = Image.open('rabbit.png')

def blur(i):
    p = i.load()
    i2 = i.copy()
    p2 = i2.load()
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
            p2[x, y] = int (sumr / 9), int (sumg / 9), int (sumb / 9)
    return i2

white_bordered = border(i, 20, (255, 255, 255))

x = blur(blur(blur(white_bordered)))

x.save('blurred.png')

def make_images_blur(i, n):
    image = i
    images = [i]
    for x in range(n):
        image = blur(image)
        images.append(image)
    return images

images = make_images_blur(white_bordered, 20)

images[0].save('animation.gif', save_all=True, append_images=images[1:],
               duration=100, loop=0)

def fadeby(f, p):
  r, g, b = p
  r_out = int ((f * r + (100 - f) * 255) / 100)
  g_out = int ((f * g + (100 - f) * 255) / 100)
  b_out = int ((f * b + (100 - f) * 255) / 100)
  return (r_out, g_out, b_out)

def process_pixels(f, i):
    p = i.load()
    i2 = i.copy()
    p2 = i2.load()
    sx, sy = i.size
    for x in range(sx):
        for y in range(sy):
            p2[x, y] = f(p[x, y])
    return i2

def make_images(i):
    images = []
    for x in range(100, -1, -5):
        def fade(p): return fadeby(x, p)
        faded = process_pixels(fade, i)
        images.append(faded)
    return images

images = make_images(i)

images[0].save('fade.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

