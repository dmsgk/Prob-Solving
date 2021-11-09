# 영수증
import sys

total = int(sys.stdin.readline())
for _ in range(9):
    book_price = int(sys.stdin.readline())
    total -= book_price

print(total)