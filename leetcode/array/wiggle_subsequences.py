# 376. Wiggle Subsequence
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diff = [nums[i+1] -nums[i] for i in range(len(nums)-1) if (nums[i+1] -nums[i]) != 0]
        idx = []

        for i in range(0, len(diff)-1):
            if diff[i] * diff[i+1] > 0:
                idx.append(i)
        return len(diff)-len(idx) + 1



test = Solution()
print(test.wiggleMaxLength([1,7,4,9,2,5]))  # 6
print(test.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))  # 7
print(test.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))  # 2
print(test.wiggleMaxLength([0,0]))  # 1

