# 사전

import sys
from itertools import product

n, m, k = map(int, sys.stdin.readline().split())

if n+m < k:
    print(-1)
else:
    char_li = ['a'] * n + ['z'] * m
    result = list(product(char_li))
    # cnt = 1
    # org_idx, curr_idx = n-1, n-1
    # empty_idx = m+n-1  # z로 되어있는 마지막 인덱스.
    # while cnt < k:
    #     cnt += 1
    #     char_li[curr_idx], char_li[empty_idx] = char_li[empty_idx], char_li[curr_idx]
    #     empty_idx
    # p = set(permutations(char_li))
    # print(p)
    # p_li = list(map("".join, p))
    # p_li.sort()
    # print(p_li)
    # print(p_li[k-1])
