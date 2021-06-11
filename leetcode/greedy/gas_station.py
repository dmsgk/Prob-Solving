# 134. Gas Station
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)

        for i in range(length):
            tank = gas[i] - cost[i]
            idx = i + 1
            while tank >=0 and idx % length != i:
                tank = tank + gas[idx % length] - cost[idx % length]
                idx += 1
            if idx % length == i and tank >=0:
                return i
        return -1


test = Solution()
# print(test.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
print(test.canCompleteCircuit([2,3,4],[3,4,3]))  # -1

"""
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

"""



