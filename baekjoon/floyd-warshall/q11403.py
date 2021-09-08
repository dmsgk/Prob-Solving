# 경로 찾기

import sys
from copy import deepcopy

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def floyd_warshall(board, n):
    result = deepcopy(board)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if result[i][j] == 1:
                    continue
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1
    return result


result = floyd_warshall(board, n)
for i in range(n):
    print(*result[i])
