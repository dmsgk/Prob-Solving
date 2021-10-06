# 아기상어
import sys
from collections import deque
import heapq

n = int(sys.stdin.readline())
board = []
x, y = -1, -1
fish_size = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0
        elif board[i][j] > 0:
            fish_size.append(board[i][j])


# 자신보다 큰 물고기가 있는 곳은 지나갈수도 먹을수도 없고, 자신과 같은 크기인 물고기가 있는 칸은 지나갈 수만 있음
def bfs(board, x,y, size, fish_size):
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]  # 상, 좌, 우, 하
    queue = deque([[x, y, 1, size, 0]]) # 현재행, 열, 방문한 위치, 현재 상어의 크기, 현재 크기에서 먹은 물고기의 개수
    ans = 0
    visited = [(x, y)]
    path_len = sys.maxsize
    path_heap = []  # 최단경로에 있는 좌표들 저장
    while queue:
        x, y, move_cnt, curr_size, cnt = queue.popleft()
        flag = False

        if not fish_size or min(fish_size) >= curr_size:
            break

        if 0 < board[x][y] < curr_size:
            path_len = min(path_len, move_cnt)
            if move_cnt <= path_len:
                heapq.heappush(path_heap, (x, y))
                flag = True

        if not flag and move_cnt < path_len:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] <= curr_size and (nx,ny) not in visited:
                    visited += [(nx,ny)]
                    queue.append([nx,ny, move_cnt+1, curr_size, cnt])

        if not queue and path_heap:
            x, y = heapq.heappop(path_heap)
            f_size = board[x][y]
            board[x][y] = 0
            fish_size.remove(f_size)
            if cnt + 1 == curr_size:
                curr_size += 1
                cnt = 0
            else:
                cnt += 1

            ans += path_len - 1
            queue = deque([[x,y, 1, curr_size, cnt]])  # 새로 초기화
            visited = [(x,y)]
            path_len = sys.maxsize
            path_heap = []

    return ans

print(bfs(board, x, y, 2, fish_size))