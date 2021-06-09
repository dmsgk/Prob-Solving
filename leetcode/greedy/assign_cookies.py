# 455. Assign Cookies
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = 0
        cnt = 0
        for cookie in s:
            for content in range(gi, len(g)):
                if cookie >= g[content]:
                    gi = content + 1
                    cnt += 1
                    break
        return cnt


"""
Runtime: 1260 ms, faster than 5.75% of Python3 online submissions for Assign Cookies.
Memory Usage: 16.1 MB, less than 38.43% of Python3 online submissions for Assign Cookies.
"""