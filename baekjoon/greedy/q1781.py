# 컵라면
import sys
import heapq

n = int(sys.stdin.readline())
prob_heap = []
cnt = 0

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort()

queue = []
for due, ramen in arr:
    heapq.heappush(queue, ramen)
    if due < len(queue):
        heapq.heappop(queue)
print(sum(queue))


