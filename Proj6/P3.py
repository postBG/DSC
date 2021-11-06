def P3(num: int) -> int:
    ans = 0
    for _ in range(32):
        ans = ans << 1
        ans += num & 1
        num = num >> 1
    return ans
