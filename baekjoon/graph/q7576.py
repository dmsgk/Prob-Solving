import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def bfs(graph, d):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = -1
    while d:
        a = d.popleft()
        cnt += 1
        while a:
            x, y = a.pop()
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    if not d:
                        d.append([[nx, ny]])
                    else:
                        d[-1].append([nx, ny])

    for i in range(n):
        if 0 in graph[i]:
            return -1

    return cnt


d = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            if not d:
                d.append([deque([i,j])])
            else:
                d[0].append([i,j])

print(bfs(graph, d))
