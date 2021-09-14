import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c = a+b
heapq.heapify(c)
while c:
    if len(c) == 1:
        print(heapq.heappop(c))
    else:
        print(heapq.heappop(c), end = ' ')
