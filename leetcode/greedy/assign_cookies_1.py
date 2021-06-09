from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i

"""
Runtime: 232 ms, faster than 15.90% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.9 MB, less than 63.55% of Python3 online submissions for Assign Cookies.
"""