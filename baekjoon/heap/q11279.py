# 최대 힙

import sys
import heapq

n = int(sys.stdin.readline().strip())
queue = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not queue:
            print(0)
        else:
            print(-heapq.heappop(queue))
    else:
        heapq.heappush(queue, -x)