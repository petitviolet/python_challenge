# -*- encoding:utf-8 -*-
import urllib2
import re

def geturl(url='http://www.pythonchallenge.com/pc/def/linkedlist.php'):
    num = 12345
    pattern = 'html'
    regex = re.compile(pattern)
    print 'it takes long time... please wait'
    while 1:
        path = 'nothing=' + str(num)
        source = urllib2.urlopen('%s?%s' % (url, path))
        next = source.read()
        num = next.split(' ')[-1]
        check = regex.findall(next)
        if check != []:
            break
    print 'ans =', next

if __name__ == '__main__':
    geturl()
