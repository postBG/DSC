from typing import List


def P8(L1: List[int], L2: List[int]) -> List[int]:
    return [a if a > b else b for a, b, in zip(L1, L2)]
