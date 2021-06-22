# 198. House Robber
from typing import List
import copy


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = copy.deepcopy(nums)

        idx = 2
        while idx < len(nums):
            dp[idx] = dp[idx] + max(dp[:idx - 1])
            idx += 1

        return max(dp)


test = Solution()
print(test.rob([2,1,1,2]))  # 4
