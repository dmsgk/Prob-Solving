# 에라토스테네스의 체

import sys

n, k = map(int, sys.stdin.readline().strip().split())

def prime_num(n, k):
    num_dict = {i:True for i in range(2,n+1)}
    cnt = 0
    for i in range(2,n+1):
        if i not in num_dict:
            continue
        for j in range(i, n+1, i):
            if j not in num_dict:
                continue

            cnt += 1
            if cnt == k:
                return j
            del num_dict[j]

print(prime_num(n,k))
