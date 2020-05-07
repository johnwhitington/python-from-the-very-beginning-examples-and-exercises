from PIL import Image
i = Image.open('image.png')
p = i.load()

#modify an image in place, and show and re-save
#greyscale, brightness, contrast, flip, instagram type effect


#New image from old
#rotate, blur, resize, crop
def grey(p):
    r, g, b = p
    gr = int((r + g + b) / 3)
    return (gr, gr, gr)

i2 = i.copy()
p2 = i2.load()

sx, sy = i2.size

for x in range(sx):
    for y in range(sy):
        p2[x, y] = grey(p[x, y])



#make an image from scratch
#gradient, fractals, similar?
#from our turtle graphics?

#Subtitling: adding text on top with PostScript

#An animated GIF. Reverse existing ones.

