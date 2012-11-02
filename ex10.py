# -*- encoding:utf-8 -*-
from time import sleep
import re

a = [1, 11, 21, 1211, 111221, ]
#カッコウはコンピュータに卵を産む
def change(s):
    seq = [_s for _s in s]
    i = 0
    _seq = []
    length = len(seq)
    while 1:
        if i >= length:
            break
        elif i + 1 == length:
            _seq.append('1' + seq[i])
            break
        elif i + 1 < length:
            if seq[i] == seq[i + 1]:
                if i + 2 < length:
                    if seq[i] == seq[i + 2]:
                        _seq.append('3' + seq[i])
                        i += 3
                    else:
                        _seq.append('2' + seq[i])
                        i += 2
                else:
                    _seq.append('2' + seq[i])
                    break
                    
            else:
                _seq.append('1' + seq[i])
                i += 1
    _seq = ''.join(_seq)
    return _seq
    
def main():
    s = '1'
    for i in xrange(30):
        # print len(s), ':', s
        print len(s)
        s = change(s)
    print len(s)
    print 'ans =', len(s)

if __name__ == '__main__':
    main()
