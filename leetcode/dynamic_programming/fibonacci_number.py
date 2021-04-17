# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]

        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])

        print(dp)
        return dp[n]



test = Solution()
print(test.fib(100))
