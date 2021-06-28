# 톱니바퀴

import sys
from collections import deque


def engage_cogs(cog_dict, cog_num, direction):
    sawtooth_li = []  # 맞닿은 톱니의 방향 저장
    for i in range(1,5):
        if i == 1:
            sawtooth_li.append(cog_dict[i][2])
        elif i == 4:
            sawtooth_li.append(cog_dict[i][6])
        else:
            sawtooth_li.append(cog_dict[i][6])
            sawtooth_li.append(cog_dict[i][2])

    rotate = [[cog_num, direction]]  # 회전하는 톱니바퀴번호, 방향(-1, 1) 리스트

    temp_l, temp_r = direction, direction
    for idx in range(2*(cog_num-1), 6): # 오른쪽으로 가는 탐색
        if idx % 2 == 0:
            if sawtooth_li[idx] == sawtooth_li[idx+1]:
                break
            elif sawtooth_li[idx] != sawtooth_li[idx+1]:
                temp_r *= -1
                rotate.append([idx//2+2, temp_r])
    for idx in range(2*(4-cog_num)+1, 6): # 왼쪽으로 가는 탐색
        if idx % 2 == 1:
            if sawtooth_li[-idx] == sawtooth_li[-idx-1]:
                break
            elif sawtooth_li[-idx] != sawtooth_li[-idx-1]:
                temp_l *= -1
                rotate.append([3-(idx)//2, temp_l])
    return rotate_cogs(cog_dict, rotate)


def rotate_cogs(cog_dict, rotate):  # 결과값을 토대로 톱니바퀴 회전시키는 함수
    for r in rotate:
        idx, direction = r
        cog = cog_dict[idx]
        if direction == 1: # 시계방향
            last = cog.pop()
            cog.appendleft(last)
            cog_dict[idx] = cog
        else:
            first = cog.popleft()
            cog.append(first)
            cog_dict[idx] = cog
    return cog_dict


cog_dict = dict()
for i in range(1, 5):
    cog_dict[i] = deque(map(int, list(sys.stdin.readline().strip())))  # N극은 0, S극은 1로 나타냄

k = int(sys.stdin.readline().strip())
for _ in range(k):
    cog_num, direction = map(int, sys.stdin.readline().strip().split())   # 방향 1인경우 시계방향, -1인 경우 반시계방향
    cog_dict = engage_cogs(cog_dict, cog_num, direction)  # 값을 계산해서 cog_dict에 업데이트한다.

ans = 0
for i in range(1,5):
    if cog_dict[i][0] == 1: # s극일 경우
        ans += 2**(i-1)

print(ans)