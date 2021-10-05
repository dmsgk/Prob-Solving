# 듣보잡
import sys

n, m = map(int, sys.stdin.readline().split())
not_heard = set()
not_seen = set()

for _ in range(n):
    not_heard.add(sys.stdin.readline().strip())
for _ in range(m):
    not_seen.add(sys.stdin.readline().strip())

ans = list(not_heard.intersection(not_seen))
ans.sort()
print(len(ans))
for person in ans:
    print(person)