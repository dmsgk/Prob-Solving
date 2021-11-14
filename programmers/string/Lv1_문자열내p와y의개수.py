from collections import defaultdict


def solution(s):
    counter_dict = defaultdict(int)
    for char in s.lower():
        counter_dict[char] += 1

    if counter_dict['p'] == counter_dict['y']:
        return True

    return False