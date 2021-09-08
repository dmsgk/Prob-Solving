# 최소비용구하기

import sys
import heapq


def dijkstra(n, start, end, graph):
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [start, 0])

    while q:
        curr, cost = heapq.heappop(q)
        # 현재 curr까지의 최소거리가 현재 보는 비용보다 작을 때. continue
        if distance[curr] < cost:
            continue

        for nxt, cst in graph[curr]:
            cst += cost
            if cst >= distance[nxt]:
                continue
            distance[nxt] = cst
            heapq.heappush(q, (nxt, cst))

    return distance[end]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])

s_node, e_node = map(int, sys.stdin.readline().split())
print(dijkstra(n, s_node, e_node, graph))

