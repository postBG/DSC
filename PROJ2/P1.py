"""
**Instruction**
Please see instruction document.

"""
_PAIRS = {
    ')': '(',
    '}': '{',
    ']': '['
}


class Stack(object):
    def __init__(self):
        super().__init__()
        self._values = []

    def push(self, value):
        self._values.append(value)

    def pop(self):
        popped_value = self._values.pop(-1)
        return popped_value

    def __len__(self):
        return len(self._values)


def P1(parentheses: str) -> bool:
    stack = Stack()
    for c in parentheses:
        if c in ['(', '{', '[']:
            stack.push(c)
            continue
        if len(stack) == 0:
            return False

        top = stack.pop()
        if _PAIRS[c] == top:
            continue
        else:
            return False

    return len(stack) == 0
