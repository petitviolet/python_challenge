# -*- encoding:utf-8 -*-
import urllib
import pickle

def main(url='http://www.pythonchallenge.com/pc/def/banner.p'):
    # url='http://www.pythonchallenge.com/pc/def/peak.html'
    get_file = urllib.urlopen(url).read()
    filename = 'banner.p'
    g = file(filename, 'w')
    g.write(get_file)
    g.close()
    # source = urllib.urlopen(url).read()
    with open(filename, 'r') as f:
        banner = pickle.load(f)
    for y in banner:
        s = ''
        for z in y:
            (c, n) = z
            s += c*n
        print s

if __name__ == '__main__':
    main()
