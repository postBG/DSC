def P10(words: set, query_word: str) -> bool:
    candidates = [w for w in words if len(query_word) == len(w)]
    for w in candidates:
        diff = 0
        for c1, c2 in zip(w, query_word):
            if c1 != c2:
                diff += 1
        if diff == 1:
            return True
    return False
