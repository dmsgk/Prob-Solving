import sys
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[0]* m for _ in range(n)]

dx, dy = [1,-1,0,0], [0,0,1,-1]
queue = deque([[0, 0]])
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    graph[x][y] = 0
    if x == n-1 and y == m-1:
        print(visited[n-1][m-1])
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<= nx < n and 0<= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx, ny])

"""
4 6
101111
101010
101011
111011

7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111

"""