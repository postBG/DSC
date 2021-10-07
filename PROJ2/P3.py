"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode


def P3(head: ListNode) -> ListNode:
    if head is None:
        return None

    curr_first = ListNode(head.val)
    runner = head.next
    while runner is not None:
        new_node = ListNode(runner.val)
        new_node.next = curr_first
        curr_first = new_node
        runner = runner.next

    return curr_first
