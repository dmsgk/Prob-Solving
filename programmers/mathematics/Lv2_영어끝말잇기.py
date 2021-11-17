def solution(n, words):
    answer = []
    last_char = ""
    prev_words = set()

    for idx, word in enumerate(words):
        if word in prev_words:
            order = idx % n + 1
            answer.append(order)
            answer.append((idx) // n + 1)
            return answer
        if last_char == "" or last_char == word[0]:
            last_char = word[-1]
            prev_words.add(word)
        else:
            order = idx % n + 1
            answer.append(order)
            answer.append((idx) // n + 1)
            return answer
    return [0, 0]
