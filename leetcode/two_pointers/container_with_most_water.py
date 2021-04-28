# 11. Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        answer = 0

        while lp < rp:
            h = min(height[lp], height[rp])
            answer = max((rp - lp) * h, answer)

            if height[lp] == h:  # 왼쪽 기둥이 더 낮다
                lp += 1
            else:
                rp -= 1

        return answer


test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(test.maxArea([4,3,2,1,4])) # 16