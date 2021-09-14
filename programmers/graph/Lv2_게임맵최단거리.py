from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([[(0, 0), 1]])
    visited = {(0, 0)}
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        curr_tup, cnt = queue.popleft()
        x, y = curr_tup
        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append([(nx, ny), cnt + 1])
                visited.add((nx,ny))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))