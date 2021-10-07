class LinkedNode(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MyStack(object):
    def __init__(self) -> None:
        self.sentinel = LinkedNode(0)
        self.size = 0

    def push(self, x: int) -> None:
        newFirst = LinkedNode(x)
        newFirst.next = self.sentinel.next
        self.sentinel.next = newFirst
        self.size += 1

    def top(self) -> int:
        if self.sentinel.next:
            return self.sentinel.next.val
        return None

    def pop(self) -> int:
        if self.sentinel.next is None:
            return None

        ret = self.sentinel.next.val
        self.sentinel.next = self.sentinel.next.next
        self.size -= 1
        return ret

    def isEmpty(self):
        return self.sentinel.next is None

    def getSize(self) -> int:  # Improved with caching!
        return self.size

