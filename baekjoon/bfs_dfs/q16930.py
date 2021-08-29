# 달리기
import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
a, b, x, y = map(int, sys.stdin.readline().split())  # a, b 에서 x, y로


def bfs(board, start_x, start_y, final_x, final_y, k):
    check = [[-1] * m for _ in range(n)]
    queue = deque([[start_x-1,start_y-1]])
    check[start_x-1][start_y-1] = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        if x == final_x - 1 and y == final_y - 1:
            return check[x][y]

        for i in range(4):
            for j in range(1, k+1):
                nx, ny = x + j * dx[i], y + j * dy[i]
                if not(0 <= nx < n and 0 <= ny < m) or board[nx][ny] == '#':
                    break
                if -1 != check[nx][ny] <= check[x][y]:  # 이미 더 짧은 거리로 지나간 경우,
                    break
                if -1 != check[nx][ny]:  # 이미 지나갔지만 현재 더 짧은 거리로 지나는 경우, 다음 경로를 위해 continue
                    continue
                queue.append([nx, ny])
                check[nx][ny] = check[x][y] + 1


    return -1


print(bfs(board, a, b, x, y, k))