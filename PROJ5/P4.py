def series_max_len(num, cache):
    if cache[num] != -1:
        return cache[num]

    if num + 1 not in cache:
        cache[num] = 1
        return cache[num]
    max_len = series_max_len(num + 1, cache) + 1
    cache[num] = max_len
    return cache[num]


def P4(nums: list) -> int:
    cache = {i: -1 for i in nums}
    return max([series_max_len(i, cache) for i in nums])
