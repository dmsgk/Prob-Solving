# 알파벳
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(r)]
cnt_set = set()


def bfs(board):
    global cnt_set
    queue = deque([[0, 0, {board[0][0]}]])
    visited = {(0,0)}
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y, alphabet = queue.popleft()
        flag = False
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and (nx,ny) not in visited and board[nx][ny] not in alphabet:
                queue.append([nx, ny, alphabet | {board[nx][ny]}])
                visited.add((nx, ny))
                flag = True
        if not flag:
            print(alphabet, len(alphabet))
            cnt_set.add(len(alphabet))

bfs(board)
print(max(cnt_set))
