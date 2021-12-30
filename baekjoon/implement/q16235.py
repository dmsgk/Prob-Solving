# 나무 재테크
import sys
from collections import deque


def solution(n, k, board):
    for _ in range(k):
        board = update_year(board, nut_arr)

    result = 0
    for x in range(n):
        for y in range(n):
            result += len(board[x][y][1])

    return result


def update_year(board, nut_arr):  # 각 해마다 바뀌는 상태를 출력.
    dx, dy = [-1,1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1,-1,1]
    # 봄, 여름
    for x in range(n):
        for y in range(n):
            nut = board[x][y][0]
            summer_nut = 0
            summer_tree = deque()
            while board[x][y][1]:
                tree = board[x][y][1].popleft()
                if nut >= tree:
                    nut -= tree
                    summer_tree.append(tree+1)
                else:
                    summer_nut += tree//2
            board[x][y][0] = nut + summer_nut + nut_arr[x][y]
            board[x][y][1] = summer_tree
    # 가을
    for a in range(n):
        for b in range(n):
            for t_age in board[a][b][1]:
                if t_age % 5 != 0:
                    continue
                for idx in range(8):
                    na, nb = a + dx[idx], b + dy[idx]
                    if 0 <= na < n and 0 <= nb < n:
                        board[na][nb][1].appendleft(1)
    return board


# 입력
n, m, k = map(int, sys.stdin.readline().split())
nut_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

board = []
for r in range(n):
    arr = []
    for c in range(n):
        arr.append([5, []])
    board.append(arr)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    board[x-1][y-1][1].append(z)

for r in range(n):
    for c in range(n):
        board[r][c][1].sort()
        board[r][c][1] = deque(board[r][c][1])

print(solution(n,k,board))