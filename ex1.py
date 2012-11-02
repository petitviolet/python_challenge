# -*- encoding:utf-8 -*-
import string
import sys

def change(c):
    stopword = ['"', "'", '(', ')', '*', '+', ' ']
    if c in stopword:
        return c
    elif c == '.':
        return '.\n'
    elif c == 'y':
        return 'a'
    elif c == 'z':
        return 'b'
    else:
        num = ord(c)
        return chr(num+2)

def _main():
        text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
        pattern = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
        _text = 'http://www.pythonchallenge.com/pc/def/map.html'
        print text.translate(pattern)
        print _text.translate(pattern)

def main():
    try:
        text = sys.argv[1]
    except:
        text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    out = []
    for t in text:
        print change(t),
        out.append(change(t))
    print ''
    print ''.join(out)

if __name__ == '__main__':
    _main()
