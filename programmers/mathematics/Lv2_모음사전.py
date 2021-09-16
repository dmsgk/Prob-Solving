from itertools import product


def solution(word):
    li = []
    for i in range(1, 6):
        li += list(product(list('AEIOU'), repeat=i))
    li.sort()

    word_tup = tuple(word)
    return li.index(word_tup) + 1