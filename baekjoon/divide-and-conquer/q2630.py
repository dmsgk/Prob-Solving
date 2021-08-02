# 색종이 만들기
import sys

sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
wp_cnt, bp_cnt = 0, 0


def recursion(n, board):
    global wp_cnt, bp_cnt
    if n == 0:  # 종료조건
        return

    color_set = set()
    for i in range(n):
        color_set.update(board[i])  # board가 하나의 색으로 이루어졌는지 체크

    if color_set == {0} or color_set == {1}:
        if color_set == {0}:
            wp_cnt += 1
        else:
            bp_cnt += 1
        return

    # 분할정복
    for j in range(4):
        if j == 0:  # 1구역
            new_b = [board[r][:n//2] for r in range(n//2)]
            recursion(n//2, new_b)
        elif j == 1:  # 2구역
            new_b = [board[r][n//2:] for r in range(n//2)]
            recursion(n // 2, new_b)
        elif j == 2:  # 3구역
            new_b = [board[r][:n//2] for r in range(n//2, n)]
            recursion(n // 2, new_b)
        elif j == 3:  # 4구역
            new_b = [board[r][n//2:] for r in range(n//2, n)]
            recursion(n // 2, new_b)


recursion(n, board)
print(wp_cnt)
print(bp_cnt)