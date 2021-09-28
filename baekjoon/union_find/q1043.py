# 거짓말
import sys

n, m = map(int, sys.stdin.readline().split())
truth = sys.stdin.readline()
t_set = set(map(int,truth.split()[1:]))

party = []
result = []
for _ in range(m):
    p_set = set(map(int, sys.stdin.readline().split()[1:]))
    party.append(p_set)
    result.append(1)

for _ in range(m):
    for idx, par in enumerate(party):
        if t_set & par:
            result[idx] = 0
            t_set = t_set | par

print(sum(result))