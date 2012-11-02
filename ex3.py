# -*- encoding:utf-8 -*-

import re

def main():
    txt='text_3.txt'
    lines = file(txt).read()
    text = ''.join(lines)
    pattern = '[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
    regex = re.compile(pattern)
    ans = regex.findall(text)
    print ''.join(ans)

if __name__ == '__main__':
    main()

