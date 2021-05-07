def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)):
        j = i + 1
        if j < len(phone_book) and phone_book[j].startswith(phone_book[i]):
            return False

    return answer