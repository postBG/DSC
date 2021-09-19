from collections import defaultdict


def P8(vector1: dict, vector2: dict) -> dict:
    appended = defaultdict(list)
    for k, v in vector1.items():
        appended[k].append(v)
    for k, v in vector2.items():
        appended[k].append(v)

    return {k: sum(v) for k, v in appended.items() if sum(v) != 0}
