# 189. Rotate Array
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            n = nums.pop()
            nums.insert(0, n)
        """
        Do not return anything, modify nums in-place instead.
        """

test = Solution()
print(test.rotate([1,2,3,4,5,6,7], 3))
