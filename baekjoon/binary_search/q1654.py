# 랜선자르기

import sys

k, n = map(int, sys.stdin.readline().strip().split())
lan = [int(sys.stdin.readline().strip()) for _ in range(k)]

left, right = 1, max(lan)

while left <= right:
    mid = (left+right)//2
    num_of_lines = 0
    for l in lan:
        num_of_lines += l//mid

    if num_of_lines >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)