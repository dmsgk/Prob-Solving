# 상어 초등학교

import sys

n = int(sys.stdin.readline())
board = [[0]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def fill_seat(n, board):
    answer_dict = dict()
    for _ in range(n**2):
        num, s1, s2, s3, s4 = map(int, sys.stdin.readline().split())
        like_set = {s1, s2, s3, s4}
        answer_dict[num] = like_set
        result = []
        for x in range(n):
            for y in range(n):
                if board[x][y] != 0:
                    continue
                like_cnt, empty_cnt = 0, 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 0:
                            empty_cnt += 1
                        elif board[nx][ny] in like_set:
                            like_cnt += 1
                result.append([-like_cnt, -empty_cnt, x, y])
        result.sort()
        minus_lc, minus_ec, r, c = result[0]
        board[r][c] = num

    return board, answer_dict


def calculate_score(n, board, answer_dict):
    total_score = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            student_num = board[x][y]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in answer_dict[student_num]:
                        cnt += 1
            if cnt == 0:
                continue
            total_score += 10**(cnt-1)
    return total_score


board, answer_dict = fill_seat(n, board)
print(calculate_score(n, board, answer_dict))
