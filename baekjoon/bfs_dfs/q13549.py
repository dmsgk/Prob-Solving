# 숨바꼭질 3
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())


def bfs(n, k):
    queue = deque([[n, 0]])
    visited = {n}

    while queue:
        curr_loc, cnt = queue.popleft()
        if curr_loc == k:
            return cnt

        if 100000 >= curr_loc*2 and curr_loc*2 not in visited:
            visited.add(curr_loc*2)
            queue.append([curr_loc*2, cnt])

        if 0 <= curr_loc-1 and curr_loc-1 not in visited:
            visited.add(curr_loc-1)
            queue.append([curr_loc-1, cnt + 1])
        if 100000 >= curr_loc+1 and curr_loc+1 not in visited:
            visited.add(curr_loc+1)
            queue.append([curr_loc+1, cnt + 1])



print(bfs(n,k))