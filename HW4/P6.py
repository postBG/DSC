def P6(dct1: dict, dct2: dict) -> dict:
    return {k: v for k, v in dct1.items() if k in dct2 and v == dct2[k]}
