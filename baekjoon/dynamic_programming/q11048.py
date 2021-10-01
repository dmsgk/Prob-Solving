# 이동하기
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
candy_board = [[0]*m for _ in range(n)]
candy_board[0][0] = board[0][0]


dx, dy = [0, 1, 1], [1, 0, 1]  # 좌, 하, 대각선

for x in range(n):
    for y in range(m):
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and candy_board[nx][ny] < candy_board[x][y] + board[nx][ny]:
                candy_board[nx][ny] = candy_board[x][y] + board[nx][ny]
print(candy_board[n-1][m-1])

