from typing import List


def P6(alphabet_list: List[str]) -> int:
    for i, e in enumerate(alphabet_list):
        if 'A' <= e < 'a':
            idx = i
            return idx
    return -1
