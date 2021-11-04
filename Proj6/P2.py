def P2(n: int) -> bool:
    last_bit = n & 1

    while n != 0:
        n_last_bit = n & 1
        if last_bit != n_last_bit:
            return False
        n = n >> 1
        last_bit = last_bit ^ 1
    return True
