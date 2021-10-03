_BEATER_LOOK_UP = {
    'R': 'P',
    'S': 'R',
    'P': 'S'
}
_LOSER_LOOK_UP = {
    'R': 'S',
    'S': 'P',
    'P': 'R'
}


def _B_score(match):
    a, b, c = match
    if _BEATER_LOOK_UP[b] in [a, c]:
        return 0

    return 1 if _LOSER_LOOK_UP[b] in [a, c] else 0


def P1(game: list) -> int:
    return sum([_B_score(match) for match in game])
