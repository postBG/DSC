class Str(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if len(self.value) != len(other.value):
            return len(self.value) < len(other.value)

        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


def P4(lst: list) -> list:
    lst = [Str(s) for s in lst]
    sorted_lst = sorted(lst)
    return [s.value for s in sorted_lst]
