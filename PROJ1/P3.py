_LOOKUP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def is_alpha(char):
    return 'A' <= char <= 'z'


def is_number(char):
    return '0' <= char <= '9'


def is_matching_exists(s, start_idx, last_idx):
    sub_s = s[start_idx:last_idx]
    return sub_s in _LOOKUP


def need_cut(s, start_idx, last_idx):
    if len(s) <= last_idx or is_number(s[last_idx]):
        return True

    if is_alpha(s[last_idx]):
        return is_number(s[start_idx]) or is_matching_exists(s, start_idx, last_idx)


def tokenizer(s):
    tokens = []
    start_idx = 0
    last_idx = 0
    while last_idx < len(s):
        last_idx += 1
        if need_cut(s, start_idx, last_idx):
            tokens.append(s[start_idx:last_idx])
            start_idx = last_idx

    return tokens


def tokens_to_numbers(tokens):
    return [_LOOKUP[token] if token in _LOOKUP else token for token in tokens]


def P3(s: str) -> int:
    tokens = tokenizer(s)
    numbers = tokens_to_numbers(tokens)
    return int(''.join(numbers))
