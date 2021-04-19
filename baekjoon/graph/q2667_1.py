# bfs로 풀기

def bfs(data, cnt, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    data[x][y]=0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(0, 4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx< n and 0<= ny and ny <n:
                if data[nx][ny] == 1:
                    cnt += 1
                    data[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt



import sys
from collections import deque

read = lambda : sys.stdin.readline().strip()

n = int(read())
data = [list(map(int, list(read()))) for _ in range(n)]


cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            ans.append(bfs(data, cnt+1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)