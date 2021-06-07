# 구슬탈출2
import sys
from collections import deque


def bfs(b, r, o, board):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = {(b[0],b[1], r[0], r[1])}
    ans = 0
    queue = deque([[b[0],b[1], r[0], r[1], ans]])

    while queue:
        bx, by, rx, ry, ans = queue.popleft()
        if ans > 10:  # 10번 넘어가는 경우 -1 리턴
            return -1
        if [rx, ry] == o:
            return ans

        for i in range(4):
            next_bx, next_by = bx + dx[i], by + dy[i]
            next_rx, next_ry = rx + dx[i], ry + dy[i]

            # ---파란공
            while 0 < next_bx < n - 1 and 0 < next_by < m - 1 and board[next_bx][next_by] == '.':  # 파란공 다음이 빈 곳일때
                next_bx += dx[i]
                next_by += dy[i]
            if board[next_bx][next_by] == 'O':  # 파란공 구멍에 빠지면 경로에 추가하지 않고 해당 for문 넘긴다.
                continue
            next_bx -= dx[i]
            next_by -= dy[i]
            # ---빨간공

            while 0 < next_rx < n - 1 and 0 < next_ry < m - 1 and board[next_rx][next_ry] == '.':
                next_rx += dx[i]
                next_ry += dy[i]

            if not (0 < next_rx < n - 1 and 0 < next_ry < m - 1 and board[next_rx][next_ry] == 'O'):         # 경계값까지 갔을 때나 장애물이 있을 때  한칸 뒤로 가준다.
                next_rx -= dx[i]
                next_ry -= dy[i]

            if next_bx == next_rx and next_by == next_ry:  # 파란공이 가려는 방향으로 한칸 앞에 있을 때(빨간공 위치 예외처리해야)
                if bx-rx == 0:
                    if (dy[i] == 1 and (ry-by) >= dy[i]) or (dy[i] == -1 and (ry-by) <= dy[i]):
                        next_by -= dy[i]
                    else:
                        next_ry -= dy[i]
                if by-ry == 0:
                    if (dx[i] == 1 and (rx-bx) >= dx[i]) or (dx[i] == -1 and (rx-bx) <= dx[i]):
                        next_bx -= dx[i]
                    else:
                        next_rx -= dx[i]
            # ---------

            if board[next_bx][next_by] != 'O'and (next_bx, next_by, next_rx, next_ry) not in visited:
                queue.append([next_bx, next_by, next_rx, next_ry, ans+1])
                visited.add((next_bx, next_by, next_rx, next_ry))
    return -1


n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'
        elif board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'O':
            ox, oy = i, j

print(bfs([bx, by], [rx, ry], [ox,oy], board))

"""
5 10 
##########
#........#
#.####...#
#R##O..#B#
##########
답 :: 6

6 7
#######
#..BR##
#.#####
#.#O###
#....##
#######
답 :: 8

6 7
#######
##RB..#
#####.#
###O#.#
##....#
#######
답 :: 8

6 7
#######
#..BR##
#.#####
#.#O###
#....##
#######
답 :: 8

6 7
#######
#....##
#.#O###
#.#####
#..BR##
#######
답 :: 8

10 10
##########
#.......O#
#.#.....B#
#........#
#........#
##.......#
#....#..R#
#.##.....#
#........#
##########

4 출

10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########

10 출력

5 5
#####
#..B#
#.#.#
#RO.#
#####

1출력
"""

"""
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

5 출력


3 7
#######
#R.O.B#
#######

1 출력 
"""
