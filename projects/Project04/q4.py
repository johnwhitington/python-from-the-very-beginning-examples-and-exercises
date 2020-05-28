from PIL import Image
i = Image.open('rabbit.png')

#Question 4
#How wide does the border have to be for any given number of blurring operations? Implement a version which uses only the border required.
def blur_auto(i, n):
    i = border(i, n, (255, 255, 255))
    for x in range(n):
        i = blur(i)
    return i

