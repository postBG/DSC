"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *
from collections import deque


def inner_inorder_lst(root, lst):
    if root is None:
        return
    inner_inorder_lst(root.left, lst)
    lst.append(root.val)
    inner_inorder_lst(root.right, lst)


def inorder_lst(root):
    lst = []
    inner_inorder_lst(root, lst)
    return lst


def augment_inorder_lst(val, lst):
    for i, v in enumerate(lst):
        if val < v:
            lst.insert(i, val)
            return lst

    lst.append(val)
    return lst


def has_only_one_child(node):
    has_left = node.left is not None
    has_right = node.right is not None
    return (has_left and not has_right) or (not has_left and has_right)


def find_one_child_parent(root):
    if root is None or has_only_one_child(root):
        return root

    left_search = find_one_child_parent(root.left)
    if left_search is not None:
        return left_search

    right_search = find_one_child_parent(root.right)
    if right_search is not None:
        return right_search


def fill_up_empty_node(root):
    one_child_parent = find_one_child_parent(root)

    node = TreeNode(None)
    if one_child_parent.left is None:
        one_child_parent.left = node
    else:
        one_child_parent.right = node


def reorder_nodes(root, queue):
    if root is None or len(queue) == 0:
        return

    reorder_nodes(root.left, queue)
    root.val = queue.popleft()
    reorder_nodes(root.right, queue)


def P3(root: TreeNode, val: int) -> TreeNode:
    lst = inorder_lst(root)
    queue = deque(augment_inorder_lst(val, lst))
    fill_up_empty_node(root)
    reorder_nodes(root, queue)
    return root
