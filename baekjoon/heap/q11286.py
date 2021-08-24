# 절댓값 힙
import sys
import heapq


n = int(sys.stdin.readline())
h = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if not h:
            print(0)
            continue
        abs_num, sign = heapq.heappop(h)
        print(sign * abs_num)
    else:
        if num < 0:
            heapq.heappush(h, [-num, -1])
        else:
            heapq.heappush(h, [num, 1])

