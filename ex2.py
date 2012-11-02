# -*- encoding:utf-8 -*-
from itertools import permutations

def count(text):
    words = {}
    for t in text:
        words.setdefault(t, 0)
        words[t] += 1
    return words

def main():
    lines = file('text_2.txt').read()
    words = count(lines)
    ans = []
    for k, v in words.items():
        if v == 1:
            ans.append(k)
    for p in permutations(ans):
        # print ''.join(p)
        if ''.join(p) == 'equality':
            print 'answer is "', ''.join(p), '"'

if __name__ == '__main__':
    main()
