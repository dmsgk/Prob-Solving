# 제로
k = int(input())
answer = []
for _ in range(k):
    n = int(input())
    if n != 0:
        answer.append(n)
    else:
        answer.pop()
print(sum(answer))

