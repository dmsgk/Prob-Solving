# 136. Single Number
# xor 활용한 풀이. counter 활용한 것과 시간, 메모리효율은 동일.
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result




nums = [1, 2, 3, 2, 1]

result = 0
for num in nums:
    print("num: ", num, "result: ", result)
    result^= num
    print("result: ", result)
    print()
