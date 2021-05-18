from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)):
            a = s.pop()
            s.insert(i, a)
