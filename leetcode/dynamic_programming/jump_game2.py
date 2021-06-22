# 45. Jump Game II

import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize] * len(nums)
        dp[0] = 0
        for idx, n in enumerate(nums):
            for j in range(1, n + 1):
                if idx + j < len(nums):
                    dp[idx + j] = min(dp[idx] + 1, dp[idx + j])

        return dp[-1]

