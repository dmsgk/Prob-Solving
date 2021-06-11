import math


def solution(enroll, referral, seller, amount):
    answer = []
    relation_dict = {}
    money_dict = {}
    for i in range(len(enroll)):
        relation_dict[enroll[i]] = referral[i]
        money_dict[enroll[i]] = 0

    for j in range(len(seller)):
        money = amount[j] * 100
        person = seller[j]
        while money >= 10:
            portion = math.floor(money * 0.1)
            money_dict[person] += money - portion
            money = portion
            person = relation_dict[person]
            if person == '-':
                break
        if money < 10 and person != '-':
            money_dict[person] += money

    return list(money_dict.values())


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
# [360, 958, 108, 0, 450, 18, 180, 1080]
