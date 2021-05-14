def solution(numbers):
    answer = []

    for num in numbers:
        temp = list(bin(num)[2:])
        length = len(temp)
        if length == bin(num).count("1") and num >= 3:
            li = ["1"] * (length + 1)
            li[1] = "0"
            b = "".join(li)
            answer.append(int(b, 2))
        elif bin(num)[-1] == '0' or num< 3:
            answer.append(num+1)            
        else:
            zero_num, one_num = -100,-100
            for i in range(1, length + 1):
                if temp[-i] == "0":
                    for j in range(length - i + 1, length):
                        if temp[j] == "1":
                            one_num = j
                            break
                    zero_num = length - i
                    break
            temp[zero_num] = "1"
            temp[one_num] = "0"
            answer.append(int("".join(temp), 2))

    return answer