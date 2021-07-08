# 개똥벌레
# range update point query 방법
import sys
from collections import Counter

n, h = map(int, sys.stdin.readline().split())
rock = [int(sys.stdin.readline().strip()) for _ in range(n)]


acc_h = [0]*h   # 누적합 구하기
for i, r in enumerate(rock):
    if i % 2 == 0:
        acc_h[0] += 1
        acc_h[r] -= 1
    else:
        acc_h[h - r] += 1


acc_sum = [0]*h
for i in range(h):
    if i == 0:
        acc_sum[0] = acc_h[0]
    else:
        acc_sum[i] = acc_sum[i-1] + acc_h[i]

sorted_sum = sorted(acc_sum)
min_obstacle = sorted_sum[0]

counter_dict = dict(Counter(acc_sum).most_common())
print(min_obstacle, counter_dict[min_obstacle])