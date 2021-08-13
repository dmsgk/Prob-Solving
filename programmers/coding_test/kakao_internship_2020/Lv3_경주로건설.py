# 경주로 건설
from collections import deque


def solution(board):
    queue = deque()
    n = len(board)
    visited = [[-1] * n for _ in range(n)]  # 방문경로, 그 당시 건설 금액
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 남서북동(시계방향)

    # 초깃값 설정(queue, visited)
    visited[0][0] = 0
    for i in [0, 3]:  # 남, 동 방향
        nx, ny = dx[i], dy[i]
        if board[nx][ny] == 0:
            queue.append([nx, ny, i, 100])  # 방문행, 열, 방향, 금액
            visited[nx][ny] = 100

    while queue:
        x, y, d, c = queue.popleft()
        if x == n - 1 and y == n - 1:
            continue

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                temp = c + 100  # 기본 직선도로 비용
                if d != j:  # 코너 생성비용
                    temp += 500

                if visited[nx][ny] == -1 or temp <= visited[nx][ny]:
                    visited[nx][ny] = temp
                    queue.append([nx, ny, j, temp])

    return visited[n - 1][n - 1]

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))