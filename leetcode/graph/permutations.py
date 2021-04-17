# 46. Permutations
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = itertools.permutations(nums)
        return list(p)


test = Solution()
print(test.permute([1,2,3]))