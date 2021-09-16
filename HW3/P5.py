from typing import List


def P5(word_num_list: List[list]) -> list:
    word_list = [w for w, l in word_num_list]
    word_list.sort()
    return word_list
