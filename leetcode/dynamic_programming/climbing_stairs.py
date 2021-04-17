# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        global result
        if len(result)-1 >= n:
            return result[n]

        result.append(self.climbStairs(n-1)+self.climbStairs(n-2))
        print(result)
        return result[n]


result = [0,1,2]
test = Solution()
print(test.climbStairs(4))


