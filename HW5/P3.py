def P3(filename: str) -> list:
    with open(filename, 'r') as f:
        return [l for l in reversed(f.readlines())]
