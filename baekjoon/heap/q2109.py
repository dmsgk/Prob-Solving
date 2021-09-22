# 순회공연

import sys
import heapq

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    req = []
    for _ in range(n):
        p, d = map(int, sys.stdin.readline().split())
        req.append([p, d])

    req.sort(reverse=True, key= lambda x: x[1])  # 역순으로 리스트 정렬
    cnt = 0
    price_heap = []
    prev_day = req[0][1]


    for i in range(len(req)):
        p, d = req[i][0], req[i][1]
        while prev_day > d and price_heap:
            cnt += -heapq.heappop(price_heap)
            prev_day -= 1
        prev_day = d
        heapq.heappush(price_heap, -p)  # 최대힙으로 구성


    while prev_day > 0 and price_heap:
        cnt += -heapq.heappop(price_heap)
        prev_day -= 1

    print(cnt)


