# 198. House Robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0,0]

        for i, v in enumerate(nums):
            if i % 2 == 1:
                ans[0] += v
            else:
                ans[1] += v

        return max(ans)

test = Solution()
print(test.rob([2,1,1,2]))  # 4
