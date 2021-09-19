from collections import defaultdict


def P1(lst: list) -> set:
    counts = defaultdict(int)
    for e in lst:
        counts[e] += 1

    return {number for number, count in counts.items() if 1 < count}
