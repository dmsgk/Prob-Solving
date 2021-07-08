# 소수 구하기

import sys
import math

m, n = map(int, sys.stdin.readline().rstrip().split())


def prime_num(m, n):
    num_dict = {i: True for i in range(max(2,m), n + 1)}
    num = math.ceil(math.sqrt(n))  # n의 제곱근보다 크거나 같은 정수까지 탐색할 것
    for i in range(2, num + 1):
        for j in range(i * 2, n + 1, i):
            if j in num_dict:
                del num_dict[j]

    return list(num_dict.keys())

p_li = prime_num(m,n)
for p in p_li:
    print(p)
