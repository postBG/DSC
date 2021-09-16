from typing import List


def P10(word_list: List[str]) -> List[str]:
    return [w for w in word_list if w.startswith('a') or w.startswith('A')]
