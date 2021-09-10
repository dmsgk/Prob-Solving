# 암호만들기

import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().strip().split())
char_li = list(sys.stdin.readline().strip().split())


cons = []
vowel = []

for char in char_li:
    if char in set("aeiou"):
        vowel.append(char)
    else:
        cons.append(char)


com_li = []

for i in range(1, len(vowel)+1):
    j = l - i   # 자음의 개수
    if j > 1:  # 자음이 2개이상인 경우
       v, c = list(map("".join, combinations(vowel, i))), list(map("".join, combinations(cons, j)))
       for vcomb in v:
           for ccomb in c:
               comb_str_li = sorted(list(vcomb+ccomb))
               com_li.append("".join(comb_str_li))
com_li.sort()
for c in com_li:
    print(c)





