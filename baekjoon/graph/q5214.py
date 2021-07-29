# 환승
# 메모리초과

import sys
from collections import defaultdict, deque


n, k, m = map(int, sys.stdin.readline().split())
linked_li = defaultdict(set)

for i in range(m):
    stations = set(sys.stdin.readline().split())
    for sta in stations:
        linked_li[sta].update(stations.difference(sta))


def bfs(linked_li, n):
    visited = set()
    queue = deque([['1', 1]])
    while queue:
        q, cnt = queue.popleft()
        if q == str(n):
            return cnt

        if q not in visited:
            visited.add(q)
            for nq in linked_li[q]:
                queue.append([nq, cnt+1])
    return -1


print(bfs(linked_li, n))