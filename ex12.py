# -*- encoding:utf-8 -*-
from PIL import Image

filename = 'evil1.jpg'

def main():
    global filename
    img = Image.open(filename)
    _size = tuple([x / 2 for x in img.size])
    n_img = Image.new(img.mode, _size)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            # if x % 2 == 1 and y % 2 == 0:
            if y % 2 in (0, 1):
                p = img.getpixel((x, y))
                n_img.putpixel((x/2, y/2), p)
    n_img.show()

if __name__ == '__main__':
    main()



