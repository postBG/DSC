def P4(filename: str) -> list:
    with open(filename, 'r') as f:
        return [l for l in f.readlines() if not (l.startswith('#') or l.startswith('//'))]
