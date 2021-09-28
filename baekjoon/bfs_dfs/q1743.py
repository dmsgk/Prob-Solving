# 음식물 피하기

import sys
sys.setrecursionlimit(10**9)

n, m, k = map(int, sys.stdin.readline().split())
board = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = 1


def dfs(board, x, y):
    global total_visited
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    stack = [[x,y]]
    result = 1

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and (nx, ny) not in total_visited:
                total_visited.add((nx,ny))
                stack.append([nx,ny])
                result += 1
    return result


total_visited = set()
result = []


for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and (i,j) not in total_visited:
            total_visited.add((i,j))
            result.append(dfs(board,i,j))


print(max(result))
