# 감시
import sys

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
cctv = []
wall = 0

for i in range(n):
    for j in range(m):
        if 0< board[i][j] < 6:
            cctv.append([board[i][j], i, j])    # cctv에 [cctv종류, 행, 열] 형태로 저장
        elif board[i][j] == 6:
            wall += 1    # 벽은 총 몇 개인지 개수만 저장


def add_temp_set(board, temp, idx, nx, ny):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북동남서
    while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
        temp.add((nx, ny))
        nx += dx[idx]
        ny += dy[idx]
    return temp


def update_visited(visited, partial_visited, idx, temp):
    if idx == 0:
        partial_visited.append(temp)
    else:
        for v in visited:
            partial_visited.append(temp.union(v))
    return partial_visited


def find_blindspot(board, cctv):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북동남서
    visited = []
    if not cctv:
        return 0
    for idx, cam in enumerate(cctv):
        cam_num, x, y = cam
        partial_visited = []

        if cam_num == 1:
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                temp = {(x,y)}
                temp = add_temp_set(board, temp, i, nx, ny)
                partial_visited = update_visited(visited, partial_visited, idx, temp)

        elif cam_num == 2:
            for i in range(2):  # 0,1 두 가지 경우 (0,2 // 1,3 두가지 구현)

                temp = {(x, y)}
                for j in range(2):
                    nx, ny = x+dx[i+2*j], y+dy[i+2*j]
                    temp = add_temp_set(board, temp, i + 2 * j, nx, ny)
                partial_visited = update_visited(visited, partial_visited, idx, temp)

        elif cam_num == 3:
            for i in range(4):  # 4가 경우 ((0,1 // 2,3 두가지 구현)
                temp = {(x, y)}
                for j in range(2):
                    nx, ny = x+dx[(i+j)%4], y+dy[(i+j)%4]
                    temp = add_temp_set(board, temp, (i+j) % 4, nx, ny)
                partial_visited = update_visited(visited, partial_visited, idx, temp)

        elif cam_num == 4:
            for i in range(4):
                temp = {(x, y)}
                for j in range(4):
                    if j == i:
                        continue
                    nx, ny = x+dx[j], y+dy[j]
                    temp = add_temp_set(board, temp, j, nx, ny)
                partial_visited = update_visited(visited, partial_visited, idx, temp)

        else:
            temp = {(x, y)}
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                temp = add_temp_set(board, temp, i, nx, ny)
            partial_visited = update_visited(visited, partial_visited, idx, temp)

        visited = partial_visited
        # -------
    ans = []
    for v in visited:
        ans.append(len(v))

    return max(ans)


print(n*m - find_blindspot(board, cctv) - wall)




"""
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0

20 출력 


6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5

15출력 


7 5
6 0 0 0 6
0 4 1 6 6
6 0 6 0 6
0 6 0 3 6
0 6 0 1 6
6 6 0 5 6
6 6 6 5 6
output: 4
correct answer: 3
"""
