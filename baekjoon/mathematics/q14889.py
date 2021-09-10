# 스타트와 링크

import sys
from itertools import combinations, permutations

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_diff = sys.maxsize  # 차이의 최솟값 초기화
num_range = {i for i in range(n)}

combi = list(combinations(num_range, n//2))  # n//2 명씩의 조합
length = len(combi)
half_combi = combi[length//2:]  # 조합 리스트의 뒷부분 절반
half_combi.reverse()

for i in range(length//2):
    start = combi[i]
    link = half_combi[i]
    c_per = list(permutations(start, 2))  # start 팀 구성 시 팀원 2명씩의 순열
    rest_per = list(permutations(link, 2))  # link 팀 구성 시 팀원 2명씩의 순열

    start_sum, link_sum = 0, 0  # 팀원 간 시너지 합 초기화
    for p in range(len(c_per)):  # 각 조합에서의 시너지 합 더하기
        c_row, c_col = c_per[p]
        r_row, r_col = rest_per[p]

        start_sum += board[c_row][c_col]
        link_sum += board[r_row][r_col]

    diff = abs(start_sum - link_sum)
    min_diff = min(min_diff, diff)  # 최솟값 업데이트하기.

print(min_diff)






"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

0 출력 

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

2 출력

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0

1 출력  
"""