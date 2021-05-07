# 숫자카드2
# counter를 활용한 풀이
import collections

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
li = list(map(int, input().split()))

cards_dict = dict(collections.Counter(cards))
answer = []
for i in range(len(li)-1):
    if li[i] not in cards_dict:
        print(0, end = ' ')
    else:
        print(cards_dict[li[i]], end = ' ')
if li[-1] not in cards_dict:
    print(0, end = ' ')
else:
    print(cards_dict[li[-1]])



"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

# 3 0 0 1 2 0 0 2 출력
"""