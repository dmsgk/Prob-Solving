n = int(input())

# 단순 재귀로 풀기
def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)

print(factorial(n))

# 메모이제이션으로 풀기
def dp_factorial(n):
    dp = [1,1]
    for i in range(2,n+1):
        dp.append(i* dp[i-1])
    return dp[n]

print(dp_factorial(n))