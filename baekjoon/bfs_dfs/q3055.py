# 탈출
import sys
from collections import deque

# 입력 부분
r,c = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]


water_queue = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            water_queue.append([i,j])
        elif board[i][j] == 'S':
            hedgehog = [i, j, 0]  # 행, 열, 움직인 횟수 저장하기.


def bfs(board, r, c, hedgehog, water_queue):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    h_queue = deque([hedgehog])
    visited = {(hedgehog[0], hedgehog[1])}  # set 에 행, 열 튜플로 저장.

    temp_board = [[0]*c for _ in range(r)]

    h_temp = deque()
    water_temp = deque()
    while h_queue:
        # 물 먼저 이동
        while water_queue:
            x, y = water_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == '.' or board[nx][ny] == 'S':  # 돌과 비버의 집 불가
                        board[nx][ny] = '*'
                        water_temp.append([nx, ny])

        hx, hy, cnt = h_queue.popleft()
        if board[hx][hy] == 'D':   # 비버네 집에 도착
            return cnt   # 최소 시간 리턴

        for j in range(4):
            nhx, nhy = hx + dx[j], hy + dy[j]
            if 0 <= nhx < r and 0 <= nhy < c and (nhx,nhy) not in visited:
                if board[nhx][nhy] == '.' or board[nhx][nhy] == 'D':
                    h_temp.append([nhx,nhy, cnt + 1])
                    visited.add((nhx,nhy))
                    temp_board[nhx][nhy] = cnt + 1
        if not h_queue and h_temp:
            water_queue = water_temp
            h_queue = h_temp
            water_temp = deque()
            h_temp = deque()

    return "KAKTUS"


print(bfs(board, r, c, hedgehog, water_queue))

"""
3 3
D.*
...
.S.
answer : 3

"""