# 바이러스
import sys
from collections import deque


def bfs(graph, start):
    visited = {}
    q = deque([start])
    cnt = 0

    while q:
        n = q.popleft()
        if n not in visited:
            visited[n] = True
            for i in range(len(graph[n])):
                if graph[n][i] == 1 and i not in visited and i not in q:
                    q.append(i)
                    graph[i][n] = 0
                    graph[n][i] = 0
                    cnt += 1
    return cnt


n = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

graph =[[0] * (n+1) for i in range(n+1)]

for _ in range(c):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

print(bfs(graph, 1))