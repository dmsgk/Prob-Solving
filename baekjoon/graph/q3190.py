# 조현 풀이

from collections import deque

n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 1   # 사과 있는 칸을 1로 설정

l = int(input())
relative_d = [list(input().split()) for _ in range(l)]  # 상대적 방향 ('L', 'R')
relative_d = deque(relative_d)

abs_d = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}  # 절대적 방향 (동서남북)

directions = {'N': {'L':'W','D':'E'}, 'S': {'L':'E','D':'W'}, 'W': {'L':'S','D':'N'}, 'E': {'L':'N','D':'S'}}   # 회전 시 절대적 방향 찾기 위한 딕셔너리

#------메인-----------
visited = [[1, 1]]
length = 1  # 뱀의 길이
sec = 1   # 게임 진행 시간

direction = 'E'
x, y = 1,1
curr_x, curr_y = 1,2
while 1:
    i, j = abs_d[direction]
    curr_x, curr_y = x+i, y+j
    if curr_x < 1 or curr_x > n or curr_y < 1 or curr_y > n or [curr_x,curr_y] in visited[-length:]:   # 벽에 부딪히거나 뱀의 몸에 부딪힘
        break
    if board[curr_x][curr_y] == 1:  # 사과가 있을 때
        length += 1
        board[curr_x][curr_y] = 0
    if relative_d:
        s, r = relative_d.popleft()
        if sec == int(s):  # 회전해야 하는 시간일 때
            direction = directions[direction][r]
        else:
            relative_d.appendleft([s,r])  # 다시 집어넣기

    visited.append([curr_x,curr_y])
    sec += 1
    x, y = curr_x, curr_y


print(sec)