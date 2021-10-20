# 미세먼지 안녕!

import sys
from collections import deque


def spread_dust(board, r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향
    queue = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                queue.append([i,j])

    cmd = []
    while queue:
        x, y = queue.popleft()
        dir_cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                cmd.append([nx, ny, board[x][y] // 5])
                dir_cnt += 1

        cmd.append([x,y, -(board[x][y]//5) * dir_cnt])
    for a, b, adding in cmd:
        board[a][b] += adding

    return board


def rotation(board, clockwise, r_idx, r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향
    x, y = r_idx, 0
    idx = 0
    prev = 0
    while 1:
        nx, ny = x + dx[idx], y + dy[idx]
        if nx == r_idx and ny == 0:
            break
        if not (0 <= nx < r) or not (0 <= ny < c):
            idx = (idx + clockwise * 1) % 4
            nx, ny = x + dx[idx], y + dy[idx]

        curr = board[nx][ny]
        board[nx][ny] = prev
        prev = curr
        x, y = nx,ny
    return board


def circulate_air(board, r, c, cleaner):
    upper, lower = cleaner
    # 윗 부분은 반시계
    board = rotation(board, -1, upper, r, c)
    # 아랫부분은 시계방향
    board = rotation(board, 1, lower, r, c)
    return board


def solution(board, r, c, t, cleaner):
    for i in range(t):
        # 미세먼지가 확산
        board = spread_dust(board, r, c)
        # 공기청정기 가동
        board = circulate_air(board, r, c, cleaner)

    cnt = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                cnt += board[i][j]
    return cnt


r, c, t = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
cleaner = []  # 공기청정기의 열 위치 저장
for j in range(r):
    if board[j][0] == -1:
        cleaner = [j, j+1]
        break

print(solution(board, r, c, t, cleaner))