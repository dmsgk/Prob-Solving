# 그룹단어 체커
import sys

n = int(sys.stdin.readline())
checker = 0
for _ in range(n):
    char_dict = dict()
    word = sys.stdin.readline().rstrip()

    for i, char in enumerate(word):
        if char not in char_dict:
            char_dict[char] = i
            continue
        if char_dict[char] + 1 < i:
            break

        char_dict[char] = i
    else:
        checker += 1

print(checker)



