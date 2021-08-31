# MooTube(Sliver)
import sys
from collections import deque


def bfs(k, vi, graph):
    ans = 0
    queue = deque()
    visited = [0]*(N+1)
    visited[vi] = 1

    for v, w in graph[vi]:
        queue.append((v, w))
        visited[v] = 1

    while queue:
        node, weight = queue.popleft()
        if weight >= k:
            ans += 1

        for n_node, n_weight in graph[node]:
            if visited[n_node] == 0:
                visited[n_node] = 1
                queue.append((n_node, min(weight, n_weight)))
    return ans


N, Q = map(int, sys.stdin.readline().split())
graph = {i: deque() for i in range(1, N+1)}

for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    graph[p].append([q, r])
    graph[q].append([p, r])


for i in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(k, v, graph))

