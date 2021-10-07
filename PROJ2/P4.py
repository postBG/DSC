from linked_list_helper import ListNode


def num_to_lst(num):
    lst = []
    curr = num
    while curr:
        lst.append(curr % 10)
        curr = curr // 10
    return list(reversed(lst))


def l2n(lst: ListNode):
    total = 0
    runner = lst
    while runner is not None:
        total = total * 10 + runner.val
        runner = runner.next
    return total


def n2l(num: int):
    curr_head = ListNode(num % 10)
    curr = num // 10
    while curr:
        new_node = ListNode(curr % 10)
        new_node.next = curr_head
        curr_head = new_node
        curr = curr // 10
    return curr_head


def P4(num1: ListNode, num2: ListNode) -> ListNode:
    return n2l(l2n(num1) + l2n(num2))
