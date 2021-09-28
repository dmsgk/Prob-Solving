# A -> B
import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())


def bfs(a, b):
    queue = deque([[a, [a]]])
    while queue:
        x, visited = queue.popleft()
        if x == b:
            return len(visited)

        if 2*x <= b and 2*x not in visited:
            queue.append([2*x, visited + [2*x]])
        if int(str(x)+'1') <= b and int(str(x)+'1') not in visited:
            queue.append([int(str(x)+'1'), visited + [int(str(x)+'1')]])
    return -1


print(bfs(a,b))