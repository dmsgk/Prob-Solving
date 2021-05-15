def solution(nums):
    number = len(nums) // 2
    variety = len(set(nums))

    return min(variety, number)