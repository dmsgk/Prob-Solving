def findGCD(a, b):
    if a < b:
        a, b = b, a

    rem = a % b
    if rem == 0:
        return b

    return findGCD(b, rem)


def solution(w, h):
    gcd = findGCD(w, h)
    return w * h - (w + h - gcd)