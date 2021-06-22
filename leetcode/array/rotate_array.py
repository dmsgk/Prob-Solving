# 189. Rotate Array


from typing import List
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums = deque(nums)
        for _ in range(k):
            n = nums.pop()
            nums.appendleft(n)

        nums = list(nums)
        print(nums)

        """
        Do not return anything, modify nums in-place instead.
        """

test = Solution()
print(test.rotate([1,2,3,4,5,6,7], 3))
