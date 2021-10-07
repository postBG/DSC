"""
**Instruction**
Please see instruction document.

"""


class Stack(object):
    def __init__(self):
        super().__init__()
        self._values = []

    def push(self, value):
        self._values.append(value)

    def pop(self):
        popped_value = self._values.pop(-1)
        return popped_value

    def top(self):
        return self._values[-1]

    def __len__(self):
        return len(self._values)


def P2(stock_price: list) -> list:
    days = []
    for i in range(len(stock_price)):
        stack = Stack()
        for j in range(len(stock_price) - 1, i, -1):
            stack.push(stock_price[j])
        buy_at = stock_price[i]
        cnt = 0
        while 0 < len(stack):
            v = stack.top()
            cnt += 1
            if buy_at < v:
                days.append(cnt)
                break
            stack.pop()
        if len(stack) == 0:
            days.append(0)
    return days
