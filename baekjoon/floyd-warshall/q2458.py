# 키순서

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 작은 쪽을 -1, 큰 쪽을 1로 초기화
    graph[a-1][b-1] = -1
    graph[b-1][a-1] = 1


def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    continue
                if graph[i][k] == graph[k][j]:
                    graph[i][j] = graph[i][k]
    return graph


result = floyd_warshall(graph, n)
cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] == 0:
            break
    else:
        cnt += 1

print(cnt)