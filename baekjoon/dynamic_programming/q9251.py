# LCS
import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

board = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            board[i][j] = board[i - 1][j - 1] + 1
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])


print(board[-1][-1])