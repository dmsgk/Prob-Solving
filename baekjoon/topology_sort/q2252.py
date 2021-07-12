# 줄세우기
import sys
from collections import deque, defaultdict


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(set)
indegree = {i : 0 for i in range(1, n+1)}
queue = deque()
ans = []


for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].add(b)
    indegree[b] += 1

for k, v in indegree.items():
    if v == 0:
        queue.append(k)



while queue:
    q = queue.popleft()
    ans.append(q)
    for c in graph[q]:
        indegree[c] -= 1
        if indegree[c] == 0:
            queue.append(c)
    del graph[q]

print(" ".join(map(str, ans)))

"""
4 3
4 3
4 2
2 1


"""