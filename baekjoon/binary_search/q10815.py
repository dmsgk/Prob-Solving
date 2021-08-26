# 숫자카드
import sys


def solution(num_li, m_num):
    global ans
    start, end = 0, n-1

    while start <= end:
        mid = (start + end) // 2
        if m_num == num_li[mid]:
            ans.append(1)
            return
        elif m_num < num_li[mid]:
            end = mid - 1
        else:
            start = mid + 1
    ans.append(0)


n = int(sys.stdin.readline())
num_li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split()))

num_li.sort()
ans = []

for i in range(m):
    solution(num_li, m_li[i])

print(*ans)