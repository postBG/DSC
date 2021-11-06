def get_least_significant_one(num):
    return num & (num - 1) ^ num


def xor_all(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor


def split_nums_with_lso(nums, lso):
    has_lso = [num for num in nums if lso & num == lso]
    without_los = [num for num in nums if lso & num != lso]
    return has_lso, without_los


def P4(nums: list) -> set:
    xor_of_two = xor_all(nums)
    lso = get_least_significant_one(xor_of_two)

    nums_with_lso, nums_without_lso = split_nums_with_lso(nums, lso)
    return {xor_all(nums_with_lso), xor_all(nums_without_lso)}
