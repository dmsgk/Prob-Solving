# 숨바꼭질 4

import sys
from collections import deque


def solution(n, k):
    if n > k:
        print(n-k)
        print(*[i for i in range(n, k-1, -1)])
        return

    visited = [False] * 100001
    queue = deque([[n]])
    visited[n] = True
    while queue:
        q_arr = queue.popleft()

        curr_loc = q_arr[-1]
        if curr_loc == k:
            print(len(q_arr)-1)
            print(*q_arr)
            return

        if 0 <= (curr_loc - 1) and not visited[curr_loc-1]:
            queue.append(q_arr + [curr_loc-1])
            visited[curr_loc - 1] = True
        if (curr_loc + 1) <= 100000 and not visited[curr_loc+1]:
            queue.append(q_arr + [curr_loc + 1])
            visited[curr_loc + 1] = True

        if (curr_loc * 2) <= 100000 and not visited[curr_loc*2]:
            queue.append(q_arr + [curr_loc*2])
            visited[curr_loc*2] = True


n, k = map(int, sys.stdin.readline().split())
solution(n, k)