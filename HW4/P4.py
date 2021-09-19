import operator


def P4(dct: dict) -> str:
    return max(dct.items(), key=operator.itemgetter(1))[0]
