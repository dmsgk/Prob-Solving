from collections import deque


def solution(m, n, puddles):
    board = [[0] * (m + 1) for _ in range(n + 1)]
    for p in puddles:
        j, i = p
        board[i][j] = -1
    dx, dy = [1, 0], [0, 1]
    q = deque([[1, 1]])
    board[1][1] = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == -1:
            continue

        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= n and 0 < ny <= m and board[nx][ny] >= 0:
                q.append([nx, ny])
                board[nx][ny] += board[x][y]
        if x == n and y == m:
            continue
        board[x][y] = -1

    return board[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))  # 4