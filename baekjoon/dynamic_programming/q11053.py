# 가장 긴 증가하는 부분수열
n = int(input())
arr = list(map(int, input().split()))

result = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] = max(result[j]+1, result[i])

print(max(result))

"""
10
1 100 2 3 4 5 6 7 8 9   
 => 9출력 

8
10 20 30 5 10 20 30 40
 => 5 출력
 
6
10 1 10 30 20 20
 => 3 출력
 
 
6
10 20 10 30 20 50
 => 4 출력 
"""