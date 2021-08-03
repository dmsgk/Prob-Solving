# N-Queen

n = int(input())
board = [[-1]*n for _ in range(n)]
ans = 0

def recur(line):
    global ans
    # 종료조건
    if line == n:
        ans += 1
        return

    for j in range(n):
        if board[line][j] != -1:
            continue
        # 우
        for c in range(j, n):
            if board[line][c] == -1:
                board[line][c] = line
        # 하
        for r in range(line+1, n):
            if board[r][j] == -1:
                board[r][j] = line
        # 대각선
        for x in range(1, n):
            if line + x < n:
                if 0 <= j - x and board[line+x][j-x] == -1:
                    board[line+x][j-x] = line
                if j + x < n and board[line+x][j+x] == -1:
                    board[line+x][j+x] = line

        recur(line + 1)
        # 지금 queen의 흔적 지우기
        # 우
        for c in range(j, n):
            if board[line][c] == line:
                board[line][c] = -1
        # 하
        for r in range(line + 1, n):
            if board[r][j] == line:
                board[r][j] = -1

        # 대각선
        for x in range(1, n):
            if line + x < n:
                if 0 <= j - x and board[line+x][j-x] == line:
                    board[line+x][j-x] = -1
                if j + x < n and board[line+x][j+x] == line:
                    board[line+x][j+x] = -1




## 메인
recur(0)
print(ans)