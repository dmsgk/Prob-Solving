# 134. Gas Station
# 유일해가 존재한다고 했으므로 조건을 미충족시키는 경우를 소거하면서 O(n)으로 푼다.(파알인코드 참고)
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, tank = 0,0
        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]
        return start


test = Solution()
print(test.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # 3
print(test.canCompleteCircuit([2,3,4],[3,4,3]))  # -1
