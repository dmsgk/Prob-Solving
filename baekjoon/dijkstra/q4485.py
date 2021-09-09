# 녹색옷입은애가젤다지?
import sys
import heapq


def dijkstra(board, n):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = []
    dist = [[sys.maxsize] * n for _ in range(n)]
    dist[0][0] = board[0][0]
    visited = {(0,0)}
    heapq.heappush(q, (dist[0][0], [0, 0]))

    while q:
        cost, xy = heapq.heappop(q)
        x, y = xy
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited:
                if dist[nx][ny] > dist[x][y] + board[nx][ny]:
                    dist[nx][ny] = dist[x][y] + board[nx][ny]
                    heapq.heappush(q, (dist[nx][ny], [nx,ny]))

    return dist[n-1][n-1]


cnt = 0

while 1:
    cnt += 1
    n = int(sys.stdin.readline())
    if n == 0:
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    answer = dijkstra(board, n)
    cnt_str = str(cnt)
    iteration_str = "Problem " + cnt_str + ":"

    print(iteration_str, answer)