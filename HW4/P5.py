from collections import defaultdict


def P5(dct: dict) -> list:
    counts = defaultdict(int)
    for e in dct.values():
        counts[e] += 1

    return list({number for number, count in counts.items() if 1 < count})
