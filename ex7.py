# -*- encoding:utf-8 -*-
import Image
import re
import sys

def main():
    filename = 'oxygen.png'
    img = Image.open(filename)
    st = img.getdata()
    contents = filter(lambda row:row[0] == row[1] == row[2], st)
    rows = []
    chrs = ''
    prev =  None
    pattern = '\[([^\[]+)\]'
    pattern = '(\d+,[\s\d+,]+,\s\d+)'
    regex = re.compile(pattern)
    for con in [content[0] for content in contents]:
        if prev != con:
            chrs += chr(con)
        prev = con
    print chrs
    got_item = regex.search(chrs).group(0)
    item = [int(i) for i in got_item.split(', ')]
    print item
    for i in item:
        sys.stdout.write(chr(int(i)))

if __name__ == '__main__':
    main()
