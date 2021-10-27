# 욕심쟁이 판다
# 해설 참고. 나중에 다시 풀어볼 것.
import sys
sys.setrecursionlimit(10**6)


def dfs(x,y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
    return dp[x][y]


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]  # 각 위치를 시작점으로 해 최대로 갈 수 있는 칸.

result = 1
for i in range(n):
    for j in range(n):
        result = max(dfs(i,j), result)

print(result)
