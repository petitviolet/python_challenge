# -*- encoding:utf-8 -*-
from PIL import Image

def main():
    filename = 'cave.jpg'
    img = Image.open(filename)
    _size = tuple([x / 2 for x in img.size])
    new_img = Image.new(img.mode, _size)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if x % 2 == 0 and y % 2 == 0:
                p = img.getpixel((x, y))
                new_img.putpixel((x/2, y/2), p)
    new_img.save('11.jpg')
    new_img.show()

if __name__ == '__main__':
    main()
