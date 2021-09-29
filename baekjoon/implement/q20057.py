# 마법사 상어와 토네이도
import sys

n = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0  # 밖으로 나간 모래의 양


# 이동시 모래 분배하기.
def share_sand(r, c, i, board):  # 시작행,열, 방향.
    global cnt
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향으로 구현하기. 우하좌상
    yr, yc = r + dr[i], c + dc[i]

    if 0 <= yr < n and 0 <= yc < n and board[yr][yc] > 0:
        sand_amount = board[yr][yc]
        board[yr][yc] = 0

        alpha = sand_amount - (2 * (int(sand_amount * 0.01) + int(sand_amount * 0.07) + int(sand_amount * 0.02) + int(sand_amount * 0.1)) + int(sand_amount * 0.05))
        inboard_cnt = 0

        # 1퍼센트
        share = int(sand_amount * 0.01)
        if 0 <= r + dr[(i+1)%4] < n and 0 <= c + dc[(i+1)%4] < n:
            inboard_cnt += share
            board[r + dr[(i+1)%4]][c + dc[(i+1)%4]] += share

        if 0 <= r + dr[(i-1)%4] < n and 0 <= c + dc[(i-1)%4] < n:
            inboard_cnt += share
            board[r + dr[(i-1)%4]][c + dc[(i-1)%4]] += share

        # 7퍼센트
        share = int(sand_amount * 0.07)
        if 0 <= yr + dr[(i+1)%4] < n and 0 <= yc + dc[(i+1)%4] < n:
            inboard_cnt += share
            board[yr + dr[(i+1)%4]][yc + dc[(i+1)%4]] += share

        if 0 <= yr + dr[(i-1)%4] < n and 0 <= yc + dc[(i-1)%4] < n:
            inboard_cnt += share
            board[yr + dr[(i-1)%4]][yc + dc[(i-1)%4]] += share

        # 2퍼센트
        share = int(sand_amount * 0.02)
        if 0 <= yr + 2 * dr[(i+1)%4] < n and 0 <= yc + 2 * dc[(i+1)%4] < n:
            inboard_cnt += share
            board[yr + 2 * dr[(i+1)%4]][yc + 2 * dc[(i+1)%4]] += share

        if 0 <= yr + 2 * dr[(i-1)%4] < n and 0 <= yc + 2 * dc[(i-1)%4] < n:
            inboard_cnt += share
            board[yr + 2 * dr[(i-1)%4]][yc + 2 * dc[(i-1)%4]] += share

        # 10퍼센트
        share = int(sand_amount * 0.1)
        if 0 <= yr + dr[(i+1)%4] + dr[i] < n and 0 <= yc + dc[(i+1)%4] + dc[i] < n:
            inboard_cnt += share
            board[yr + dr[(i+1)%4] + dr[i]][yc + dc[(i+1)%4] + dc[i]] += share

        if 0 <= yr + dr[(i-1)%4] + dr[i] < n and 0 <= yc + dc[(i-1)%4] + dc[i] < n:
            inboard_cnt += share
            board[yr + dr[(i-1)%4] + dr[i]][yc + dc[(i-1)%4] + dc[i]] += share

        # 5퍼센트
        share = int(sand_amount * 0.05)
        if 0 <= yr + 2 * dr[i] < n and 0 <= yc + 2 * dc[i] < n:
            inboard_cnt += share
            board[yr + 2 * dr[i]][yc + 2 * dc[i]] += share

        # alpha
        if 0 <= yr + dr[i] < n and 0 <= yc + dc[i] < n:
            board[yr + dr[i]][yc + dc[i]] += alpha
            inboard_cnt += alpha

        cnt += (sand_amount - inboard_cnt)
    return board


# 중앙부터 (1,1)까지 이동하기
# 좌회전이 visited되지 않았으면 무조건 좌회전. 좌회전 안되면 직진.
start = n//2
x, y = start, start
dir = 3

visited = [[False]*n for _ in range(n)]
visited[start][start] = True
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

while x != 0 or y != 0:
    lrx, lry = x + dx[(dir - 1) % 4], y + dy[(dir - 1) % 4]
    if not visited[lrx][lry]:
        board = share_sand(x, y, (dir-1) % 4, board)
        visited[lrx][lry] = True
        x, y = lrx, lry
        dir = (dir-1) % 4
    else:
        srx, sry = x + dx[dir], y + dy[dir]
        board = share_sand(x, y, dir, board)
        visited[srx][sry] = True
        x, y = srx, sry

print(cnt)
