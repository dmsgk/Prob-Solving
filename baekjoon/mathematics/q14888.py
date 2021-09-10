import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
num_li = list(map(int, sys.stdin.readline().strip().split()))
oper_li = list(map(int, sys.stdin.readline().strip().split()))   # + - * /
oper_str = []
result_li = []
for i in range(4):
    if i == 0:
        for _ in range(oper_li[i]):
            oper_str.append('+')
    elif i == 1:
        for _ in range(oper_li[i]):
            oper_str.append('-')
    elif i == 2:
        for _ in range(oper_li[i]):
            oper_str.append('*')
    else:
        for _ in range(oper_li[i]):
            oper_str.append('//')

perm_set = set(permutations(oper_str, n-1))

for s in perm_set:
    result = num_li[0]
    for i in range(n-1):
        if s[i] == '+':
            result += num_li[i+1]
        elif s[i] == '-':
            result -= num_li[i+1]
        elif s[i] == '*':
            result *= num_li[i+1]
        else:
            if result < 0:
                result = -((-result) //num_li[i+1])
            else:
                result = result // num_li[i+1]
    result_li.append(result)

print(max(result_li))
print(min(result_li))