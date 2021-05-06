from collections import deque
import collections


def solution(n, edge):
    adj_list = {i:set() for i in range(1, n+1)}
    for v in edge:
        i,j = v
        adj_list[i].add(j)
        adj_list[j].add(i)

    visited = {i: 0 for i in range(1, n+1)}
    queue = deque([1])
    while queue:
        visited[1] = 0
        q = queue.popleft()
        for j in adj_list[q]:
            if visited[j] == 0:
                queue.append(j)
                visited[j] = visited[q]+1
    v = list(visited.values())
    c = dict(collections.Counter(v))
    return c[max(c)]


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3 출력