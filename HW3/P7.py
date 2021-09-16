from typing import List


def P7(num_list: List[int]) -> int:
    pos_list = [e for e in num_list if e > 0]
    return sum(pos_list)
