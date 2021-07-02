import heapq
import sys


def dijkstra(start, road, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (distance[start], start))  # 거리, 노드를 q에 저장
    while q:
        dist, curr_node = heapq.heappop(q)
        if distance[curr_node] < dist:
            continue

        for r in road:
            a, b, c = r   # a, b는 도로가 연결하는 두 마을의 번호이며, c는 도로를 지나는데 걸리는 시간
            if a == curr_node:
                if distance[b] > dist + c:
                    distance[b] = dist + c
                    heapq.heappush(q, (distance[b], b))

            elif b == curr_node:  # 경로에 겹치는 경우
                if distance[a] > dist + c:
                    distance[a] = dist + c
                    heapq.heappush(q, (distance[a], a))

    return distance


def solution(N, road, K):
    answer = 0
    distance = [sys.maxsize]*(N+1)
    start = 1
    dijkstra(start, road, distance)

    for x in distance:
        if x <= K:
            answer += 1
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))