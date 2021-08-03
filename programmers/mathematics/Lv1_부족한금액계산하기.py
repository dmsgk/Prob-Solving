def solution(price, money, count):
    total_price = price * (count * (count + 1) // 2)
    if money >= total_price:
        return 0

    return total_price - money