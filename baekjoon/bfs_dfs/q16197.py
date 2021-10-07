# 두 동전
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
coin_loc = set()
for i in range(n):
    col = list(sys.stdin.readline().strip())
    for j in range(m):
        if col[j] == 'o':
            coin_loc.add((i,j))
            col[j] = '.'
    board.append(col)


def bfs(coin_loc, board):
    queue = deque([[coin_loc, 0]])
    visited = [coin_loc]  # 방문위치 넣기
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        coin_loc, cnt = queue.popleft()
        if len(coin_loc) == 1:
            c1 = coin_loc.pop()
            c2 = c1
        else:
            c1, c2 = coin_loc
        x1, y1 = c1
        x2, y2 = c2

        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if not (0 <= nx1 < n and 0 <= ny1 < m) and not (0 <= nx2 < n and 0 <= ny2 < m):
                continue
            if (0 <= nx1 < n and 0 <= ny1 < m) and (0 <= nx2 < n and 0 <= ny2 < m):
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                if {(nx1, ny1), (nx2, ny2)} not in visited:
                    queue.append([{(nx1, ny1), (nx2, ny2)}, cnt+1])
                    visited.append({(nx1, ny1), (nx2, ny2)})
            else:
                if cnt < 10:
                    return cnt + 1
                else:
                    return -1
    return -1


print(bfs(coin_loc, board))
