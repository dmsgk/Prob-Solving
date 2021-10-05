# 달팽이
import sys

n = int(sys.stdin.readline())
certain_num = int(sys.stdin.readline())

board = [[0]*n for _ in range(n)]


def solution(n, board, certain_num):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향(동남서북)
    start = n // 2
    direction = 3  # 북쪽부터 올라감
    temp = []
    if certain_num == 1:
        temp = [start+1, start+1]
    if certain_num == 2:
        temp = [start, start+1]
    board[start][start], board[start-1][start] = 1, 2
    x, y = start-1, start
    for i in range(3, n**2 + 1):
        rx, ry = x + dx[(direction+1) % 4], y + dy[(direction+1)%4]  # 우회전한 좌표
        sx, sy = x + dx[direction], y + dy[direction]   # 직진 좌표
        if 0 <= rx < n and 0 <= ry < n and board[rx][ry] == 0:
            board[rx][ry] = i
            x, y = rx, ry
            direction = (direction+1) % 4
        else:
            board[sx][sy] = i
            x, y = sx, sy

        if i == certain_num:
            temp = [x+1, y+1]

    return board, temp


board, temp = solution(n, board, certain_num)
for i in range(n):
    print(*board[i])
print(*temp)

