# 주사위 굴리기
from collections import deque

n, m, x, y, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
order = list(map(int,input().split()))

direction = {1: [0,1], 2: [0,-1], 3: [-1,0], 4: [1,0]}
ver = deque([0]*4)
hor = deque([0]*3)

for o in order:
    dx, dy = direction[o]
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
        if o == 1:  # east
            down = ver.pop()
            hor.append(down)
            left = hor.popleft()
            ver.append(left)
            ver[1] = hor[1]

        elif o == 2:  # west
            down = ver.pop()
            hor.appendleft(down)
            right = hor.pop()
            ver.append(right)
            ver[1] = hor[1]
        elif o == 3:  # north
            down = ver.pop()
            ver.appendleft(down)
            hor[1] = ver[1]
        else:  # south
            up = ver.popleft()
            ver.append(up)
            hor[1] = ver[1]

        num = ver[1]
        if board[nx][ny] == 0:  # 지도가 0일때
            board[nx][ny] = num
        else:  # 지도가 0이 아닐 때
            num = board[nx][ny]
            board[nx][ny] = 0
            hor[1] = num
            ver[1] = num

        print(ver[-1])
        x, y = nx,ny



"""
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

0
0
3
0
0
8
6
3


2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2

0
0
0
0


3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2

0
0
0
6
0
8
0
2
0
8
0
2
0
8
0
2

"""

