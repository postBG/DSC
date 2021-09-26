def P5(filename: str) -> int:
    with open(filename, 'r') as f:
        words = []
        for l in f.readlines():
            words.extend(l.strip().split(' '))
    lengths = [len(word) for word in words]
    return max(lengths)
