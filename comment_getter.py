# -*- encoding:utf-8 -*-
import urllib
from BeautifulSoup import BeautifulSoup as bs
import re
import sys


def filegetter(url):
    if url is None:
        return 'please input URL'
    f_name = url.split('/')[-1]
    _filename = f_name.split('.')
    filename = _filename[0] + '.txt'
    line = urllib.urlopen(url).read()
    # pattern = '<!([-.\w\s<]*)>'
    pattern = '<![<\-\s]+([\s\S>]*)[\s\-]+>'
    regex = re.compile(pattern)
    line = regex.findall(line)
    if line == []:
        print 'not found'
        return None
    o = file(filename, 'w')
    count = 1
    for l in line:
        o.write('%d : %s\n' % (count, l) ) 
        count += 1
    o.close()
    f = file(filename).readlines()
    print 'cat %s' % filename
    for _f in f:
        print _f,


def main():
    try:
        url = sys.argv[1]
    except:
        print  'please input URL'
        return None
    filegetter(url)

if __name__ == '__main__':
    main()
