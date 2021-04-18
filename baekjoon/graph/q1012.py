import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n, k = map(int, sys.stdin.readline().split())

    Map = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        Map[y][x] = 1
    cnt = 0

    def dfs(Map, i, j):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        stack = [[i, j]]

        while stack:
            y, x = stack.pop()
            Map[y][x] = -1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < m and 0<= ny < n and Map[ny][nx] == 1:
                    Map[ny][nx] = -1
                    stack.append([ny, nx])
    for i in range(n):
        for j in range(m):
            if Map[i][j] <= 0:
                Map[i][j] = -1
            else:
                cnt += 1
                dfs(Map, i, j)
    print(cnt)