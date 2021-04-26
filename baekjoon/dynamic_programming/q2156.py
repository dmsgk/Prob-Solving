# 포도주 시식

num_of_glasses = int(input())
wine = [int(input()) for _ in range(num_of_glasses)]
result = [0] * (num_of_glasses+1)

for i in range(1, num_of_glasses+1):
    if i == 1:
        result[i] = wine[0]
    elif i == 2:
        result[i] = wine[0]+ wine[1]
    else:
        result[i] = max(result[i-2] + wine[i-1], result[i-3] + wine[i-2] + wine[i-1], result[i-1])

print(result[num_of_glasses])