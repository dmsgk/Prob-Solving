# 테트로미노
import sys
from collections import deque


def bfs(board, start, max_num):
    x,y = start
    queue = deque([ [x,y, board[x][y], 1, {(x,y)}] ])   # x,y, 지금까지 합, 몇번째 블록인지 기록, 현재 탐색하는 블럭이 간 위치
    dx, dy = [1,0,0], [0,-1,1]  # 하, 좌, 우

    while queue:
        x, y, curr_sum, block_num,rest_visited = queue.popleft()
        t_max = t_shape_maxnum(board, x, y)  # ㅗ ㅜ ㅓ ㅏ 최댓값은 함수로 따로 구해주기
        if t_max and t_max > max_num:
            max_num = t_max
        if block_num == 4:
            max_num = max(max_num, curr_sum)
            if queue:  # 테트리미노인 블럭이 아직 큐에 있을 때
                sorted_queue = sorted(queue, key = lambda idx: idx[2])
                max_num = max(max_num, sorted_queue[-1][2])
            break
        for i in range(3):
            nx,ny = x+dx[i], y+dy[i]
            if 0<= nx < n and 0<= ny < m and (nx,ny) and (nx,ny) not in rest_visited: # not in first_visited
                n_rest_visited = rest_visited.union({(nx,ny)})
                queue.append([nx,ny, curr_sum + board[nx][ny], block_num+1, n_rest_visited])
    return max_num


def t_shape_maxnum(board, x,y):
    sum_arr = []
    try:
        block_sum = board[x - 1][y] + board[x][y] + board[x][y - 1] + board[x][y + 1]  # ㅗ 모양
        sum_arr.append(block_sum)
    except IndexError:
        pass
    try:
        block_sum = board[x + 1][y] + board[x][y] + board[x][y - 1] + board[x][y + 1]  # ㅜ 모양
        sum_arr.append(block_sum)
    except IndexError:
        pass
    try:
        block_sum = board[x][y-1] + board[x][y] + board[x+1][y] + board[x-1][y]  # ㅓ 모양
        sum_arr.append(block_sum)
    except IndexError:
        pass
    try:
        block_sum = board[x][y+1] + board[x][y] + board[x+1][y] + board[x-1][y]  # ㅏ 모양
        sum_arr.append(block_sum)
    except IndexError:
        pass
    finally:
        if sum_arr:
            return max(sum_arr)



n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
max_num = 0
for i in range(n):
    for j in range(m):
        max_num = bfs(board, (i, j), max_num)
print(max_num)
"""
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

# 19 출력

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

# 20 출력 

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1

# 7 출력
"""