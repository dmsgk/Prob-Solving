# 가운데를 말해요

import sys
import heapq

n = int(sys.stdin.readline().strip())
left, right = [], []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if len(right) == len(left):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        left_val = heapq.heappop(left)[1]
        right_val = heapq.heappop(right)[1]
        heapq.heappush(right, (left_val, left_val))
        heapq.heappush(left, (-right_val, right_val))

    print(left[0][1])




"""
7
1
5
2
10
-99
7
5

"""