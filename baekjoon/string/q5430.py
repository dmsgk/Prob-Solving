# AC
import sys
from collections import deque


def AC(p, num_li):
    reverse_cnt = 1
    for i in range(len(p)):
        if p[i] == 'R':
            reverse_cnt *= -1
        else:
            if not num_li:
                return 'error'
            if reverse_cnt == 1:
                num_li.popleft()
            else:
                num_li.pop()

    if reverse_cnt == -1:
        num_li.reverse()

    return num_li


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        sys.stdin.readline().rstrip()
        num_li = []
    else:
        arr_str = sys.stdin.readline().rstrip()
        arr_str = arr_str.lstrip("[")
        arr_str = arr_str.rstrip("]")
        num_li = deque(map(int,arr_str.split(",")))

    result = AC(p, num_li)
    if result == 'error':
        print(result)
    else:
        print('[', end='')
        for i, r in enumerate(result):
            if i == len(result) - 1:
                print(r, end='')
                continue
            print(r, end=',')
        print(']')
