def get_bin(num):
    cnt = 0
    while num != 1:
        num //= 2
        cnt += 1
    return cnt


def P1(m: int, n: int) -> int:
    if m == 0:
        return 0
    bm = get_bin(m)
    bn = get_bin(n)
    return 1 << bn if bm == bn else 0
