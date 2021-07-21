def solution(s):
    str_num_dict = {
        "zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7',
        "eight": '8', "nine": '9'}

    ans = ''
    temp = ''
    for c in s:
        if c.isdigit():
            ans += c
        else:
            temp += c
            if temp in str_num_dict:
                ans += str_num_dict[temp]
                temp = ''

    return int(ans)