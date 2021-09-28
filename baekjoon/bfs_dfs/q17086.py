# 아기상어2
# pypy로만 통과됨
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def bfs(i,j, board):
    visited = {(i,j)}
    queue = deque([[i,j, 0]])

    dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]

    while queue:
        x, y, cnt = queue.popleft()
        if board[x][y] == 1:
            return cnt

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append([nx,ny, cnt+1])



result = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result.append(bfs(i, j, board))

print(max(result))