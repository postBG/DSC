def series_max_len(num, visited, curr_max_count):
    if visited[num] == 1:
        return curr_max_count

    max_count = 1
    while num + 1 in visited:
        visited[num] = 1
        max_count += 1
        num += 1

    return max_count if curr_max_count < max_count else curr_max_count


def P4(nums: list) -> int:
    visited = {i: 0 for i in nums}
    max_count = 0
    for num in nums:
        max_count = series_max_len(num, visited, max_count)
    return max_count
