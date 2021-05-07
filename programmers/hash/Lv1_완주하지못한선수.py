import collections


def solution(participant, completion):
    total = participant + completion
    mdict = dict(collections.Counter(total))
    reverse = {v: k for k, v in mdict.items()}

    for k in reverse:
        if k % 2 != 0:
            answer = reverse.pop(k)
            break

    return answer