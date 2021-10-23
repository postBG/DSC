def construct_modular_count_dict(nums, k):
    count_dict = {i: 0 for i in range(k)}
    for i in nums:
        mod = i % k
        count_dict[mod] += 1
    return count_dict


def check_count_dict(count_dict, k):
    for i in range(k):
        if i == 0:
            if count_dict[i] % 2 != 0:
                return False
            continue
        if count_dict[i] != count_dict[k - i]:
            return False
    return True


def P1(nums: list, k: int) -> bool:
    count_dict = construct_modular_count_dict(nums, k)
    return check_count_dict(count_dict, k)
