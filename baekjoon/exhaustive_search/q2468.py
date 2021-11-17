# 안전영역
import sys
from copy import deepcopy

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def count_area(h, board):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    temp = deepcopy(board)
    cnt = 0
    stack = []
    for i in range(n):
        for j in range(n):
            if temp[i][j] > h:
                stack.append([i,j])
                temp[i][j] = 0
                cnt += 1
                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and temp[nx][ny] > h:
                            temp[nx][ny] = 0
                            stack.append([nx,ny])
    return cnt


def solution():
    max_h = 0
    for i in range(n):
        for j in range(n):
            max_h = max(board[i][j], max_h)

    max_area = 0
    for h in range(max_h+1):
        max_area = max(max_area, count_area(h, board))
    return max_area


print(solution())