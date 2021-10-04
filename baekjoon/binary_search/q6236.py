# 용돈관리
import sys

n, m = map(int, sys.stdin.readline().split())
day_money = [int(sys.stdin.readline()) for _ in range(n)]

left, right = max(day_money), sum(day_money)
while left <= right:
    curr_money, withdraw_cnt = 0, 0
    mid = (left + right) // 2
    for d_money in day_money:
        if curr_money < d_money:
            curr_money = mid - d_money
            withdraw_cnt += 1
        else:
            curr_money -= d_money
    if withdraw_cnt <= m:
        right = mid - 1

    else:
        left = mid + 1

print(left)