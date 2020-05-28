from PIL import Image
i = Image.open('rabbit.png')

#Write a program to reverse the frames of an animated GIF. The n_frames method on an image returns the number of frames, and the seek(n) method moves to a given one.
#Fixme: output is wrong: not clear Pillow can do this...
i = Image.open('fade.gif')

images = []

for f in range(i.n_frames):
    i.seek(f)
    images.append(i.copy())

images[0].save('reversed.gif', save_all=True, append_images=images[1:], duration=100, loop=0)

