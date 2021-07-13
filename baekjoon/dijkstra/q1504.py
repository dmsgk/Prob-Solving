# 특정한 최단경로

import sys
import heapq

n, e = map(int, sys.stdin.readline().rstrip().split())
node_dict = {i: set() for i in range(1, n+1)}

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    node_dict[a].add((b,c))
    node_dict[b].add((a,c))

v1, v2 = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(a, b):
    global node_dict
    queue = [a]
    dist = [sys.maxsize] * (n+1)
    dist[a] = 0
    while queue:
        curr_node = heapq.heappop(queue)
        for nxt in node_dict[curr_node]:
            next_node, cost = nxt
            if dist[next_node] > dist[curr_node]+cost:
                dist[next_node] = dist[curr_node] + cost
                heapq.heappush(queue, next_node)
    if dist[b] == sys.maxsize:
        return -1
    else:
        return dist[b]


ans = []
path_li = [[1,v1,v2, n], [1, v2, v1, n]]

for row in path_li:
    result = 0
    for i in range(3):
        path = dijkstra(row[i], row[i+1])
        if path < 0:
            break
        result += path
    else:
        ans.append(result)

if not ans:
    print(-1)
else:
    print(min(ans))




"""
1 -> v1 -> v2 -> n 인 최단경로
1 -> v2 -> v1 -> n 인 최단경로
둘 다 없으면 -1 return

"""