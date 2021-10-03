def P2(n: int) -> bool:
    primes = []
    copied_n = n
    for denom in range(2, n + 1):
        while copied_n % denom == 0:
            copied_n = copied_n // denom
            primes.append(denom)
    print(primes)
    return len(primes) == 2
