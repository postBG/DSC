from typing import List


def P9(n1: int, n2: int) -> List[int]:
    low, high = min(n1, n2), max(n1, n2)
    return list(range(high, low - 1, -1))
