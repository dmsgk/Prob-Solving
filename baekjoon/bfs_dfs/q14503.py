# 로봇청소기 

import sys

n, m = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

cleaned_block = 0
def block_search(board, cleaned_block, d, start):
    dx, dy = [-1,0,1,0], [0,-1,0,1]   # 북서남동(반시계방향)
    x, y = start
    if board[x][y] == 0:
        cleaned_block += 1
        board[x][y] = -1
    idx = (4-d) % 4  # 로봇이 바라보는 방향의 dx,dy 인덱스
    for i in range(1, 5):
        j = (idx + i) % 4
        nx, ny = x + dx[j], y + dy[j]
        if board[nx][ny] == 0:
            return block_search(board, cleaned_block, (4-j) % 4, [nx,ny])

        elif i == 4 and board[nx][ny] != 0:
            new_idx = (idx+2) % 4  # 바라보는 방향에서 후진한 dx, dy 인덱스
            nx,ny = x+dx[new_idx], y+dy[new_idx]
            if board[nx][ny] != 1:
                return block_search(board, cleaned_block, d, [nx, ny])
            else:
                return cleaned_block


print(block_search(board, 0, d, [r,c]))


