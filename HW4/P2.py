def P2(lst1: list, lst2: list) -> set:
    return {(a, b) for a, b in zip(lst1, lst2)}