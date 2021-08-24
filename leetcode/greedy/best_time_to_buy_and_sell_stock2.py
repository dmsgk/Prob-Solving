# 122. Best Time to Buy and Sell Stock II
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]

        return result

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # 7
print(solution.maxProfit([1,2,3,4,5]))  # 4
