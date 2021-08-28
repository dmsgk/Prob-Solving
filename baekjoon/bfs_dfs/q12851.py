# 숨바꼭질 2
import sys
from collections import deque


def bfs(n, k):
    visited = set()
    fastest = sys.maxsize
    way_cnt = 0
    queue = deque([[n, 0]])

    while queue:
        x, cnt = queue.popleft()
        visited.add(x)

        if x == k:
            if fastest >= cnt:
                way_cnt += 1
                fastest = cnt

            continue

        dx = [-1, 1]
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx <= 100000 and nx not in visited:
                queue.append([nx, cnt + 1])
        nsun = x * 2  # 순간이동
        if 0 <= nsun <= 100000 and nsun not in visited:
            queue.append([nsun, cnt + 1])

    print(fastest)
    print(way_cnt)


n, k = map(int, sys.stdin.readline().split())
bfs(n, k)





