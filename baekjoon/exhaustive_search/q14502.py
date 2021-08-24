# 연구소
import sys
import copy
from itertools import combinations
from collections import deque

sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = []

zero = []
virus = []
wall = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            zero.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])
        else:
            wall += 1


def count_safe_area(board, virus, wall):
    global ans
    result = n*m - (wall+3) - (len(virus))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                result -= 1
                board[nx][ny] = 2
                queue.append([nx,ny])

    # print("연산 끝난 후")
    # print(*board, sep='\n')
    # print(result)
    # print()
    ans.append(result)


zero_comb = list(combinations(zero, 3))

for com in zero_comb:
    # print("comb", com)
    new_board = copy.deepcopy(board)
    for c in com:
        x, y = c
        new_board[x][y] = 1
    # print(*new_board, sep = '\n')
    count_safe_area(new_board, virus, wall)


print(max(ans))

