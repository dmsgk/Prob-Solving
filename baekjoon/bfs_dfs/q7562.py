# 나이트의 이동
import sys
from collections import deque


def bfs(n, x, y, fx, fy):
    board = [[0]*n for _ in range(n)]
    dx, dy = [-2,-1,1,2,2,1,-1,-2], [1,2,2,1,-1,-2,-2,-1]
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        if x == fx and y == fy:
            return board[fx][fy]

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    x, y = map(int, sys.stdin.readline().strip().split())   # 시작지점
    fx, fy = map(int, sys.stdin.readline().strip().split())  # 목표지
    print(bfs(n, x, y, fx, fy))
