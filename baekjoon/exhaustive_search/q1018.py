# 체스판 다시 찰하기
import sys


def cnt_blocks(chess_board):
    global cnt_li
    case_li = [['W', 'B'], ['B', 'W']]
    for c in case_li:
        start, opposite = c
        cnt = 0
        for p in range(8):
            for q in range(8):
                if (p+q)%2 == 0:
                    if chess_board[p][q] != start:
                        cnt += 1
                else:
                    if chess_board[p][q] != opposite:
                        cnt += 1

        cnt_li.append(cnt)


n, m = map(int, sys.stdin.readline().split())  # n이 행, m이 열
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

cnt_li = []
# 보드 채택 후 칸수 세서, 저장 후 min값 도출하기

for i in range(n + 1 - 8):
    for j in range(m + 1 - 8):
        chess_board = []
        for r in range(0 + i, 8 + i):
            chess_board.append(board[r][0 + j:8 + j])
        cnt_blocks(chess_board)

print(min(cnt_li))