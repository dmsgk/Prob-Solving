# 최소비용구하기2
import sys
import heapq


def dijkstra(graph, start, end, n):
    q = []
    dist = [[sys.maxsize, []] for _ in range(n)]
    dist[start-1][0] = 0
    dist[start-1][1].append(start)

    heapq.heappush(q, (0, start-1))
    while q:
        cost, curr = heapq.heappop(q)
        if dist[curr][0] < cost:
            continue
        for nxt, cst in graph[curr]:
            if dist[nxt][0] > dist[curr][0] + cst:
                dist[nxt] = [dist[curr][0] + cst, dist[curr][1] + [nxt+1]]
                heapq.heappush(q, (dist[nxt][0], nxt))

    return dist[end - 1]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s-1].append((e-1, c))

start, end = map(int, sys.stdin.readline().split())
result = dijkstra(graph, start, end, n)
print(result[0])
print(len(result[1]))
print(*result[1])