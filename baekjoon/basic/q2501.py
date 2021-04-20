import sys
import math
n, k = map(int, sys.stdin.readline().split())

l = []
i = 1
while i <= n//2:import sys
import math
n, k = map(int, sys.stdin.readline().split())

l = []
i = 1
while i <= n//2:
    if n % i == 0 and i not in l:
        l.append(i)
        if i != n//i:
           l.append(n//i)
    i += 1

l.sort()

if k> len(l):
    print(0)
else:
    print(l[k-1])

    if n % i == 0 and i not in l:
        l.append(i)
        if i != n//i:
           l.append(n//i)
    i += 1

l.sort()

if k> len(l):
    print(0)
else:
    print(l[k-1])
