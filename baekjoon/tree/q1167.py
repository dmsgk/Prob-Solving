# 트리의 지름

import sys
from collections import deque

input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visited = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visited[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visited[e] == -1:
                visited[e] = visited[t] + w
                que.append(e)
                if _max[0] < visited[e]:
                    _max = visited[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)