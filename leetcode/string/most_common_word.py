from typing import List
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        result = []
        result = re.sub(pattern='\W', repl=' ', string=paragraph).lower().split()
        counts = collections.Counter(result)

        li = counts.most_common(len(banned)+1)
        for i in li:
            if i[0] not in set(banned):
                return i[0]

test = Solution()
print(test.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
