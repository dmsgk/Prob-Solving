# 경사로

import sys

n, l = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
roads = 0

# 길이 되는 행 있는지 순회
for r in range(n):
    s = set(board[r])
    if len(s) == 1:  # 한 숫자로만 되어있을 경우
        roads += 1
    else:
        left, right = 0, 1
        roads_flag = False
        slides = set()  # 각 행마다 설정된 경사로 저장
        while left < right and right < n:
            if board[r][left] == board[r][right]:   # left, right 두 값이 같을 때.
                left += 1
                right += 1
            elif board[r][left] - board[r][right] == 1:   # 아래로 내려가는 형태.
                while right < n-1 and right-left < l and board[r][right] == board[r][right+1] and right+1 not in slides:
                    right += 1
                if right - left == l:
                    roads_flag = True
                    slide_idx = [right - i for i in range(l)]
                    slides.update(slide_idx)
                    left = right
                    right = left + 1
                    if right < n and board[r][left] < board[r][right]:
                        roads_flag = False
                        break
                else:
                    roads_flag = False
                    break
            elif board[r][right] - board[r][left] == 1:  # 위로 올라가는 형태
                while left > 0 and right - left < l and board[r][left] == board[r][left - 1] and left-1 not in slides:
                    left -= 1
                if right - left == l:
                    roads_flag = True
                    slide_idx = [left + i for i in range(l)]
                    slides.update(slide_idx)
                    left = right
                    right = left + 1
                else:
                    roads_flag = False
                    break
            else:  # 왼쪽값과 2이상 차이나는 경우.
                roads_flag = False
                break

        if roads_flag:
            roads += 1

# 길이 되는 열 있는지 순회
for c in range(n):
    s = {board[i][c] for i in range(n)}
    if len(s) == 1:  # 한 숫자로만 되어있을 경우
        roads += 1
    else:
        left, right = 0, 1
        roads_flag = False
        slides = set()  # 각 열마다 설정된 경사로 저장
        while left < right < n:
            if board[left][c] == board[right][c]:   # left, right 두 값이 같을 때.
                left += 1
                right += 1
            elif board[left][c] - board[right][c] == 1:   # 아래로 내려가는 형태.
                while right < n-1 and right-left < l and board[right][c] == board[right+1][c] and right+1 not in slides:
                    right += 1
                if right - left == l:
                    roads_flag = True
                    slide_idx = [right-i for i in range(l)]
                    slides.update(slide_idx)
                    left = right
                    right = left + 1
                    if right < n and board[left][c] < board[right][c]:
                        roads_flag = False
                        break
                else:
                    roads_flag = False
                    break
            elif board[right][c] - board[left][c] == 1:  # 위로 올라가는 형태
                while left > 0 and right - left < l and board[left][c] == board[left-1][c] and left-1 not in slides:
                    left -= 1
                if right - left == l:
                    roads_flag = True
                    slide_idx = [left + i for i in range(l)]
                    slides.update(slide_idx)
                    left = right
                    right = left + 1
                else:
                    roads_flag = False
                    break
            else:  # 왼쪽값과 2이상 차이나는 경우.
                roads_flag = False
                break

        if roads_flag:
            roads += 1
print(roads)
"""
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2

3 출력

6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

7 출력 

6 3
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

# 3 출력
"""