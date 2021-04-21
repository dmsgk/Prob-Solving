# 파도반 수열

def p(n):
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for i in range(11, n+1):
        dp.append(dp[-1]+dp[-5])
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(p(n))




