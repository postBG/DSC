from collections import defaultdict


def P9(vector1: dict, vector2: dict) -> int:
    appended = defaultdict(list)
    for k, v in vector1.items():
        appended[k].append(v)
    for k, v in vector2.items():
        appended[k].append(v)

    return sum([v[0] * v[1] for k, v in appended.items() if 1 < len(v)])
