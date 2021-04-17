# 77. Combinations
import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        c = list(itertools.combinations(list(range(1,n+1)),k))
        return c

test = Solution()
print(test.combine(4,2))