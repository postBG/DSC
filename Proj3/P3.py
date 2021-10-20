"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *
from collections import deque


def is_leaf(node):
    return node.left is None and node.right is None


def min_node_with_parent_node(node, parent):
    curr = node
    while curr.left is not None:
        parent = curr
        curr = curr.left

    return curr, parent


def max_node_with_parent_node(node, parent):
    curr = node
    while curr.right is not None:
        parent = curr
        curr = curr.right

    return curr, parent


def bring_to_root_and_delete(root, node, parent):
    if node is parent.left:
        parent.left = None
    if node is parent.right:
        parent.right = None

    root.val = node.val


def count_node(root):
    if root is None:
        return 0

    if is_leaf(root):
        return 1

    return count_node(root.left) + count_node(root.right) + 1


def is_left_full(root):
    left_child_num = count_node(root.left)
    right_child_num = count_node(root.right)
    return right_child_num < left_child_num


def insert_val_to_deficient_bst(val, bst_root, root_parent):
    if bst_root is None:
        if root_parent.left is None:
            root_parent.left = TreeNode(val)
            return
        if root_parent.right is None:
            root_parent.right = TreeNode(val)
            return
    if val < bst_root.val and is_left_full(bst_root):
        insert_val_to_deficient_bst(bst_root.val, bst_root.right, bst_root)
        left_max_node, left_max_node_parent = max_node_with_parent_node(bst_root.left, bst_root)
        if left_max_node.val < val:
            bst_root.val = val
            return
        bring_to_root_and_delete(bst_root, left_max_node, left_max_node_parent)
        insert_val_to_deficient_bst(val, bst_root.left, bst_root)
    elif val < bst_root.val and not is_left_full(bst_root):
        insert_val_to_deficient_bst(val, bst_root.left, bst_root)
    elif bst_root.val < val and not is_left_full(bst_root):
        insert_val_to_deficient_bst(bst_root.val, bst_root.left, bst_root)
        right_min_node, right_min_node_parent = min_node_with_parent_node(bst_root.right, bst_root)
        if val < right_min_node.val:
            bst_root.val = val
            return
        bring_to_root_and_delete(bst_root, right_min_node, right_min_node_parent)
        insert_val_to_deficient_bst(val, bst_root.right, bst_root)
    else:
        insert_val_to_deficient_bst(val, bst_root.right, bst_root)


def P3(root: TreeNode, val: int) -> TreeNode:
    insert_val_to_deficient_bst(val, root, None)
    return root
