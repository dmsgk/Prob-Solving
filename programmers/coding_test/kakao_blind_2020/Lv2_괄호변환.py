def split_str(s):
    u_dict = {'(': 0, ')': 0}
    for idx, char in enumerate(s):
        u_dict[char] += 1
        if u_dict['('] == u_dict[')']:
            u = s[:idx+1]
            v = s[idx+1:]
            return u, v


def isCorrectStr(s):
    stack = []
    for idx,  char in enumerate(s):
        if idx == 0:
            stack.append(char)
            continue
        prev = stack[-1]
        if prev == '(' and char == ')':
            stack.pop()
        else:
            stack.append(char)
    if stack: # 남아있는 경우
        return False

    return True


def reverse_str(s):
    ans = ""
    for char in s:
        if char == '(':
            ans += ')'
        else:
            ans += '('
    return ans


def solution(p):
    if p == "":
        return ""

    u, v = split_str(p)
    if isCorrectStr(u):
        return u + solution(v)
    else:
        u_strip = u[1:-1]
        ans = "(" + solution(v) + ")" + reverse_str(u_strip)
        return ans


print(solution("(()())()"))  # "(()())()"
print(solution(")("))   # "()"
print(solution("()))((()"))  # "()(())()"
