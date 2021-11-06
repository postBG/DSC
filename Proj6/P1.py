def get_bin(num):
    cnt = 0
    while num != 1:
        num //= 2
        cnt += 1
    return cnt


def P1(m: int, n: int) -> int:
    ans = 0
    while m > 0 and n > 0:
        bm = get_bin(m)
        bn = get_bin(n)
        if bm != bn:
            return ans
        ans += 1 << bn
        m -= 1 << bn
        n -= 1 << bn
    return ans
