from PIL import Image
i = Image.open('rabbit.png')

#1. Greyscale and similar effects, by processing pixels in place or from old to new

p = i.load()
sx, sy = i.size
for x in range(sx):
    for y in range(sy):
        r, g, b = p[x, y]
        gr = int ((r + g + b) / 3)
        p[x, y] = (gr, gr, gr)

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

gr.save('greyrabbit.png')

#Qs: VFlip, HFlip, Rotate, Brightness, Contrast.

#2. make an image from scratch. Use this to do blurring by copying over the original and then processing.
n = Image.new('RGB', (500, 500))


n.save('new.png')

#3. A function to add a coloured border to an image
def border(i, width, colour):
    sx, sy = i.size
    p = i.load()
    i2 = Image.new('RGB', (sx + width * 2, sy + width * 2), colour)
    p2 = i2.load()
    for x in range(sx):
        for y in range(sy):
            p2[x + width, y + width] = p[x, y]
    return i2

#4. Use this to make the blur correct.
i = Image.open('rabbit.png')

def blur(i):
    p = i.load()
    i2 = i.copy()
    p2 = i2.load()
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

bordered = border(i, 20, (120, 120, 120))

bordered.save('rabbit_border.png')

white_bordered = border(i, 20, (255, 255, 255))

x = blur(blur(blur(white_bordered)))

x.save('blurred.png')


#Q: Animated blur out
def make_images_blur(i, n):
    image = i
    images = [i]
    for x in range(n):
        image = blur(image)
        images.append(image)
    return images

#images = make_images_blur(bordered, 20)

#images[0].save('animation.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

#5. Animated fade out
def fadeby(f, p):
  r, g, b = p
  r_out = int ((f * r + (100 - f) * 255) / 100)
  g_out = int ((f * g + (100 - f) * 255) / 100)
  b_out = int ((f * b + (100 - f) * 255) / 100)
  return (r_out, g_out, b_out)

def make_images(i):
    images = []
    for x in range(100, -1, -5):
        print(x)
        def fade(p): return fadeby(x, p)
        faded = process_pixels(fade, i)
        images.append(faded)
    return images

images = make_images(i)

images[0].save('fade.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

#for n, x in enumerate(images):
#    x.save(f'fade{n}.gif')

#Q: Animated blur out
def make_images_blur(i, n):
    image = i
    images = [i]
    for x in range(n):
        image = blur(image)
        images.append(image)
    return images

#images = make_images_blur(bordered, 20)

#images[0].save('animation.gif', save_all=True, append_images=images[1:], duration=100, loop=0)


#Question 1
#Write functions to increase or decrease the brightness and contrast of an image. Brightness may be achieved by simple addition of each component of each pixel by an appropriate factor, and contrast by multiplication.

#Question 2
#Write functions to flip an image vertically or horizontally, and to rotate an image by 180°, all in-place.
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

#Question 3
#Rewrite the blurring to work in-place. Is the result appreciably different? How many times do you have to blur for the image?
def blur_in_place(i):
    p = i.load()
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
            p[x, y] = int (sumr / 9), int (sumg / 9), int (sumb / 9)

white_bordered = border(i, 20, (255, 255, 255))

for x in range(3): blur_in_place(white_bordered)

white_bordered.save('blurredinplace.png')


#Question 4
#How wide does the border have to be for any given number of blurring operations? Implement a version which uses only the border required.

#Question 5
#Write a program to reverse the frames of an animated GIF. The n_frames method on an image returns the number of frames, and the seek(n) method moves to a given one.

#Question 6
#Produce a GIF of the rabbit, or your picture, being blurred repeatedly until it is no longer visible (the rounding in the integer arithmetic will ensure it disappears eventually.)
i = border(Image.open('rabbit.png'), 3, (255, 255, 255))
 
images = [i]

for x in range(100):
    print(x)
    i = blur(i)
    images.append(i)

images[0].save('blur.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
