def P3(A: list, B: list) -> int:
    diff_map = {0: [-1]}
    diff_count = 0
    for idx, (a, b) in enumerate(zip(A, B)):
        diff_count += a - b
        if diff_count not in diff_map:
            diff_map[diff_count] = []
        diff_map[diff_count].append(idx)

    max_len = max([indices[-1] - indices[0] for _, indices in diff_map.items()])
    return max_len
