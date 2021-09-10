# 다리놓기
import sys

def combi(n,k):
    result = 1
    for i in range(max(n-k+1, k+1), n+1):
        result *= i
    for j in range(1, min(n-k, k)+1):
        result //= j
    return result


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(combi(m,n))