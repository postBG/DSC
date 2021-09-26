def P1(filename: str) -> list:        
    with open(filename, 'r') as f:
        return [l.strip().split(' ') for l in f.readlines()]

