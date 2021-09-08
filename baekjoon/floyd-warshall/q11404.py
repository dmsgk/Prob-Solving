# 플로이드

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = 10000001
board = [[] for _ in range(n)]
for i1 in range(n):
    for _ in range(n):
        board[i1].append(INF)


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = min(board[a-1][b-1], c)

for r in range(n):
    board[r][r] = 0


def floyd_warshall(board, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]
    return board


result = floyd_warshall(board, n)

for x in range(n):
    for y in range(n):
        if result[x][y] == INF:
            result[x][y] = 0
    print(*result[x])