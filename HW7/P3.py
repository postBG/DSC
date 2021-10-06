def P3(indexed_s: str) -> str:
    words = indexed_s.split(' ')
    words = [(int(w[-1]), w[:-1]) for w in words]
    sorted_words = [w for i, w in sorted(words)]
    return ' '.join(sorted_words)
