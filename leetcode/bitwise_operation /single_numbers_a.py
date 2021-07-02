# 136. Single Number
# xor 활용한 풀이. counter 활용한 것과 시간, 메모리효율은 동일.
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
