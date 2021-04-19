# dfs로 풀기

def dfs(data, cnt, start):
    stack = []
    stack.append(start)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:  # 스택이 비어있지 않을 때까지. 단지내 탐색 계속함
        [x, y] = stack.pop()
        data[x][y] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx< n and 0<= ny and ny <n:
                if data[nx][ny] == 1:
                    cnt += 1
                    data[nx][ny] = -1
                    stack.append([nx,ny])
    return cnt


import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())
data = [list(map(int, list(read()))) for _ in range(n)]


cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            ans.append(dfs(data, cnt+1, [i, j]))

print(len(ans))
for i in sorted(ans):
    print(i)
