from linked_list_helper import ListNode


def reverse(head: ListNode) -> ListNode:
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


def to_num(node):
    return 0 if node is None else node.val


def sum_node_with_carry(node1, node2, carry):
    n1 = to_num(node1)
    n2 = to_num(node2)
    total = n1 + n2 + carry
    return total % 10, total // 10


def sum_list(num1, num2):
    runner1 = num1
    runner2 = num2
    carry = 0

    current_val, carry = sum_node_with_carry(runner1, runner2, carry)
    head = ListNode(current_val)
    while (runner1 is not None) or (runner2 is not None):
        runner1 = runner1.next if runner1 else None
        runner2 = runner2.next if runner2 else None
        current_val, carry = sum_node_with_carry(runner1, runner2, carry)

        if runner1 is None and runner2 is None and current_val == 0:
            break

        curr_node = ListNode(current_val)
        curr_node.next = head
        head = curr_node
    return head


def P4(num1: ListNode, num2: ListNode) -> ListNode:
    return sum_list(reverse(num1), reverse(num2))
