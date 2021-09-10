import sys

n, k = map(int, sys.stdin.readline().split())

def combi(n,k):
    result = 1
    for i in range(max(n-k+1, k+1), n+1):
        result *= i
    for j in range(1, min(n-k, k)+1):
        result //= j
    return result % 10007


print(combi(n,k))