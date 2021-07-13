# 최단경로
import sys
import heapq

v, e = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())
distance = [sys.maxsize] * (v+1)

roads = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(e)]
graph = [[] for _ in range(v+1)]
for r in roads:
    a,b,w = r
    graph[a].append([b,w])  # 도착 간선, 가중치 저장


def dijkstra(distance, k, visited, graph):
    q = []
    distance[k] = 0
    heapq.heappush(q, (distance[k], k))
    while q:
        dist, curr_node = heapq.heappop(q)
        if visited[curr_node]:  # 방문한 노드인 경우
            continue

        visited[curr_node] = True
        for nextNode in graph[curr_node]:
            if distance[nextNode[0]] > distance[curr_node] + nextNode[1]:
                distance[nextNode[0]] = distance[curr_node] + nextNode[1]
                heapq.heappush(q, (distance[nextNode[0]], nextNode[0]))
    return distance

visited = [False] * (v+1)
distance = dijkstra(distance, k, visited, graph)

for i in range(1,v+1):
    if distance[i] < sys.maxsize:
        print(distance[i])
    else:
        print("INF")


"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

"""