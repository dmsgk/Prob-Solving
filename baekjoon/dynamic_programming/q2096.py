# 내려가기
import sys

n = int(sys.stdin.readline().rstrip())
row = list(map(int, sys.stdin.readline().rstrip().split()))
M_dp, m_dp = row, row

for i in range(1, n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))

    max_first = max(M_dp[0], M_dp[1]) + row[0]
    max_second = max(M_dp) + row[1]
    max_third = max(M_dp[1], M_dp[2]) + row[2]

    min_first = min(m_dp[0], m_dp[1]) + row[0]
    min_second = min(m_dp) + row[1]
    min_third = min(m_dp[1], m_dp[2]) + row[2]

    M_dp = [max_first, max_second, max_third]
    m_dp = [min_first, min_second, min_third]

ans_max = max(M_dp)
ans_min = min(m_dp)
print(ans_max, ans_min)

