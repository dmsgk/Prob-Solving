# 보석도둑
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
gems = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
caps = [int(sys.stdin.readline()) for _ in range(k)]
gems.sort()
caps.sort()

cnt = 0
max_gem = []
for c in caps:
    while gems and c >= gems[0][0]:
        heapq.heappush(max_gem, -gems[0][1])
        heapq.heappop(gems)

    if max_gem:
        cnt += -heapq.heappop(max_gem)
    elif not gems:
        break
print(cnt)

