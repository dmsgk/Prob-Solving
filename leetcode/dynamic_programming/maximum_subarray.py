# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = []

        for num in nums:
            if not sum or sum[-1] < 0:
                sum.append(num)
            else:
                sum.append(num + sum[-1])

        return max(sum)


test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6