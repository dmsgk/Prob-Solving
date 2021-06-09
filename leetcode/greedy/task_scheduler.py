# 621. task scheduler
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        counter = Counter(tasks)
        while 1:
            sub_cnt = 0
            for task, _ in counter.most_common(n+1):
                sub_cnt += 1
                ans += 1

                counter.subtract(task)
                counter += Counter()
            if not counter:
                break
            ans += n - sub_cnt + 1
        return ans

test = Solution()
print(test.leastInterval(["A","A","A","B","B","B"], 2))  # 8
print(test.leastInterval(["A","A","A","B","B","B"], 0))  # 6
print(test.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))  # 16
