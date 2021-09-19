def P7(dct: dict) -> int:
    keysets_of_inner_dicts = list(set(d.keys()) for d in dct.values())
    pivot = keysets_of_inner_dicts[0]
    for keyset in keysets_of_inner_dicts:
        if keyset != pivot:
            return 0
    return 1
