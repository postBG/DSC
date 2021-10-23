def P2(nums: list) -> int:
    diff_map = {0: [-1]}
    diff_count = 0
    for idx, num in enumerate(nums):
        diff_count += 1 if num == 1 else -1
        if diff_count not in diff_map:
            diff_map[diff_count] = []
        diff_map[diff_count].append(idx)

    max_len = max([indices[-1] - indices[0] for _, indices in diff_map.items()])
    return max_len
