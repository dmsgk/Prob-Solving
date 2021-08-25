# 치킨 배달
import sys
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 0은 빈칸, 1은 집, 2는 치킨집
chi_pos = []
house_pos = set()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house_pos.add((i,j))
        elif board[i][j] == 2:
            chi_pos.append([i,j])


def bfs(survived, house_pos):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = [[-1]*n for _ in range(n)]
    queue = deque(survived)
    result = 0

    for i in range(m):
        x, y = survived[i]
        board[x][y] = 0

    while queue:
        # print(*board, sep='\n')
        # print()
        x, y = queue.popleft()
        if (x,y) in house_pos:
            result += board[x][y]

        for l in range(4):
            nx, ny = x + dx[l], y + dy[l]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                queue.append([nx,ny])
    return result

chicken_dist = []
chicken_com = list(combinations(chi_pos, m))
# print(chicken_com)

for location in chicken_com:
    # m개의 치킨집 조합 location 튜플로 나타남
    result = bfs(location, house_pos)
    chicken_dist.append(result)

# print(chicken_dist)
print(min(chicken_dist))









