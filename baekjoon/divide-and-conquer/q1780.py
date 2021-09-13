# 종이의 개수
import sys


# 해당 구간이 하나의 숫자로 이루어졌는지 확인하는 함수
def get_board_status(row, col, n, board):
    check = board[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if board[i][j] != check:
                return False, check
    return True, check


def recursion(row, col, n, board):
    global minus_cnt, zero_cnt, plus_cnt
    flag, check = get_board_status(row, col, n, board)

    if flag:
        if check == -1:
            minus_cnt += 1
        elif check == 0:
            zero_cnt += 1
        else:
            plus_cnt += 1
    else:
        for i in range(3):
            for j in range(3):
                recursion(row + i * (n//3), col + j * (n//3), n//3, board)


def solution(board, n):
    global minus_cnt, zero_cnt, plus_cnt

    if n == 1:
        if board[0][0] == -1:
            minus_cnt += 1
        elif board[0][0] == 0:
            zero_cnt += 1
        else:
            plus_cnt += 1
        return
    recursion(0, 0, n, board)


sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

solution(board,n)
print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
