import sys
t = int(sys.stdin.readline())

for _ in range(t):  # 세번째로 큰 수
    li = list(map(int, sys.stdin.readline().split()))
    li.sort(reverse = True)
    print(li[2])
