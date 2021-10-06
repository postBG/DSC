def P2(Order: str, S: str) -> str:
    head = {c: 0 for c in Order}
    tail = []
    for c in S:
        if c in head:
            head[c] += 1
        else:
            tail.append(c)

    str1 = []
    for c, n in head.items():
        str1.extend([c] * n)

    str1.extend(tail)
    return ''.join(str1)
