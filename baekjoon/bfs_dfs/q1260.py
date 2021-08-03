import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
Map = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    Map[i][j] = 1
    Map[j][i] = 1

def dfs(Map, start):
    visited = []
    stack = [start]

    while stack:
        n= stack.pop()
        if n not in visited:
            visited.append(n)
            for i in range(1, len(Map[n])+1):
                if Map[n][-i] == 1 and len(Map[n])-i not in visited:
                    stack.append(len(Map[n])-i)
    return (' '.join(list(map(str, visited))))


def bfs(Map, start):
    visited = []
    q = deque([start])

    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            for i, v in enumerate(Map[n]):
                if v == 1 and i not in visited:
                    q.append(i)
    return (' '.join(list(map(str, visited))))

print(dfs(Map, v))
print(bfs(Map, v))
